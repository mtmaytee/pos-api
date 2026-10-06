from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base

class ProductType(Base):
    __tablename__ = "m_product_type"
    type_id = Column(String(10), primary_key=True, index=True)
    type_name = Column(String(100), nullable=False)

    # Relationship to Product
    products = relationship("Product", back_populates="product_type")
    