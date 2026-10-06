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