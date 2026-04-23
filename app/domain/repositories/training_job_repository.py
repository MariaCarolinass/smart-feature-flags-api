from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

from app.domain.entities.training_job import TrainingJob


class TrainingJobRepository(ABC):
    @abstractmethod
    def create(self, job: TrainingJob) -> TrainingJob:
        raise NotImplementedError

    @abstractmethod
    def get(self, job_id: str) -> TrainingJob | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, job: TrainingJob) -> TrainingJob:
        raise NotImplementedError

    @abstractmethod
    def prune(self, *, now: datetime, max_jobs: int, retention_minutes: int) -> None:
        raise NotImplementedError
