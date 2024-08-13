import sys, os

sys.path.append(os.getcwd())

import logging

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.user import models
from src import models
from config import DB_CONNECT_STRING
import asyncio

engine = create_async_engine(url=DB_CONNECT_STRING, max_overflow=10, echo=True)
logging.info("Engine for database is initialized")
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
logging.info("async_session is created")


async def create_all_database():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)

# asyncio.run(create_all_database())
