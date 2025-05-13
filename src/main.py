from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler

app = FastAPI()

#app.add_middleware(HTTPErrorHandler)
@app.middleware('http')
async def http_error_handler(request: Request, call_next) -> Response | JSONResponse:
    try:
        print('RUNNING')
        return await call_next(request)
    except Exception as e:
        content = f"exc: {str(e)}"
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=content,status_code=status_code)


app.title = "FastAPI"
app.description = "This is a simple FastAPI application."
app.version = "1.0.0"

@app.get("/",tags=['Home'])
def home():
    return {"message": "Hello, World!"}

app.include_router( prefix='/movies', router=movie_router )