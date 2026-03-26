from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Event:
    id: UUID
    user_id: str
    feature_key: str
    event_type: str
    timestamp: datetime
    properties: dict[str, str | int | float | bool | None]