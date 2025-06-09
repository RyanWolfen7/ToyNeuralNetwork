from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import api_router

app = FastAPI(
    title="ToyNeuralNetwork",
    description="This is a sample FastAPI application.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["127.0.0.1:54147", "127.0.0.1:3000"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="app/static", html = True), name="static")

app.include_router(api_router)
