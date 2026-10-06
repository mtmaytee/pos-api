# app/models/event.py
from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EventSchedule(Base):
    __tablename__ = "t_event_schedule"

    event_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    event_title = Column(String(200), nullable=False)
    connection_id = Column(Integer, ForeignKey("m_connection.connection_id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    booking_status = Column(String(20), default="Pending")
    total_booth_fee = Column(Numeric(10, 2), default=0.0)

    # ต้องมีบรรทัดนี้เพื่อรับคู่กับ back_populates="connection" ใน connection.py
    connection = relationship("Connection", back_populates="events")