from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.main import api_router

app = FastAPI(
    title="ToyNeuralNetwork",
    description="This is a sample FastAPI application.",
    version="1.0.0",
)

app.mount("/", StaticFiles(directory="app/static", html = True), name="static")

app.include_router(api_router)
