from fastapi import APIRouter, HTTPException, status

from app.dependencies import training_service
from app.schemas.model import TrainResponse, ModelStatusResponse

router = APIRouter(tags=["model"])


@router.post("/train", response_model=TrainResponse)
def train():
    try:
        return training_service.train()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/model/status", response_model=ModelStatusResponse)
def status():
    try:
        return training_service.get_status()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))