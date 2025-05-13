from fastapi import FastAPI
from src.routers.movie_router import movie_router

app = FastAPI()

app.title = "FastAPI"
app.description = "This is a simple FastAPI application."
app.version = "1.0.0"

@app.get("/",tags=['Home'])
def home():
    return {"message": "Hello, World!"}

app.include_router( prefix='/movies', router=movie_router )