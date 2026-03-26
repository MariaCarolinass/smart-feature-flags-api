from datetime import datetime, timezone

from app.domain.entities.model_metadata import ModelMetadata
from app.domain.repositories.model_repository import ModelRepository


class TrainingService:
    def __init__(self, model_repository: ModelRepository) -> None:
        self.model_repository = model_repository

    def train(self) -> ModelMetadata:
        metadata = ModelMetadata(
            status="ready",
            model_name="mock_logistic_regression",
            model_version="v1",
            trained_at=datetime.now(timezone.utc),
            metrics={
                "accuracy": 0.81,
                "f1_score": 0.78,
            },
        )
        return self.model_repository.save_status(metadata)

    def get_status(self) -> ModelMetadata:
        return self.model_repository.get_status()