from fastapi import FastAPI

from app.core.events import lifespan
from app.core.exceptions.handler import add_exception_handlers
from app.endpoints import router as api_router

app = FastAPI(
    title="Restaurant billing management system.",
    lifespan=lifespan
)

app.include_router(router=api_router)
add_exception_handlers(app=app)