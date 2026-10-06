# app/schemas/event.py
from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class EventBase(BaseModel):
    event_title: str
    connection_id: int
    start_date: date
    end_date: date
    booking_status: str = "Pending"
    total_booth_fee: Decimal = Decimal('0.00')

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    event_id: int

    class Config:
        from_attributes = True