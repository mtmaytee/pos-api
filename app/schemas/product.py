# app/schemas/product.py
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ProductBase(BaseModel):
    sku: str
    product_name: str
    category_id: Optional[str] = None
    type_id: Optional[str] = None
    lot_id: Optional[int] = None
    cost_price: Decimal = Decimal('0.00')
    selling_price: Decimal = Decimal('0.00')
    stock_qty: int = 0

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    product_id: int

    class Config:
        from_attributes = True