import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from .core.infra.tools import register_infra
from .infra import infra_list

async def serve():
    await asyncio.gather(*(register_infra(infra) for infra in infra_list))

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # или укажи список доменов
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        try:
            while True:
                data = await websocket.receive_text()

                await websocket.send({'msg': f'success - {data}'})
        except WebSocketDisconnect:
            print("WebSocket disconnected")

    @app.get("/")
    async def root():
        return {"message": "Hello from FastAPI!"}

    return app