from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse

from .base import AppException

def add_exception_handlers(app: FastAPI):
    """
        Add exception handlers to app.
    """
    async def handle_app_exception(request: Request,exc: AppException):
        """
            Handler `AppException` instances.
        """
        return JSONResponse(
            status_code=exc.status,
            content={'message':exc.message}
        )
    
    app.add_exception_handler(AppException,handle_app_exception)