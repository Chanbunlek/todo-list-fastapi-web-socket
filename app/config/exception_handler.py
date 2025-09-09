from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from app.utils.response import Response

class ServiceException(Exception):
    def __init__(self, message: str, code: int = 400):
        self.message = message
        self.code = code

async def todo_exception_handler(request: Request, exc: ServiceException):
    return JSONResponse(
        status_code=exc.code,
        content=Response.failed(code=exc.code, message=exc.message).dict()
    )

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=Response.failed(code=500, message=str(exc)).dict()
    )

def register_exception_handler(app: FastAPI):
    app.add_exception_handler(ServiceException, todo_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
