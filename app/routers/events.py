# app/routers/events.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.event import EventSchedule
# เปลี่ยนการ Import จาก EventScheduleCreate -> EventCreate ให้ตรงกับ schemas
from app.schemas import EventCreate, EventResponse
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[EventResponse])
def get_events(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(EventSchedule).all()

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_event = EventSchedule(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_event = db.query(EventSchedule).filter(EventSchedule.event_id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event: EventCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_event = db.query(EventSchedule).filter(EventSchedule.event_id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event.model_dump().items():
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.delete("/{event_id}", response_model=EventResponse)
def delete_event(event_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_event = db.query(EventSchedule).filter(EventSchedule.event_id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return db_event

@router.get("/search", response_model=List[EventResponse])
def search_events(keyword: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(EventSchedule).filter(EventSchedule.event_name.ilike(f"%{keyword}%")).all()