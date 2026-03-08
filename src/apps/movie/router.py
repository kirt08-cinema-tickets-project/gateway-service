from typing import Annotated

from fastapi import APIRouter, Query, Depends

from src.apps.shared.service import authorized

from src.apps.grpc_clients import movie_client

from src.apps.movie.shemas import ListMoviesRequest

from google.protobuf.json_format import MessageToDict

router = APIRouter()


@router.get("/")
async def get_movie(dto: Annotated[ListMoviesRequest, Query()]):
    grpc_response = await movie_client.ListMovies(dto.category, dto.random, dto.limit)
    return MessageToDict(grpc_response)