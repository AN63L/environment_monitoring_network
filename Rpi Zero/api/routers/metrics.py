from fastapi import APIRouter
from typing import List
from fastapi import HTTPException, Depends
from fastapi import APIRouter, status as httpStatus, Response
import utils.errorBuilder as errorBuilder
from sqlalchemy.orm import Session
from fastapi import Request

from db.connection import get_db

from models import models, sensors
from db.connection import engine
from utils import crud

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("/sensor_1", response_model=list[sensors.Sensor1])
def get_metrics_1(
    response: Response, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        data = crud.list_metrics_1(db, skip=skip, limit=limit)
        return data
    except Exception as e:
        print("ERROR: ", e)
        response.status_code = httpStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return errorBuilder.server_error()


@router.get("/sensor_2", response_model=list[sensors.Sensor2])
def get_metrics_2(
    response: Response, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        data = crud.list_metrics_2(db, skip=skip, limit=limit)
        return data
    except Exception as e:
        print("ERROR: ", e)
        response.status_code = httpStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return errorBuilder.server_error()


@router.post("/sensor_1", response_model=sensors.Sensor1, status_code=201)
async def post_metrics_1(
    response: Response, data: sensors.Sensor1Create, db: Session = Depends(get_db)
):
    try:
        print("posting metrics 1....")
        return crud.create_sensor1(db=db, data=data)
    except Exception as e:
        print("ERROR: ", e)
        response.status_code = httpStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return errorBuilder.server_error()


@router.post("/sensor_2", response_model=sensors.Sensor2, status_code=201)
async def post_metrics_2(
    response: Response, data: sensors.Sensor2Create, db: Session = Depends(get_db)
):
    try:
        print("posting metrics 2....")
        return crud.create_sensor2(db=db, data=data)
    except Exception as e:
        print("ERROR: ", e)
        response.status_code = httpStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return errorBuilder.server_error()


# get chart by id and integrate filter (for graphs page)
@router.get("/charts/{chartId}", status_code=200)
async def get_chart(
    response: Response,
    chartId: str,
    filter_by: str = "",
    db: Session = Depends(get_db),
):
    try:
        validChartIds = [
            "temp_chart",
            "humidity_chart",
            "pressure_chart",
            "gas_resistance_chart",
            "pm1_chart",
            "pm25_chart",
            "pm10_chart",
            "rain_chart",
            "moisture_chart",
            "rain_percentage_chart",
            "moisture_percentage_chart",
        ]
        print("filter_by: ", filter_by)
        print("chartId: ", chartId)
        if chartId is None:
            print("missing chartId")
            response.status_code = httpStatus.HTTP_400_BAD_REQUEST
            return errorBuilder.missing_path_parameter("chartId")
        if filter_by is None:
            print("missing filter")
            response.status_code = httpStatus.HTTP_400_BAD_REQUEST
            return errorBuilder.missing_query_parameter("filter")
        if int(filter_by) not in [-1, 0, 7, 30, 365]:
            print("Invalid filter value")
            response.status_code = httpStatus.HTTP_400_BAD_REQUEST
            return errorBuilder.invalid_field(
                "filter", filter_by, "Please provide a valid filter value"
            )
        if chartId not in validChartIds:
            print("Invalid filter value")
            response.status_code = httpStatus.HTTP_400_BAD_REQUEST
            return errorBuilder.invalid_field(
                "chartId", chartId, "Please provide a valid chartId value"
            )
        print("getting chart data....")
        data = crud.get_chart_data(chartId, int(filter_by), db)
        return data
    except Exception as e:
        print("ERROR: ", e)
        response.status_code = httpStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return errorBuilder.server_error()


# get latest values (for dashboard page)
@router.get("/latest", status_code=200)
async def get_latest(
    response: Response,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    try:
        print("getting latest values...")
        return crud.get_latest(db=db, skip=skip, limit=limit)
    except Exception as e:
        print("ERROR: ", e)
        response.status_code = httpStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return errorBuilder.server_error()
