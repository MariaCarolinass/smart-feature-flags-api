from datetime import datetime, timezone

from app.core.event_types import POSITIVE_EVENT_TYPES
from app.core.exceptions import ValidationError
from app.domain.entities.model_metadata import ModelMetadata
from app.domain.repositories.event_repository import EventRepository
from app.domain.repositories.model_repository import ModelRepository
from app.infrastructure.ml.trainer import train_from_events


class TrainingService:
    def __init__(self, event_repository: EventRepository, model_repository: ModelRepository) -> None:
        self.event_repository = event_repository
        self.model_repository = model_repository

    def train(self) -> dict:
        started_at = datetime.now(timezone.utc)
        events = self.event_repository.list()
        if not events:
            raise ValidationError("Training requires at least one event.")

        total_events = len(events)
        unique_users = len({event.user_id for event in events})
        positive_events = sum(1 for event in events if event.event_type in POSITIVE_EVENT_TYPES)

        try:
            result = train_from_events(events)
        except ValueError as exc:
            raise ValidationError(str(exc)) from exc

        metadata = ModelMetadata(
            status="ready",
            model_name=result["model_name"],
            model_version=result["model_version"],
            trained_at=result["trained_at"],
            metrics=result["metrics"],
            artifact_path=result["artifact_path"],
        )

        saved = self.model_repository.save_status(metadata)
        duration_ms = int((datetime.now(timezone.utc) - started_at).total_seconds() * 1000)

        return {
            "status": saved.status,
            "model_name": saved.model_name,
            "model_version": saved.model_version,
            "artifact_path": saved.artifact_path,
            "trained_at": saved.trained_at,
            "metrics": saved.metrics,
            "process": {
                "total_events": total_events,
                "unique_users": unique_users,
                "positive_events": positive_events,
                "duration_ms": duration_ms,
                "feature_columns": result.get("feature_columns", []),
            },
        }

    def get_status(self) -> ModelMetadata:
        return self.model_repository.get_status()