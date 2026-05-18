from fastapi import FastAPI, Depends
from database import get_data

from services import WeatherFilters
app = FastAPI()


@app.get("/api/v1/weather")
def weather(filters: WeatherFilters = Depends()):
    data = get_data(
        town_id=filters.town_id,
        date_from=filters.date_from,
        date_to=filters.date_to,
        weather_main=filters.weather_main,
        temp_from=filters.temp_from,
        temp_to=filters.temp_to,
        pressure_from=filters.pressure_from,
        pressure_to=filters.pressure_to,
        humidity_from=filters.humidity_from,
        humidity_to=filters.humidity_to,
        wind_speed_from=filters.wind_speed_from,
        wind_speed_to=filters.wind_speed_to,
        clouds_from=filters.clouds_from,
        clouds_to=filters.clouds_to,
        limit=filters.limit,
        offset=filters.offset,
    )

    return {
        "success": True,
        "data": data
    }