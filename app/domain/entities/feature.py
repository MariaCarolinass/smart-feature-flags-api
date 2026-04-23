from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Feature:
    id: int | None
    name: str
    key: str
    description: str | None
    enabled: bool
    rollout_percentage: int
    ml_enabled: bool
    created_at: datetime
    updated_at: datetime