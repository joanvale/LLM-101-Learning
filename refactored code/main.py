from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
import uvicorn

from app.core.config import settings
from app.core.logger import logger
from app.api import health_router, validation_router
from app.core.handlers import (
    validation_exception_handler,
    generic_exception_handler
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize resources
    logger.info("🚀 Starting LLM 101 Lab Server")
    yield
    # Cleanup resources
    logger.info("🛑 Shutting down LLM 101 Lab Server")


# Initialize FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

# Include API routers
app.include_router(health_router.router)
app.include_router(validation_router.router)

# TODO: include all your APIRouters 

# Add exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# TODO: add any additional exception handlers here


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )
