from google.oauth2 import id_token
from google.auth.transport import requests
from core.env_variables import client_id


async def decode_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)

        return idinfo
    except ValueError:
        print("Invalid token:", ValueError)
        return False
    

async def validate_token(token) -> bool:
    decoded = await decode_token(token)
    return True if decoded else False