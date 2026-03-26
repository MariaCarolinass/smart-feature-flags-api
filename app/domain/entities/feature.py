from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Feature:
    id: UUID
    name: str
    key: str
    description: str | None
    enabled: bool
    rollout_percentage: int
    ml_enabled: bool
    created_at: datetime
    updated_at: datetime