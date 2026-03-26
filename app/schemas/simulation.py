from pydantic import BaseModel, Field


class SimulateUsersRequest(BaseModel):
    count: int = Field(ge=1, le=100000)


class SimulateEventsRequest(BaseModel):
    count: int = Field(ge=1, le=100000)
    feature_key: str