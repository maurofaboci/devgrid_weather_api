from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from app.Enum import EStatus
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    city_id = Column(Integer, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "datetime": self.datetime.isoformat(),
            "city_id": self.city_id,
            "temperature": self.temperature,
            "humidity": self.humidity
        }

class PostWeatherInfos(Base):
    __tablename__ = 'post_weather_info'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    total_cities = Column(Integer, nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=True)
    status = Column(Enum(EStatus, values_callable=lambda obj: [e.value for e in obj]),nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total_cities": self.total_cities,
            "date_start": self.date_start.isoformat(),
            "date_end": self.date_end.isoformat(),
            "status": self.status
        }

