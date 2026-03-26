from abc import ABC, abstractmethod

from app.domain.entities.model_metadata import ModelMetadata


class ModelRepository(ABC):
    @abstractmethod
    def save_status(self, metadata: ModelMetadata) -> ModelMetadata:
        raise NotImplementedError

    @abstractmethod
    def get_status(self) -> ModelMetadata:
        raise NotImplementedError