from app.domain.services.event_service import EventService
from app.domain.services.evaluation_service import EvaluationService
from app.domain.services.feature_service import FeatureService
from app.domain.services.simulation_service import SimulationService
from app.domain.services.training_service import TrainingService

from app.domain.repositories.feature_repository import FeatureRepository
from app.domain.repositories.event_repository import EventRepository
from app.domain.repositories.model_repository import ModelRepository
from app.infrastructure.repositories.in_memory_event_repository import (
    InMemoryEventRepository,
)
from app.infrastructure.repositories.in_memory_feature_repository import (
    InMemoryFeatureRepository,
)
from app.infrastructure.repositories.in_memory_model_repository import (
    InMemoryModelRepository,
)

feature_repository: FeatureRepository = InMemoryFeatureRepository()
event_repository: EventRepository = InMemoryEventRepository()
model_repository: ModelRepository = InMemoryModelRepository()

feature_service = FeatureService(feature_repository)
event_service = EventService(event_repository)
evaluation_service = EvaluationService(feature_repository, model_repository)
training_service = TrainingService(model_repository)
simulation_service = SimulationService(event_service)