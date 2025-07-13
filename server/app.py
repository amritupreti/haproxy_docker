import os
from fastapi import FastAPI, APIRouter

server_name = os.getenv("SERVER_NAME", "default_server")

router = APIRouter()
@router.get("/")
async def home():
    return f"{server_name}: Home page!"

@router.get("/admin")
async def admin():
    return f"{server_name}: Admin page!"

@router.get("/lightwork")
async def admin():
    return f"{server_name}: Doing light work!"

@router.get("/heavywork")
async def heavywork():
    return f"{server_name}: Doing heavy work!"

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app

app = create_app()
