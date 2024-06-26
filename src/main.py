from fastapi import FastAPI, status
from models.healthcheck_model import HealthCheckModel
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from middlewares.cors import cors_args
from middlewares.auth import is_authenticated
from api.v1.api import api_router

# Create FastAPI App
app = FastAPI(title="EasyBalance API", version="1.0.0")

# Middlewares
app.add_middleware(CORSMiddleware, **cors_args)
app.add_middleware(BaseHTTPMiddleware, dispatch=is_authenticated)


# Include endpoints
app.include_router(api_router, prefix="/api/v1")


# Health check
@app.get("/", status_code=status.HTTP_200_OK, response_model=HealthCheckModel)
async def health_check():
    return {"message": "OK"}