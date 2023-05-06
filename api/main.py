"""
Main function.

Includes all the router and middleware loading
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.config import get_config
from api.routes import sample

app = FastAPI()

# Get instance of settings
config = get_config()


# Setup cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_allow_origin.split(","),
    allow_credentials=config.cors_allow_credentials,
    allow_methods=config.cors_allow_methods.split(","),
    allow_headers=config.cors_allow_headers.split(","),
)

# Add all router
app.include_router(sample.router)


# Add general error handler
@app.exception_handler(Exception)
async def unicorn_exception_handler(_: Request, exc: Exception):
    """Exception handler."""
    return JSONResponse(
        status_code=500,
        content={
            "message": "Uh-oh, our gears are broken. Please contact admin.",
            "title": "Internal error occurred.",
            "details": str(exc),
        },
    )
