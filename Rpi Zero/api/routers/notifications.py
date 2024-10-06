from fastapi import APIRouter
from typing import Union
from fastapi import Depends
from fastapi import APIRouter, status as httpStatus, Response
import utils.errorBuilder as errorBuilder
from sqlalchemy.orm import Session

from db.connection import get_db
from models import models, notifications
from db.connection import engine
from utils import crud

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("/", response_model=list[notifications.Notifications])
def get_notifications(response: Response, db: Session = Depends(get_db)):
    try:
        data = crud.get_notifications(db)
        return data
    except Exception as e:
        print("ERROR: ", e)
        response.status_code = httpStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return errorBuilder.server_error()


@router.put("/{notificationId}", status_code=200)
def update_notifications(
    response: Response,
    notificationId: str,
    body: Union[notifications.updateNotificationStatus, None] = None,
    db: Session = Depends(get_db),
):
    try:
        # check path param is valid and present
        validNotificationIds = [
            "sensor_1_last_update_over_10",
            "sensor_2_last_update_over_10",
            "soil_very_dry",
            "soil_very_moist",
            "started_raining",
            "stopped_raining",
        ]
        if body is None:
            print("missing body")
            response.status_code = httpStatus.HTTP_400_BAD_REQUEST
            return errorBuilder.missing_body()
        if body.value not in [True, False]:
            print("missing body")
            response.status_code = httpStatus.HTTP_400_BAD_REQUEST
            return errorBuilder.invalid_body("value")
        if notificationId is None:
            print("missing chartId")
            response.status_code = httpStatus.HTTP_400_BAD_REQUEST
            return errorBuilder.missing_path_parameter("notificationId")
        if notificationId not in validNotificationIds:
            print("Invalid notificationId value")
            response.status_code = httpStatus.HTTP_400_BAD_REQUEST
            return errorBuilder.invalid_field(
                "notificationId",
                notificationId,
                "Please provide a valid notificationId value",
            )
        data = crud.update_notifications(db, notificationId, body.value)
        return data
    except Exception as e:
        print("ERROR: ", e)
        response.status_code = httpStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return errorBuilder.server_error()
