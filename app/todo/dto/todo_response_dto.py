from pydantic import BaseModel, Field
from datetime import datetime

class TodoResponseDTO(BaseModel):
    id: int
    todo: str
    is_completed: bool = Field(..., alias="isCompleted")
    create_date: datetime = Field(..., alias="createdDate")

    model_config = {
        "from_attributes": True,
        "populate_by_name": True
    }
