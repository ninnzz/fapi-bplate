"""
All response schema should be added here.

Uses pydantic validation. See full info here:
https://pydantic-docs.helpmanual.io/usage/schema/
"""
from typing import List, Optional

from pydantic import BaseModel


class SampleResponse(BaseModel):
    """Response model."""

    name: str
    updated_info: Optional[str] = None
    age_in_five_years: int
    new_added_info: List[str]
