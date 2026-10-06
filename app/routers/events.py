# app/routers/events.py
from fastapi import APIRouter, Depends
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