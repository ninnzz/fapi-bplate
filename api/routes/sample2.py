"""Sample route 2."""
from typing import Optional
from fastapi import APIRouter
from api.config import get_config


from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/sample2",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)