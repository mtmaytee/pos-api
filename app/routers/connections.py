from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.connection import Connection
from app.schemas.connection import ConnectionCreate, ConnectionResponse
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/connections", tags=["Connections"])

@router.get("/", response_model=List[ConnectionResponse])
def get_connections(province: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """ค้นหารายชื่อคอนเนกชัน (กรองตามจังหวัดได้)"""
    query = db.query(Connection)
    if province:
        query = query.filter(Connection.province_name == province)
    return query.all()

@router.post("/", response_model=ConnectionResponse, status_code=status.HTTP_201_CREATED)
def create_connection(conn_in: ConnectionCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """บันทึกคอนเนกชันใหม่"""
    db_conn = Connection(**conn_in.model_dump())
    db.add(db_conn)
    db.commit()
    db.refresh(db_conn)
    return db_conn