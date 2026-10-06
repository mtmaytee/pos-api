# ใช้ Python 3.10 Slim Image
FROM python:3.10-slim

# ตั้งค่า Working Directory ใน Container
WORKDIR /app

# ป้องกันไม่ให้ Python สร้างไฟล์ .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ติดตั้ง Dependencies สำหรับ PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# ก๊อปปี้ไฟล์ requirements.txt และติดตั้ง Packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ก๊อปปี้โค้ดทั้งหมดในโปรเจกต์เข้าไปใน Container
COPY . .

# เปิด Port 8000
EXPOSE 8000

# คำสั่งรัน FastAPI ผ่าน Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]