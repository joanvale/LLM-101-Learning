from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from app.core.config import settings

API_KEY = "secretkey"
api_key_header = APIKeyHeader(name="API_KEY", auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return api_key
