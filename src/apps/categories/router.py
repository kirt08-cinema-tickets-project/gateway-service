from fastapi import APIRouter

from google.protobuf.json_format import MessageToDict

from src.apps.grpc_clients import category_client


router = APIRouter()

@router.get("/",
            summary="Get all categories")
async def get_all_categories():
    grpc_response = await category_client.GetAllCategories()
    return MessageToDict(grpc_response)