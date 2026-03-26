from datetime import datetime
from pydantic import BaseModel


class TrainResponse(BaseModel):
    status: str
    model_version: str
    trained_at: datetime
    metrics: dict[str, float]


class ModelStatusResponse(BaseModel):
    status: str
    model_name: str | None = None
    model_version: str | None = None
    trained_at: datetime | None = None
    metrics: dict[str, float] | None = None