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

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """ดึงข้อมูลสินค้าตาม ID"""
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_in: ProductCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """แก้ไขข้อมูลสินค้าตาม ID"""
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    for key, value in product_in.model_dump().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """ลบสินค้าตาม ID"""
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return db_product

@router.get("/search", response_model=List[ProductResponse])
def search_products(keyword: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """ค้นหาสินค้าตามคำค้น"""
    return db.query(Product).filter(Product.product_name.ilike(f"%{keyword}%")).all()