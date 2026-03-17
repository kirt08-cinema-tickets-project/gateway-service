import grpc
from kirt08_contracts.screening import screening_pb2, screening_pb2_grpc

from datetime import datetime


class ScreeningClient:
    def __init__(self, host: str):
        self._connection = grpc.aio.insecure_channel(host)
        self._stub = screening_pb2_grpc.ScreeningServiceStub(self._connection)

    async def CreateScreening(
            self,
            movie_id: str,
            hall_id: str,
            start_at: datetime,
            end_at: datetime
    ) -> screening_pb2.CreateScreeningResponse:
        request = screening_pb2.CreateScreeningRequest(
            movie_id = movie_id,
            hall_id = hall_id,
            start_at = str(start_at),
            end_at = str(end_at)
        )
        response: screening_pb2.CreateScreeningResponse = await self._stub.CreateScreening(request)
        return response
    

    async def GetScreenings(
            self,
            theater_id: str | None = None,
            date: datetime | None = None
    ) -> screening_pb2.GetScreeningsResponse:
        request = screening_pb2.GetScreeningsRequest(
            theater_id = theater_id if theater_id else None,
            date = str(date) if date else None
        )
        response: screening_pb2.GetScreeningsResponse = await self._stub.GetScreenings(request)
        return response
    
    
    async def GetScreening(
            self, 
            id: str
    ) -> screening_pb2.GetScreeningResponse:
        request = screening_pb2.GetScreeningRequest(id = id)
        response: screening_pb2.GetScreeningResponse = await self._stub.GetScreening(request)
        return response
    
    async def GetScreeningsByMovie(
            self,
            movie_id: str,
            date: datetime | None = None
    ) -> screening_pb2.GetScreeningsByMovieResponse:
        request = screening_pb2.GetScreeningsByMovieRequest(
            movie_id = movie_id,
            date = str(date) if date else None
        )
        response: screening_pb2.GetScreeningsByMovieResponse = await self._stub.GetScreeningsByMovie(request)
        return response