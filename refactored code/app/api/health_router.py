
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/", summary="Health Check")
async def health_check():
    return {
        "status": "OK",
        "message": "LLM101 API is up and running.",
        "timestamp": datetime.utcnow().isoformat()
    }
