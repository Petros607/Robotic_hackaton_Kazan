# данный скрипт вытягивает все чувствительные данные из .env и подставляет туда, где это необходимо

import os
from dotenv import load_dotenv

load_dotenv(override=True)


DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

DB_CONNECT_STRING = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
