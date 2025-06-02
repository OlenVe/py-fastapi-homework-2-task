from typing import List

from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from pydantic_extra_types.country import CountryAlpha2


class BaseMovieSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    date: date
    score: float = Field(..., ge=0, le=100)
    overview: str
    status: str
    budget: float = Field(..., ge=0)
    revenue: float = Field(..., ge=0)
    country: CountryAlpha2 = Field(
        ...,
        description="ISO 3166-1 alpha-2"
    )
    genre: List[str]
    actors: List[str]
    language: List[str]


class MovieCreateSchema(BaseMovieSchema):
    pass


class MovieCreateResponseSchema(BaseMovieSchema):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True


