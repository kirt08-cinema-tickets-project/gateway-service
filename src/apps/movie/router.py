from typing import Annotated

from fastapi import APIRouter, Query, Depends

from src.apps.shared.service import authorized

from src.apps.grpc_clients import movie_client

from src.apps.movie.shemas import ListMoviesRequest

from google.protobuf.json_format import MessageToDict

router = APIRouter()


@router.get("/",
            summary="Returns a list of movies based on the provided filtering options.")
async def get_movie(dto: Annotated[ListMoviesRequest, Query()]) -> list[dict]:
    grpc_response = await movie_client.ListMovies(dto.category, dto.random, dto.limit)

    # it should be such type
    # {'movies': [{}, {}, {}]} -> we just convert it into list of movies wothous parent 'movies'
    res = MessageToDict(grpc_response) 
    return res["movies"]


@router.get("/{slug}",
            summary="Returns detailed information about a movie by its slug.")
async def get_movie_by_slug(slug: str):
    grpc_response = await movie_client.GetMovie(slug = slug)
    return MessageToDict(grpc_response)
