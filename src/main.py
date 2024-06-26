from fastapi import Depends, FastAPI, status
from models.healthcheck_model import HealthCheckModel
from fastapi.middleware.cors import CORSMiddleware
from security.auth import is_authenticated
from middlewares.cors import cors_args
from api.v1.api import api_router

# Create FastAPI App
app = FastAPI(title="EasyBalance API", version="1.0.0")

# Middlewares
app.add_middleware(CORSMiddleware, **cors_args)

# Include endpoints
app.include_router(api_router, prefix="/api/v1", dependencies=[Depends(is_authenticated)])

# Health check
@app.get("/", status_code=status.HTTP_200_OK, response_model=HealthCheckModel, tags=["Health Check"])
async def health_check():
    return {"message": "OK"}