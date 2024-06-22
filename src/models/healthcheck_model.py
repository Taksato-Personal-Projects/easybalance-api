from pydantic import BaseModel


class HealthCheckModel(BaseModel):
    message: str