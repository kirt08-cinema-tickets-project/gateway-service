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
    