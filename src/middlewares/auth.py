from services.google.auth.google_oauth import validate_token
from fastapi import Request, status
from fastapi.responses import JSONResponse


async def is_authenticated(request: Request, call_next):
    token = request.headers.get("Authorization")

    validated = await validate_token(token)

    if (validated):
        response = await call_next(request)
        return response
    
    return JSONResponse(content={"message": "invalid token"}, status_code=status.HTTP_401_UNAUTHORIZED)


