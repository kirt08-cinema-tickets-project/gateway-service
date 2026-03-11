import grpc
from google.protobuf.empty_pb2 import Empty

from kirt08_contracts.category import category_pb2_grpc, category_pb2


class CategoryClient:
    def __init__(self, host: str):
        self._channel = grpc.aio.insecure_channel(host)
        self._stub = category_pb2_grpc.CategoryServiceStub(self._channel)

    async def GetAllCategories(self):
        response = await self._stub.GetAllCategories(Empty())
        return response