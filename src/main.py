from contextlib import asynccontextmanager

from fastapi import FastAPI

app = FastAPI(lifespan=lifespan)
