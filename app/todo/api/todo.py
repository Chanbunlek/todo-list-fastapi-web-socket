from fastapi import APIRouter
from app.db.models.todo import Todo
from app.db.session import session
from app.web_socket.service import connection_manager
from app.utils.response import Response
from app.todo.dto.todo_request_dto import TodoRequestDTO
from app.todo.dto.todo_response_dto import TodoResponseDTO
from app.config.exception_handler import ServiceException

todo = APIRouter(prefix="/todo", tags=["Todo"])

@todo.get("/", response_model=Response[list[TodoResponseDTO]])
async def get_all():
    db = session()
    todos = db.query(Todo).all()
    db.close()

    todo_dto = [TodoResponseDTO.from_orm(todo) for todo in todos]

    return Response.ok(data=todo_dto)

@todo.post("/", response_model=Response[TodoResponseDTO])
async def create_todo(dto: TodoRequestDTO):
    todo = Todo(todo = dto.todo)
    db = session()
    db.add(todo)
    db.commit()
    db.refresh(todo)
    db.close()

    await connection_manager.broadcast("change")
    
    return Response.ok(data=todo)

@todo.delete("/{id}", response_model=Response[str])
async def delete_todo(id: int):
    db = session()
    todo = db.query(Todo).filter(Todo.id == id).first()

    if not todo:
        raise ServiceException("Not found", 200)

    db.delete(todo)
    db.commit()
    db.close()

    await connection_manager.broadcast("change")

    return Response.ok(data = "Delete successfully!")

@todo.patch("/{id}", response_model=Response[TodoResponseDTO])
async def edit_todo(id: int, dto: TodoRequestDTO):
    db = session()
    todo = db.query(Todo).filter(Todo.id == id).first()
    
    if not todo:
        raise ServiceException("Not found", 200)
    
    todo.todo = dto.todo
    db.add(todo)
    db.commit()
    db.refresh(todo)
    db.close()

    await connection_manager.broadcast("change")

    return Response.ok(data = todo)

@todo.patch("/{id}/update-status", response_model=Response[TodoResponseDTO])
async def update_status(id: int, status: bool):
    db = session()
    todo = db.query(Todo).filter(Todo.id == id).first()
    
    if not todo:
        raise ServiceException("Not found", 200)
    
    todo.is_completed = status
    db.add(todo)
    db.commit()
    db.refresh(todo)
    db.close()

    await connection_manager.broadcast("change")

    return Response.ok(data=todo)
