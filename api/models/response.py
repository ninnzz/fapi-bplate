"""
All response schema should be added here.

Uses pydantic validation. See full info here:
https://pydantic-docs.helpmanual.io/usage/schema/
"""
from typing import Optional, List
from pydantic import BaseModel


class SampleResponse(BaseModel):
    name: str
    updated_info: Optional[str] = None
    age_in_five_years: int
    new_added_info: List[str]
