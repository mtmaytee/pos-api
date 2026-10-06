from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """ดึงรายการสินค้าทั้งหมด (ต้อง Login)"""
    return db.query(Product).all()

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """เพิ่มสินค้าใหม่เข้าสต็อก"""
    db_product = Product(**product_in.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product