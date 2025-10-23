from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.health_router import router as health_router
from api.validation_router import router as validation_router
from starlette.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=FileResponse)
async def read_root():
    return "ml101.html"

app.include_router(health_router)
app.include_router(validation_router)
