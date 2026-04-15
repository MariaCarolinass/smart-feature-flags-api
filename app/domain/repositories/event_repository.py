from abc import ABC, abstractmethod

from uuid import UUID

from app.domain.entities.event import Event


class EventRepository(ABC):
    @abstractmethod
    def create(self, event: Event) -> Event:
        raise NotImplementedError

    @abstractmethod
    def list(
        self,
        user_id: str | None = None,
        feature_key: str | None = None,
        event_type: str | None = None,
    ) -> list[Event]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, event_id: UUID) -> Event | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, event: Event) -> Event:
        raise NotImplementedError

    @abstractmethod
    def delete(self, event_id: UUID) -> bool:
        raise NotImplementedError