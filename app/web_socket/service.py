from fastapi import WebSocket
from typing import List

class ConnectionManagement:
    def __init__(self):
        self.clients: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.clients.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        if websocket in self.clients:
            self.clients.remove(websocket)

    async def broadcast(self, message: str):
        disconnected_clients = []

        for client in self.clients:
            try:
                await client.send_text(message)
            except Exception:
                disconnected_clients.append(client)
        
        for client in disconnected_clients:
            self.disconnect(client)

connection_manager = ConnectionManagement()
