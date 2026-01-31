import logging
import grpc

from kirt08_contracts import auth_pb2, auth_pb2_grpc

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