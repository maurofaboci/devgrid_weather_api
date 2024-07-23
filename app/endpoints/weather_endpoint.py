import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from ..weather_utils import collect_weather_data
from ..database import get_db
from ..models import WeatherData, PostWeatherInfos, EStatus
from ..schemas import WeatherDataCreate, WeatherDataResponse
from datetime import datetime
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/weather", response_model=WeatherDataResponse)
async def create_weather_data(data: WeatherDataCreate, session: Session = Depends(get_db)):
    try:
        user_id = data.user_id
        
        existing_record = session.query(PostWeatherInfos).filter_by(user_id=user_id).first()
        if existing_record:
            raise HTTPException(status_code=400, detail="User ID already exists. Please use a unique ID for each request.")
        
        requistion_data = PostWeatherInfos(
            user_id=user_id,
            total_cities=len(data.city_ids),
            date_start=datetime.now(),
            status=EStatus.IN_PROGRESS
        )
        session.add(requistion_data)
        session.commit()
        session.refresh(requistion_data)

        weather_data = await collect_weather_data(user_id, data.city_ids, session)

        if weather_data:
            requistion_data.status = EStatus.FINISHED
            requistion_data.date_end = datetime.now()
            session.commit()
            return JSONResponse(content={"request_info": requistion_data.as_dict(), "data": weather_data})
        else:
            requistion_data.status = EStatus.ERROR
            requistion_data.date_end = datetime.now()
            session.commit()
            raise HTTPException(status_code=400, detail="Something went wrong trying to collect weather data")

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        if 'requistion_data' in locals():
            requistion_data.status = EStatus.ERROR
            requistion_data.date_end = datetime.now()
            session.commit()
        raise HTTPException(status_code=500, detail=f'An error occurred: {e}')


@router.get("/weather/{user_id}")
def get_weather_progress(user_id: str, session : Session = Depends(get_db)):
    try:
        total_cities = session.query(PostWeatherInfos.total_cities).filter_by(user_id=user_id).scalar()
        collected_cities = session.query(WeatherData).filter_by(user_id=user_id).count()
        progress_percentage = (collected_cities / total_cities) * 100 if total_cities > 0 else 0
        progress_percentage = float(format(progress_percentage, ".2f"))
        
        return {"progress_percentage": progress_percentage}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'An error occurred: {e}')

@router.get("/weather_post_info/{user_id}")
def get_weather_progress(user_id: str, session : Session = Depends(get_db)):
    try:
        request_info = session.query(PostWeatherInfos).filter_by(user_id=user_id).first()
        return request_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'An error occurred: {e}')

    