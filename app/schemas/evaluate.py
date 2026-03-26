from pydantic import BaseModel, Field, ConfigDict


class EvaluateUser(BaseModel):
    user_id: str
    age: int | None = Field(default=None, ge=0, le=120)
    country: str | None = None
    plan: str | None = None
    days_since_signup: int | None = Field(default=None, ge=0)


class EvaluateRequest(BaseModel):
    feature_key: str
    user: EvaluateUser

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "feature_key": "new_home",
                "user": {
                    "user_id": "u123",
                    "age": 29,
                    "country": "BR",
                    "plan": "premium",
                    "days_since_signup": 45
                }
            }
        }
    )


class EvaluateResponse(BaseModel):
    feature_key: str
    user_id: str
    enabled: bool
    decision_source: str
    score: float | None = None
    model_version: str | None = None