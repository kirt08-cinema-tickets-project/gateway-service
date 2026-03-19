from datetime import datetime
from typing import Annotated, Optional
from fastapi import APIRouter, Query, Path, Depends

from google.protobuf.json_format import MessageToDict

from src.apps.grpc_clients import screening_client

from src.apps.screening.schemas import GetScreeningsRequest, CreateScreeningRequest


router = APIRouter()


@router.post("/")
async def create_screening(data: CreateScreeningRequest):
    grpc_response = await screening_client.CreateScreening(
        movie_id = data.movie_id,
        hall_id = data.hall_id,
        start_at = data.start_at,
        end_at = data.end_at
    )
    return MessageToDict(grpc_response)


@router.get("/")
async def get_screenings(
    data: Annotated[GetScreeningsRequest, Depends()]
):
    grpc_response = await screening_client.GetScreenings(
        theater_id = data.theater_id,
        date = data.date
    )
    response = MessageToDict(grpc_response)
    return response.get("screenings")


@router.get("/{id}")
async def get_screening(id: Annotated[str, Path()]):
    grpc_response = await screening_client.GetScreening(id = id)
    return MessageToDict(grpc_response)


@router.get("/movie/{movie_id}")
async def get_by_movie(
    movie_id: Annotated[str, Path()],
    date: Optional[datetime] = Query(default=None)
):
    grpc_response = await screening_client.GetScreeningsByMovie(
        movie_id = movie_id,
        date = date
    )
    return MessageToDict(grpc_response)