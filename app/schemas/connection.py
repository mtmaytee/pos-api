# app/schemas/connection.py
from pydantic import BaseModel
from typing import Optional

class ConnectionBase(BaseModel):
    contact_name: str
    phone_number: str
    province_name: str
    location_name: Optional[str] = None
    booking_conditions: Optional[str] = None

class ConnectionCreate(ConnectionBase):
    pass

class ConnectionResponse(ConnectionBase):
    connection_id: int

    class Config:
        from_attributes = True