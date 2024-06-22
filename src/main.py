from fastapi import FastAPI
from models.healthcheck_model import HealthCheckModel
from api.v1.api import api_router

# Create FastAPI App
app = FastAPI(title="EasyBalance API", version="1.0.0")

# Health check
@app.get("/", response_model=HealthCheckModel, tags=["HealthCheck"])
async def health_check():
    return {"message": "OK"}

# Include endpoints
app.include_router(api_router, prefix="/api/v1")