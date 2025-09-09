from pydantic import BaseModel

class TodoRequestDTO(BaseModel):
    todo: str

    model_config = {
        "from_attributes": True
    }

