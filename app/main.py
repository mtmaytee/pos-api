from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import products, connections, categories, product_types, events
from app.models import Product, Connection, Category, ProductType, EventSchedule
import logging
from src.config import Config

print("Database URL:", Config.DATABASE_URL)
print("Secret Key:", Config.SECRET_KEY)
print("JWT Secret Key:", Config.JWT_SECRET_KEY)


# ปิดการสร้างตารางอัตโนมัติเพื่อป้องกัน error
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="POS Jewelry & Connection API Service", 
              version="1.0.0")

# กำหนด Origin ที่อนุญาตให้เข้าถึง API
origins = [
    "http://localhost:5173",  # สำหรับ Vue Vite Dev Server
    "http://127.0.0.1:5173",
    # หากมี Domain หน้า Production จริง ให้ใส่เพิ่มตรงนี้ เช่น "https://your-frontend.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # อนุญาตทุก Method (รวมถึง OPTIONS, GET, POST, PUT, DELETE)
    allow_headers=["*"],  # อนุญาตทุก Header (รวมถึง Authorization Bearer token)
)

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