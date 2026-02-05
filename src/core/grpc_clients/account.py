import grpc
from kirt08_contracts.account import account_pb2, account_pb2_grpc


class AccountClient:
    def __init__(self, host):
        self.channel = grpc.aio.insecure_channel(host)
        self.stub = account_pb2_grpc.AccountServiceStub(self.channel)

    async def get_account(self, user_id : int):
        request = account_pb2.GetAccountRequest(
            id = user_id
        )
        response = await self.stub.GetAccount(request)
        return response
    
    async def init_email_change(self, email: str, id: int):
        request = account_pb2.InitEmailChangeRequest(
            email = email,
            id = id,
        )
        response = await self.stub.InitEmailChange(request)
        return response
    
    async def confirm_email_change(self, email: str, code : str, id: int):
        request = account_pb2.ConfirmEmailChangeRequest(
            email = email,
            code = code,
            id = id,
        )
        response = await self.stub.ConfirmEmailChange(request)
        return response.ok
    
    async def init_phone_change(self, phone: str, id: int):
        request = account_pb2.InitPhoneChangeRequest(
            phone = phone,
            id = id,
        )
        response = await self.stub.InitPhoneChange(request)
        return response
    
    async def confirm_phone_change(self, phone: str, code : str, id: int):
        request = account_pb2.ConfirmPhoneChangeRequest(
            phone = phone,
            code = code,
            id = id,
        )
        response = await self.stub.ConfirmPhoneChange(request)
        return response.ok
    