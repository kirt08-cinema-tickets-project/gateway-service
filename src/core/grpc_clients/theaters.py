import grpc
from google.protobuf.empty_pb2 import Empty

from kirt08_contracts.theater import theater_pb2_grpc, theater_pb2


class TheaterClient:
    def __init__(self, host: str):
        self._channel = grpc.aio.insecure_channel(host)
        self._stub = theater_pb2_grpc.TheaterServiceStub(self._channel)

    async def GetListTheaters(self):
        response = await self._stub.ListTheaters(Empty())
        return response
    
    async def GetTheater(self, id: str):
        request = theater_pb2.GetTheaterRequest(id = id)
        response = await self._stub.GetTheater(request)
        return response
    
    async def CreateTheater(self, name: str, address: str):
        request = theater_pb2.CreateTheaterRequest(
            name = name,
            address = address
        )
        response = await self._stub.CreateTheater(request)
        return response