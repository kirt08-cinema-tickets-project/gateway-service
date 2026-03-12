from fastapi import APIRouter
from google.protobuf.json_format import MessageToDict

from src.apps.grpc_clients import theater_client

from src.apps.theaters.shemas import TheaterCreateRequest


router = APIRouter()

@router.get("/list")
async def get_list():
    grpc_response = await theater_client.GetListTheaters()
    res = MessageToDict(grpc_response) 
    return res["theaters"]

@router.get("/{id}")
async def get_one(id: str):
    grpc_response = await theater_client.GetTheater(id = id)
    return MessageToDict(grpc_response) 

@router.post("/")
async def create_theater(data: TheaterCreateRequest):
    grpc_response = await theater_client.CreateTheater(name = data.name, address = data.address)
    return MessageToDict(grpc_response) 