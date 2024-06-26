from typing import Annotated
from services.google.auth.google_oauth import validate_token
from fastapi import Header, HTTPException, status


async def is_authenticated(authorization: Annotated[str | None, Header()] = None):
    validated = await validate_token(authorization)

    if (not validated):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
