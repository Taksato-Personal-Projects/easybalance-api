from pydantic import BaseModel


class UserProfileMode(BaseModel):
    name: str
    picture: str