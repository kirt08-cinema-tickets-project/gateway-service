import grpc

from kirt08_contracts.seats import seats_pb2_grpc, seats_pb2


class SeatsClient:
    def __init__(self, host: str):
        self._channel = grpc.aio.insecure_channel(host)
        self._stub = seats_pb2_grpc.SeatsServiceStub(self._channel)
        
    async def GetSeat(self, id: str):
        request = seats_pb2.GetSeatRequest(
            id = id
        )
        response = await self._stub.GetSeat(request)
        return response
    
    async def ListSeatsRequest(self, hall_id: str, screening_id: str):
        request = seats_pb2.ListSeatsRequest(
            hall_id = hall_id,
            screening_id = screening_id
        )
        response = await self._stub.ListSeatsByHall(request)
        return response