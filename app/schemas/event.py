from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class EventCreate(BaseModel):
    user_id: str = Field(min_length=1, max_length=100)
    feature_key: str = Field(min_length=1, max_length=50)
    event_type: str = Field(min_length=1, max_length=50)
    timestamp: datetime
    properties: dict[str, str | int | float | bool | None] = Field(default_factory=dict)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "user_id": "u123",
                "feature_key": "new_home",
                "event_type": "clicked_banner",
                "timestamp": "2026-03-25T10:00:00Z",
                "properties": {
                    "device": "mobile",
                    "session_length": 180
                }
            }
        }
    )


class EventResponse(BaseModel):
    id: UUID
    user_id: str
    feature_key: str
    event_type: str
    timestamp: datetime
    properties: dict[str, str | int | float | bool | None]