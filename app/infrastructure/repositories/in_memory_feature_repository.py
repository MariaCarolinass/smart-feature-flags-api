from uuid import UUID

from app.domain.entities.feature import Feature
from app.domain.repositories.feature_repository import FeatureRepository


class InMemoryFeatureRepository(FeatureRepository):
    def __init__(self) -> None:
        self._by_id: dict[UUID, Feature] = {}
        self._by_key: dict[str, Feature] = {}

    def create(self, feature: Feature) -> Feature:
        self._by_id[feature.id] = feature
        self._by_key[feature.key] = feature
        return feature

    def list(self) -> list[Feature]:
        return list(self._by_id.values())

    def get_by_id(self, feature_id: UUID) -> Feature | None:
        return self._by_id.get(feature_id)

    def get_by_key(self, key: str) -> Feature | None:
        return self._by_key.get(key)
