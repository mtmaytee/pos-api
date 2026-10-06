import os

class Config:
    # Database configuration
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Secret key for Flask applications
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # API keys
    API_KEY = os.environ.get('API_KEY')
    
    # JWT Configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM', 'HS256')

    # Other configurations

    # Application settings
    APP_NAME = os.environ.get('APP_NAME', 'MyApp')

# ตัวอย่างการใช้งาน
# from config import Config
# database_url = Config.DATABASE_URL