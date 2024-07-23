from fastapi import FastAPI
from .database import get_db
from .endpoints.weather_endpoint import router as main_router

def lifespan(app: FastAPI):
    get_db()
    yield

app = FastAPI(title='API - Test Devgrid Wheather', description='Weather ', version='0.1.1v', docs_url='/docs')

app.lifespan = lifespan(app)

app.include_router(main_router, prefix= '/devgrid', tags=['Devgrid Weather API'])

def create_app() -> FastAPI:
    return app