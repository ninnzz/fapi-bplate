"""Sample route."""
from typing import Optional
from fastapi import APIRouter, HTTPException
from api.config import get_config


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello")
async def hello(name: str):
    """
    Example of passing a query string in URL.

    :param name:
    :return:
    """
    return {"message": f"Hello {name}"}


@router.get("/hello_optional")
async def hello_optional(name: Optional[str] = None):
    """
    Example of passing an optional query string in URL.

    :param name:
    :return:
    """
    if name is not None:
        return {"message": f"Hello {name}"}
    else:
        return {"message": "name is an optional parameter"}


@router.get("/get_error/{error_code}")
async def sample_error(error_code: int, message: Optional[str] = None):
    """
    Example of throwing errors.

    :param error_code:
    :param message:
    :return:
    """
    if message is None:
        message = "No included message"
    if error_code != 0:
        raise HTTPException(status_code=error_code, detail=message)
    return {"message": "Hello World"}


@router.get("/token")
async def token():
    """
    Example access of config.

    :return:
    """
    config = get_config()
    return {"token": config.app_token}


#
# @app.post("/info")
# async def user_info(info: Dict):
#
