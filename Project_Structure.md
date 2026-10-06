# POS FastAPI Project Structure

## 📁 Directory Structure

```text
pos_fastapi/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point สำหรับรัน FastAPI
│   ├── config.py               # จัดการ Environment Variables & Secret Keys
│   ├── database.py             # ตั้งค่าการเชื่อมต่อ Database (SQLAlchemy)
│   │
│   ├── core/                   # ระบบหลักและ Security
│   │   ├── security.py         # ฟังก์ชัน Hash Password / JWT Token
│   │   └── dependencies.py     # OAuth2 Verification & get_current_user
│   │
│   ├── models/                 # Database Models (ORM - SQLAlchemy)
│   │   ├── user.py             # ตารางผู้ใช้งาน / ระบบ Login
│   │   ├── product.py          # หมวดหมู่, ลายสินค้า (เบนซ์, พิกุล), สินค้า Master
│   │   ├── connection.py       # คอนเนกชันผู้ติดต่อตามจังหวัด
│   │   └── event.py            # ปฏิทินจองงาน / ออกบูธ
│   │
│   ├── schemas/                # Data Validation (Pydantic Models)
│   │   ├── auth.py             # Schema สำหรับ Login
│   │   ├── product.py          # Schema สำหรับ Request/Response สินค้า
│   │   ├── connection.py       # Schema สำหรับข้อมูลคอนเนกชัน
│   │   └── event.py            # Schema สำหรับตารางงาน
│   │
│   └── routers/                # API Endpoints
│       ├── auth.py             # API Login & Check Status
│       ├── products.py         # API จัดการสต็อกสินค้า
│       ├── connections.py      # API ค้นหาและบันทึกคอนเนกชัน
│       └── events.py           # API จัดการปฏิทินงาน
│
├── .env                        # ค่า Config ความลับ เช่น SECRET_KEY, DATABASE_URL
├── .gitignore
├── Project_Structure.md        # เอกสารอธิบายโครงสร้างโปรเจกต์
└── requirements.txt            # รายการ Dependencies (fastapi, uvicorn, sqlalchemy, ฯลฯ)
```
