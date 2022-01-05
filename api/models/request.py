"""
All request schema should be added here.

Uses pydantic validation. See full info here:
https://pydantic-docs.helpmanual.io/usage/schema/
"""
from typing import Optional

from pydantic import BaseModel


class SampleRequest(BaseModel):
    name: str
    info: Optional[str] = None
    age: int
    weight: Optional[float] = None
