import grpc
from google.protobuf.empty_pb2 import Empty

from kirt08_contracts.auth import auth_pb2, auth_pb2_grpc

class AuthClient:
    def __init__(self, host : str):
        self.channel = grpc.aio.insecure_channel(host)
        self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)

    async def send_otp(self, identifier : str, type_ : str):
        request = auth_pb2.SendOtpRequest(
            identifier = identifier,
            type = type_,
        )
        response = await self.stub.SendOtp(request)
        return response
    
    async def verify_otp(self, identifier: str, type_: str, code: str):
        request = auth_pb2.VerifyOtpRequest(
            identifier = identifier,
            type = type_,
            code = code,
        )
        response = await self.stub.VerifyOtp(request)
        return response
    
    async def refresh(self, refresh_token : str):
        request = auth_pb2.RefreshRequest(
            refresh_token = refresh_token
        )
        response = await self.stub.Refresh(request)
        return response
    
    async def telegram_init(self):
        response = await self.stub.TelegramInit(Empty())
        return response
    
    async def telegram_verify(self, query: dict[str, str]):
        request = auth_pb2.TelegrmaVerifyRequest(query = query)
        response = await self.stub.TelegramVerify(request)
        return response