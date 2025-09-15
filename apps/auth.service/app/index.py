import grpc
import asyncio

from grpc.server import AuthService
import generated.auth_pb2_grpc as auth_pb2_grpc

from app.config import config

async def serve():
    server = grpc.aio.server()

    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port(f'[::]:{config['port']}')

    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())