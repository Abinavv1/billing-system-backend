from fastapi import FastAPI

from app.core.settings import get_settings
from app.core.events import lifespan
from app.core.exceptions.handler import add_exception_handlers
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints import router as api_router

settings = get_settings()

app = FastAPI(
    title="Restaurant billing management system.",
    lifespan=lifespan
)

app.include_router(router=api_router)
add_exception_handlers(app=app)

origins = [
    "http://192.168.10.103:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)