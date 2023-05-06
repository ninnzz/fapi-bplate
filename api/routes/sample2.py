"""Sample route 2."""
# from typing import Optional
from fastapi import APIRouter, Depends

# from api.config import get_config

router = APIRouter(
    prefix="/sample2",
    tags=["items"],
    dependencies=[Depends()],
    responses={404: {"description": "Not found"}},
)
