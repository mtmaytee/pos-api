# app/schemas/product_type.py
from pydantic import BaseModel

class ProductTypeBase(BaseModel):
    type_id: str
    type_name: str

class ProductTypeCreate(ProductTypeBase):
    pass

class ProductTypeResponse(ProductTypeBase):
    class Config:
        from_attributes = True