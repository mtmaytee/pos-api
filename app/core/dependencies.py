# app/core/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.config import Config
import os

# ใช้ Secret Key และ Algorithm เดียวกับระบบ Central Login
SECRET_KEY = Config.JWT_SECRET_KEY

if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY environment variable is required")

ALGORITHM = "HS256"

# กำหนด tokenUrl จาก environment variable หรือใช้ default
TOKEN_URL = os.environ.get('TOKEN_URL', 'http://localhost:8001/auth/login')

# OAuth2 Scheme ดึง Token จาก Header Authorization: Bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)
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


