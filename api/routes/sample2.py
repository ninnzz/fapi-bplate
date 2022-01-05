"""Sample route 2."""
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from api.config import get_config

router = APIRouter(
    prefix="/sample2",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
