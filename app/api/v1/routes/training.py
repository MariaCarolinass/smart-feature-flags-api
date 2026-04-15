from fastapi import APIRouter, HTTPException, status

from app.core.exceptions import AppError, to_http_exception
from app.core.logging import get_logger
from app.dependencies import training_service
from app.schemas.model import TrainResponse, ModelStatusResponse

router = APIRouter(tags=["model"])
logger = get_logger(__name__)


@router.post("/train", response_model=TrainResponse)
def train():
    try:
        return training_service.train()
    except AppError as e:
        raise to_http_exception(e)
    except Exception as e:
        logger.exception("Erro ao treinar modelo")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

@router.get("/model/status", response_model=ModelStatusResponse)
def status():
    try:
        return training_service.get_status()
    except AppError as e:
        raise to_http_exception(e)
    except Exception as e:
        logger.exception("Erro ao obter status do modelo")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")