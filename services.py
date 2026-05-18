from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum

class WeatherMain(str, Enum):
    Snow = "Snow"
    Clear = "Clear"
    Clouds = "Clouds"
    Rain = "Rain"
    Thunderstorm = "Thunderstorm"
    Drizzle = "Drizzle"
    Fog = "Fog"
    Mist = "Mist"
    Smoke = "Smoke"
    Dust = "Dust"
    Haze = "Haze"

class WeatherFilters(BaseModel):
    town_id: Optional[int] = Field(default=None, gt=0)

    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None

    weather_main: Optional[WeatherMain] = None

    temp_from: Optional[float] = None
    temp_to: Optional[float] = None

    pressure_from: Optional[float] = None
    pressure_to: Optional[float] = None

    humidity_from: Optional[int] = None
    humidity_to: Optional[int] = None

    wind_speed_from: Optional[float] = None
    wind_speed_to: Optional[float] = None

    clouds_from: Optional[int] = None
    clouds_to: Optional[int] = None

    limit: int = Field(default=100, gt=0)
    offset: int = Field(default=0, ge=0)