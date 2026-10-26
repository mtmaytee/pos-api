from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import ProductType
from app.schemas import ProductTypeCreate, ProductTypeResponse
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[ProductTypeResponse])
def get_product_types(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(ProductType).all()

@router.post("/", response_model=ProductTypeResponse)
def create_product_type(item: ProductTypeCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    db_item = ProductType(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/{product_type_id}", response_model=ProductTypeResponse)
def get_product_type(product_type_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    db_item = db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Product type not found")
    return db_item

@router.put("/{product_type_id}", response_model=ProductTypeResponse)
def update_product_type(product_type_id: int, item: ProductTypeCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    db_item = db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Product type not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{product_type_id}", response_model=ProductTypeResponse)
def delete_product_type(product_type_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    db_item = db.query(ProductType).filter(ProductType.product_type_id == product_type_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Product type not found")
    db.delete(db_item)
    db.commit()
    return db_item

@router.get("/search", response_model=List[ProductTypeResponse])
def search_product_types(keyword: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(ProductType).filter(ProductType.product_type_name.ilike(f"%{keyword}%")).all()

