from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .endpoints import flashcards

app = FastAPI()

app.include_router(flashcards.router)

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    error_message = "An error occurred while processing your request"
    if isinstance(exc, HTTPException):
        error_message = exc.detail
    return JSONResponse(status_code=500, content={"message": error_message})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
