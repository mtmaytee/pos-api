# app/models/connection.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Connection(Base):
    __tablename__ = "m_connection"

    connection_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contact_name = Column(String(150), nullable=False)  # เช่น พี่นก, คุณสมชาย
    phone_number = Column(String(20), nullable=False)
    province_name = Column(String(100), nullable=False, index=True)  # เช่น เชียงใหม่, ขอนแก่น
    location_name = Column(String(200), nullable=True)
    booking_conditions = Column(Text, nullable=True)

    # เชื่อม Relationship ไปหา EventSchedule
    events = relationship("EventSchedule", back_populates="connection", cascade="all, delete-orphan")