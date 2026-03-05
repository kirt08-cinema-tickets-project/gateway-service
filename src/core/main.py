import grpc
import time

from kirt08_exceptions.exceptions import GrpcToHttp

from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Request,
    Response,
)
from fastapi.responses import JSONResponse

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from src.apps import router as apps_router

from src.core.service import service_ping
from src.core.schemas import HealthResponse
from src.core.prometheus_metrics import (
    REQUEST_COUNT,
    REQUEST_DURATION,
    REQUEST_IN_FLIGHT,
)


app = FastAPI()
app.include_router(apps_router)

@app.exception_handler(grpc.aio.AioRpcError)
async def grpc_exception_handler(request: Request, exc: grpc.aio.AioRpcError):
    http_status = GrpcToHttp[exc.code().name].value
    return JSONResponse(
        status_code = http_status,
        content = {"details": exc.details()}
    )

@app.middleware("http")
async def prometheus_metrics(request: Request, call_next):
    service_name = "gateway-service"
    method_name = request.method
    endpoint_path = request.url.path

    REQUEST_IN_FLIGHT.labels(service_name).inc()

    start = time.perf_counter()
    response: Response = await call_next(request)
    process_time = time.perf_counter() - start

    status_code = response.status_code

    REQUEST_COUNT.labels(
        service_name,
        method_name,
        endpoint_path,
        status_code
    ).inc()

    REQUEST_DURATION.labels(
        service_name,
        method_name,
        endpoint_path,
        status_code
    ).observe(process_time)

    REQUEST_IN_FLIGHT.labels(service_name).dec()

    return response

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

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
    
