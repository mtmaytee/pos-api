# app/core/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import os

# ใช้ Secret Key และ Algorithm เดียวกับระบบ Central Login
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY environment variable is required")

ALGORITHM = "HS256"

# OAuth2 Scheme ดึง Token จาก Header Authorization: Bearer
# ใช้ URL ที่เหมาะสมสำหรับ production
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="https://login-register-vdar.onrender.com/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token ไม่ถูกต้อง หมดอายุ หรือไม่มีสิทธิ์เข้าถึง",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # ถอดรหัส Token จาก Central Auth Server
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        return user_id
    except JWTError:
        raise credentials_exception
