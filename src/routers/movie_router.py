
from typing import List
from fastapi import APIRouter, Body, Path, Query
from fastapi.responses import JSONResponse
from src.models.movie_model import Movie, movies

movie_router = APIRouter()

@movie_router.get("/", tags=['Movies'])
def get_movies() -> List[Movie]:
    return JSONResponse([movie.model_dump() for movie in movies])

@movie_router.get("/{movie_id}", tags=['Movies'])
def get_movie(movie_id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == movie_id:
            return JSONResponse(movie.model_dump(),200) 
    return JSONResponse({},status_code=404)

@movie_router.get("/titulo/",tags=['Movies'])
def get_movie_by_title(title: str = Query()):
    for movie in movies:
        if movie.title==title:
            content = movie.model_dump()
            return JSONResponse(content, status_code=200)
    return JSONResponse({},status_code=404)

@movie_router.post('/',tags=['Movies'])
def add_movie(movie: Movie) -> List[Movie]:
    movies.append(movie)
    return JSONResponse([movie.model_dump() for movie in movies])

@movie_router.put('/{id}',tags=['Movies'])
def update_movie(id:int, movie: Movie = Body()) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = movie.title
            movie['director'] = movie.director
    return JSONResponse([movie.model_dump() for movie in movies])

@movie_router.delete('/{id}',tags=['Movies'])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
    return movies