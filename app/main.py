from fastapi import FastAPI
from app.database import engine, Base
from app.routers import products, connections, categories, product_types, events
from app.models import Product, Connection, Category, ProductType, EventSchedule
import logging



# ปิดการสร้างตารางอัตโนมัติเพื่อป้องกัน error
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="POS Jewelry & Connection API Service", 
              version="1.0.0")

# ลงทะเบียน Routers เข้ากับตัวแอป FastAPI
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(product_types.router, prefix="/product-types", tags=["Product Types"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(connections.router, prefix="/connections", tags=["Connections"])
app.include_router(events.router, prefix="/events", tags=["Event Schedules"])

@app.get("/")
def root():
    return {"status": "ok", "message": "POS Backend Service is running"}

# เพิ่ม endpoint สำหรับตรวจสอบการเชื่อมต่อฐานข้อมูล
@app.get("/health")
def health_check():
    try:
        # ทดสอบการเชื่อมต่อ
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}