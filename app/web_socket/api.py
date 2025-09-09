from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.web_socket.service import connection_manager

ws = APIRouter(prefix="/web-socket", tags=["Socket"])

clients = []

@ws.websocket("/")
async def web_socket(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
