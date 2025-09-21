import os
import logging
from dotenv import load_dotenv

load_dotenv('.flaskenv')


class Config:
    DEBUG = os.getenv('DEBUG', True)
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = os.getenv('PORT', 5000)
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_FILE = 'app.log'

    DATE_FORMAT = '%Y-%m-%d'
