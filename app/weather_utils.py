import aiohttp
import asyncio
from datetime import datetime
from .models import WeatherData
from sqlalchemy.orm import Session

import os

OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

async def fetch_weather(session, city_id):
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={OPEN_WEATHER_API_KEY}&units=metric"
    async with session.get(url) as response:
        return await response.json()

async def collect_weather_data(user_id: str, city_ids: list, session: Session):
    async with aiohttp.ClientSession() as http_session:
        for i in range(0, len(city_ids), 60):
            chunk = city_ids[i:i + 60]
            tasks = [fetch_weather(http_session, city_id) for city_id in chunk]
            responses = await asyncio.gather(*tasks)
            
            for response in responses:
                weather_data = WeatherData(
                    user_id=user_id,
                    datetime=datetime.now(),
                    city_id=response['id'],
                    temperature=response['main']['temp'],
                    humidity=response['main']['humidity']
                )
                session.add(weather_data)
                session.commit()

            await asyncio.sleep(60)

        return [wd.as_dict() for wd in session.query(WeatherData).filter_by(user_id=user_id).all()]
