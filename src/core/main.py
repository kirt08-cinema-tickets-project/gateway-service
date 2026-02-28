import grpc
from kirt08_exceptions.exceptions import GrpcToHttp

from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Request,
)
from fastapi.responses import JSONResponse

from src.apps import router as apps_router

from src.core.service import service_ping
from src.core.schemas import HealthResponse


app = FastAPI()
app.include_router(apps_router)

@app.exception_handler(grpc.aio.AioRpcError)
async def grpc_exception_handler(request: Request, exc: grpc.aio.AioRpcError):
    http_status = GrpcToHttp[exc.code().name].value
    return JSONResponse(
        status_code = http_status,
        content = {"details": exc.details()}
    )


@app.get("/ping",
            summary="Health check", 
            description="Checks if the Gateway is running", 
            response_model=HealthResponse
)
async def ping():
    try:
        res = await service_ping()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error: {str(e)}"
        )
    return res
    
