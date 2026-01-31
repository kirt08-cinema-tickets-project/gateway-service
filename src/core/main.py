from fastapi import FastAPI, HTTPException, status

from src.apps import router as apps_router

from src.core.service import service_ping
from src.core.schemas import HealthResponse


app = FastAPI()
app.include_router(apps_router)


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
    
