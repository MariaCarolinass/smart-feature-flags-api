from app.domain.entities.event import Event
from app.domain.repositories.event_repository import EventRepository


class InMemoryEventRepository(EventRepository):
    def __init__(self) -> None:
        self._events: list[Event] = []

    def create(self, event: Event) -> Event:
        self._events.append(event)
        return event

    def list(
        self,
        user_id: str | None = None,
        feature_key: str | None = None,
        event_type: str | None = None,
    ) -> list[Event]:
        out = self._events
        if user_id is not None:
            out = [e for e in out if e.user_id == user_id]
        if feature_key is not None:
            out = [e for e in out if e.feature_key == feature_key]
        if event_type is not None:
            out = [e for e in out if e.event_type == event_type]
        return list(out)
