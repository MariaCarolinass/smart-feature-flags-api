import random
from datetime import datetime, timezone, timedelta

from app.domain.services.event_service import EventService


class SimulationService:
    PLANS = ["free", "basic", "premium"]
    COUNTRIES = ["BR", "US", "AR", "PT"]

    def __init__(self, event_service: EventService) -> None:
        self.event_service = event_service

    def simulate_users(self, count: int) -> list[dict]:
        users: list[dict] = []
        for i in range(count):
            users.append(
                {
                    "user_id": f"user_{i + 1}",
                    "age": random.randint(18, 70),
                    "country": random.choice(self.COUNTRIES),
                    "plan": random.choice(self.PLANS),
                    "days_since_signup": random.randint(1, 1000),
                }
            )
        return users

    def simulate_events(self, count: int, feature_key: str) -> list[dict]:
        events = []

        for _ in range(count):
            event = self.event_service.create_event(
                user_id=f"user_{random.randint(1, 1000)}",
                feature_key=feature_key,
                event_type=random.choice(
                    [
                        "viewed_feature",
                        "clicked_banner",
                        "used_feature",
                        "completed_flow",
                    ]
                ),
                timestamp=datetime.now(timezone.utc)
                - timedelta(minutes=random.randint(0, 50000)),
                properties={
                    "device": random.choice(["mobile", "desktop"]),
                    "session_length": random.randint(30, 1800),
                },
            )
            events.append(event)

        return events