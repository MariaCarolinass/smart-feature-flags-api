from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from threading import Lock
from uuid import uuid4

from app.core.logging import get_logger
from app.domain.entities.training_job import TrainingJob
from app.domain.repositories.training_job_repository import TrainingJobRepository
from app.domain.services.training_service import TrainingService

logger = get_logger(__name__)


class TrainingJobService:
    def __init__(
        self,
        training_service: TrainingService,
        training_job_repository: TrainingJobRepository,
        *,
        max_workers: int = 1,
        max_jobs: int = 500,
        retention_minutes: int = 60,
    ) -> None:
        self._training_service = training_service
        self._training_job_repository = training_job_repository
        self._executor = ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="training-job")
        self._lock = Lock()
        self._max_jobs = max(1, max_jobs)
        self._retention_minutes = max(1, retention_minutes)

    def start(self) -> dict:
        now = datetime.now(timezone.utc)
        job_id = uuid4().hex
        job = TrainingJob(
            job_id=job_id,
            status="queued",
            submitted_at=now,
        )
        with self._lock:
            self._training_job_repository.create(job)
            self._prune_jobs(now)
        self._executor.submit(self._run_job, job_id)
        return self._to_dict(job)

    def get(self, job_id: str) -> dict | None:
        with self._lock:
            self._prune_jobs(datetime.now(timezone.utc))
            job = self._training_job_repository.get(job_id)
            return self._to_dict(job) if job else None

    def _run_job(self, job_id: str) -> None:
        with self._lock:
            job = self._training_job_repository.get(job_id)
            if job is None:
                logger.warning("Async training job disappeared before execution: job_id=%s", job_id)
                return
            job.status = "running"
            job.started_at = datetime.now(timezone.utc)
            self._training_job_repository.update(job)

        try:
            result = self._training_service.train()
        except Exception as exc:
            logger.exception("Async training job failed: job_id=%s", job_id)
            with self._lock:
                job = self._training_job_repository.get(job_id)
                if job is None:
                    logger.warning("Async training job disappeared while failing: job_id=%s", job_id)
                    return
                job.status = "failed"
                job.finished_at = datetime.now(timezone.utc)
                job.error = str(exc)
                self._training_job_repository.update(job)
            return

        with self._lock:
            job = self._training_job_repository.get(job_id)
            if job is None:
                logger.warning("Async training job disappeared while succeeding: job_id=%s", job_id)
                return
            job.status = "succeeded"
            job.finished_at = datetime.now(timezone.utc)
            job.result = self._to_jsonable(result)
            self._training_job_repository.update(job)

    def _prune_jobs(self, now: datetime) -> None:
        self._training_job_repository.prune(
            now=now,
            max_jobs=self._max_jobs,
            retention_minutes=self._retention_minutes,
        )

    @staticmethod
    def _to_jsonable(data: dict) -> dict:
        return json.loads(json.dumps(data, default=str))

    @staticmethod
    def _to_dict(job: TrainingJob) -> dict:
        return {
            "job_id": job.job_id,
            "status": job.status,
            "submitted_at": job.submitted_at,
            "started_at": job.started_at,
            "finished_at": job.finished_at,
            "result": job.result,
            "error": job.error,
        }
