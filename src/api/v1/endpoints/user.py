from typing import Annotated
from fastapi import APIRouter, Header, HTTPException, status
from models.user_profile_model import UserProfileMode
from services.google.auth.google_oauth import decode_token


router = APIRouter()


@router.get("/profile", status_code=status.HTTP_200_OK, response_model=UserProfileMode)
async def get_user_profile_data(authorization: Annotated[str | None, Header()] = None):
    decoded = await decode_token(authorization)
    
    return {
        "name": decoded["given_name"],
        "picture": decoded["picture"]
    }