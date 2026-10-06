# app/schemas/category.py
from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    category_id: str
    category_name_th: str

class CategoryCreate(CategoryBase):
    pass

# เพิ่ม Class นี้เข้าไปครับ
class CategoryUpdate(BaseModel):
    category_name_th: Optional[str] = None

class CategoryResponse(CategoryBase):
    class Config:
        from_attributes = True