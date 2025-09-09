from typing import TypeVar, Dict, Any, Optional, Generic
from pydantic import BaseModel

T = TypeVar("T")

class Response(BaseModel, Generic[T]):
    code: int
    success: bool
    data: Optional[T]
    message: str = ""

    @staticmethod
    def ok(code = 200, data: T = None, message = ""):
        return Response(code=code, success=True, data=data, message=message)
    
    @staticmethod
    def failed(code = 400, data: T = [], message = ""):
        return Response(code=code, success=False, data=data, message=message)

