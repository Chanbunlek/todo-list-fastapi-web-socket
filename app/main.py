from fastapi import FastAPI
from app.todo.api.todo import todo
from app.config.cors import set_cors
from app.config.exception_handler import register_exception_handler
from app.web_socket.api import ws

app = FastAPI(docs_url = "/api/swagger")

app.include_router(todo, prefix="/api")
app.include_router(ws, prefix="/api")

set_cors(app)
register_exception_handler(app)
