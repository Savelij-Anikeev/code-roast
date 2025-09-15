import grpc

import generated.auth_pb2 as auth_pb2
import generated.auth_pb2_grpc as auth_pb2_grpc

class AuthService(auth_pb2_grpc.AuthServiceServicer):
    async def GetProfile(self, request, context):
        try:
            user = {
                "id": 1,
                "email": "email@email.email",
                "username": "username",
            }

            return auth_pb2.GetProfileResponse(
                id=user.id,
                email=user.email,
                username=user.username
            )
        except ValueError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))