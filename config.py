import os
import logging
from dotenv import load_dotenv

load_dotenv('.flaskenv')


class Config:
    DEBUG = os.getenv('DEBUG', True)
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = os.getenv('PORT', 5000)
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_FILE = 'app.log'
    BENCHMARK_RECORD_TABLE = os.getenv('BENCHMARK_RECORD_TABLE', 'BenchmarkRecord')
    CACHE_RANGE_TABLE = os.getenv('CACHE_RANGE_TABLE', 'CacheRange')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///Database.db')
    API_VERSION = "1.0.0"
    DATE_FORMAT = '%Y-%m-%d'
