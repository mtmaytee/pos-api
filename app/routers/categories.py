from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Category
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse
from app.core.auth import get_current_user # Dependency ยืนยัน JWT Token

router = APIRouter()

@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(Category).all()

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_category = db.query(Category).filter(Category.category_id == category.category_id).first()
    if db_category:
        raise HTTPException(status_code=400, detail="Category ID already exists")
    new_category = Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category