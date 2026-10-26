from fastapi import APIRouter, Depends, HTTPException, status
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


@router.get("/{connection_id}", response_model=ConnectionResponse)
def get_connection(connection_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """ดึงข้อมูลคอนเนกชันตาม ID"""
    db_conn = db.query(Connection).filter(Connection.connection_id == connection_id).first()
    if not db_conn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Connection not found")
    return db_conn

@router.put("/{connection_id}", response_model=ConnectionResponse)
def update_connection(connection_id: int, conn_in: ConnectionCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """อัปเดตข้อมูลคอนเนกชันตาม ID"""
    db_conn = db.query(Connection).filter(Connection.connection_id == connection_id).first()
    if not db_conn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Connection not found")
    for key, value in conn_in.model_dump().items():
        setattr(db_conn, key, value)
    db.commit()
    db.refresh(db_conn)
    return db_conn

@router.delete("/{connection_id}", response_model=ConnectionResponse)
def delete_connection(connection_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """ลบคอนเนกชันตาม ID"""
    db_conn = db.query(Connection).filter(Connection.connection_id == connection_id).first()
    if not db_conn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Connection not found")
    db.delete(db_conn)
    db.commit()
    return db_conn

@router.get("/search/", response_model=List[ConnectionResponse])
def search_connections(name: Optional[str] = None, province: Optional[str] = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """ค้นหาคอนเนกชันตามชื่อและจังหวัด"""
    query = db.query(Connection)
    if name:
        query = query.filter(Connection.connection_name.ilike(f"%{name}%"))
    if province:
        query = query.filter(Connection.province_name == province)
    return query.all()