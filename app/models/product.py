# app/models/product.py
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "m_product"

    product_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sku = Column(String(50), unique=True, index=True, nullable=False)
    product_name = Column(String(200), nullable=False)
    
    # Foreign Keys
    category_id = Column(String(10), ForeignKey("m_category.category_id"), nullable=True)
    type_id = Column(String(10), ForeignKey("m_product_type.type_id"), nullable=True)
    
    cost_price = Column(Numeric(10, 2), default=0.0)
    selling_price = Column(Numeric(10, 2), default=0.0)
    stock_qty = Column(Integer, default=0)

    # Relationships เชื่อมไปยัง Category และ ProductType
    category = relationship("Category", back_populates="products")
    product_type = relationship("ProductType", back_populates="products")