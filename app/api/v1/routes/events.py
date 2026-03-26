from fastapi import APIRouter, HTTPException, status

from app.dependencies import event_service
from app.schemas.event import EventCreate, EventResponse

router = APIRouter(prefix="/events", tags=["events"])


@router.post("", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create(event: EventCreate):
    try:
        return event_service.create_event(
            user_id=event.user_id,
            feature_key=event.feature_key,
            event_type=event.event_type,
            timestamp=event.timestamp,
            properties=event.properties,
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{event_id}", response_model=EventResponse)
def retrieve(event_id: str):
    try:
        return event_service.get_event_by_id(event_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{event_id}", response_model=EventResponse)
def update(event_id: str, event: EventCreate):
    try:
        return event_service.update_event(event_id, event)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(event_id: str):
    try:
        event_service.delete_event(event_id)
        return {}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("", response_model=list[EventResponse])
def list():
    try:
        return event_service.list_events()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))