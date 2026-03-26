from datetime import datetime, timezone
from uuid import uuid4, UUID

from app.domain.entities.feature import Feature
from app.domain.repositories.feature_repository import FeatureRepository


class FeatureService:
    def __init__(self, feature_repository: FeatureRepository) -> None:
        self.feature_repository = feature_repository

    def create_feature(
        self,
        name: str,
        key: str,
        description: str | None,
        enabled: bool,
        rollout_percentage: int,
        ml_enabled: bool,
    ) -> Feature:
        existing = self.feature_repository.get_by_key(key)
        if existing is not None:
            raise ValueError(f"Feature with key '{key}' already exists.")

        now = datetime.now(timezone.utc)

        feature = Feature(
            id=uuid4(),
            name=name,
            key=key,
            description=description,
            enabled=enabled,
            rollout_percentage=rollout_percentage,
            ml_enabled=ml_enabled,
            created_at=now,
            updated_at=now,
        )

        return self.feature_repository.create(feature)

    def list_features(self) -> list[Feature]:
        return self.feature_repository.list()

    def get_feature_by_id(self, feature_id: UUID) -> Feature | None:
        return self.feature_repository.get_by_id(feature_id)