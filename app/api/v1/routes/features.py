from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.dependencies import feature_service
from app.schemas.feature import FeatureCreate, FeatureResponse

router = APIRouter(prefix="/features", tags=["features"])


@router.post("", response_model=FeatureResponse, status_code=status.HTTP_201_CREATED)
def create(request: FeatureCreate):
    try:
        return feature_service.create_feature(
            name=request.name,
            key=request.key,
            description=request.description,
            enabled=request.enabled,
            rollout_percentage=request.rollout_percentage,
            ml_enabled=request.ml_enabled,
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{feature_id}", response_model=FeatureResponse)
def retrieve(feature_id: UUID):
    try:
        return feature_service.get_feature_by_id(feature_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{feature_id}", response_model=FeatureResponse)
def update(feature_id: str, feature: FeatureCreate):
    try:
        return feature_service.update_feature(feature_id, feature)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{feature_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(feature_id: str):
    try:
        feature_service.delete_feature(feature_id)
        return {}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("", response_model=list[FeatureResponse])
def list():
    try:
        return feature_service.list_features()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))