import grpc
from google.protobuf.empty_pb2 import Empty

from kirt08_contracts.hall import hall_pb2_grpc, hall_pb2


class HallClient:
    def __init__(self, host: str):
        self._channel = grpc.aio.insecure_channel(host)
        self._stub = hall_pb2_grpc.HallServiceStub(self._channel)

    async def CreateHall(self, name: str, theater_id: str, layouts: list):
        request = hall_pb2.CreateHallRequest(
            name = name,
            theater_id = theater_id,
            layouts = layouts
        )
        response = await self._stub.CreateHall(request)
        return response
    
    async def GetHall(self, id: str):
        request = hall_pb2.GetHallRequest(id = id)
        response = await self._stub.GetHall(request)
        return response