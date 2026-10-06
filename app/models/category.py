from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "m_category"
    category_id = Column(String(10), primary_key=True, index=True)
    category_name_th = Column(String(100), nullable=False)

    # เชื่อมย้อนกลับไปหา Product
    products = relationship("Product", back_populates="category")