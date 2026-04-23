from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class TrainingJob:
    job_id: str
    status: str
    submitted_at: datetime
    started_at: datetime | None = None
    finished_at: datetime | None = None
    result: dict | None = None
    error: str | None = None
