import grpc
from kirt08_contracts.users import users_pb2, users_pb2_grpc


class UsersClient:
    def __init__(self, host: str):
        self.channel = grpc.aio.insecure_channel(host)
        self.stub = users_pb2_grpc.UsersServiceStub(self.channel)

    async def get_me(self, id: str):
        request = users_pb2.GetMeRequest(
            id = id
        )
        response = await self.stub.GetMe(request)
        return response
    
    async def patch_me(self, id: str, name: str | None = None): # avatar: str | None = None
        request = users_pb2.PatchUserRequest(
            user_id = id,
            name = name,
        )
        response = await self.stub.PatchUser(request)
        return response