from app.domain.entities.model_metadata import ModelMetadata
from app.domain.repositories.model_repository import ModelRepository


class InMemoryModelRepository(ModelRepository):
    def __init__(self) -> None:
        self._metadata = ModelMetadata(
            status="idle",
            model_name=None,
            model_version=None,
            trained_at=None,
            metrics=None,
        )

    def save_status(self, metadata: ModelMetadata) -> ModelMetadata:
        self._metadata = metadata
        return metadata

    def get_status(self) -> ModelMetadata:
        return self._metadata
