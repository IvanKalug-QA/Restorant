from fastapi import FastAPI
from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import main_router
from app.core.config import settings


app = FastAPI()
add_pagination(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.main_host,],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)
