from pydantic import BaseModel
from typing import List

class WeatherDataCreate(BaseModel):
    user_id: str
    city_ids: List[int]

class WeatherDataResponse(BaseModel):
    user_id: str
    datetime: str
    data: List[dict]
