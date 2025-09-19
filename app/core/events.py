from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.container import container

database = container.database()

@asynccontextmanager
async def lifespan(app: FastAPI):
    #await database.create_tables()
    yield