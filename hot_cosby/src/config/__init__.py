import os

DB_URL = os.getenv('DB_URL')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 5432))
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_USER = os.getenv('MONGO_USER', 'cosby')
MONGO_PASS = os.getenv('MONGO_PASS')

if DB_URL is None:
    DB_URL = f'postgresql+pg8000://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}'
