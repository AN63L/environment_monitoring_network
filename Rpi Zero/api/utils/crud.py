from sqlalchemy.orm import Session
from models import models, sensors, notifications
from datetime import datetime, timezone
import pytz
import math
from utils.utils import (
    process_labels_single_dataset_charts,
    process_labels_multiple_dataset_charts,
)
from sqlalchemy import inspect
from db.connection import engine


def list_metrics_1(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.Sensor1).offset(skip).limit(limit).all()
    except Exception as e:
        print("Error: ", e)
        return


def list_metrics_2(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.Sensor2).offset(skip).limit(limit).all()
    except Exception as e:
        print("Error: ", e)
        return


def create_sensor1(db: Session, data: sensors.Sensor1Create):
    try:
        sensor1 = models.Sensor1(
            temperature=data.temperature,
            pressure=data.pressure,
            humidity=data.humidity,
            gas_resistance=data.gas_resistance,
            altitude=data.altitude,
            pm_1=data.pm_1,
            pm_2=data.pm_2,
            pm_10=data.pm_10,
        )
        db.add(sensor1)
        db.commit()
        db.refresh(sensor1)
        return sensor1
    except Exception as e:
        print("Error: ", e)
        return


def create_sensor2(db: Session, data: sensors.Sensor2Create):
    try:
        sensor2 = models.Sensor2(
            rain_raw_reading=data.rain_raw_reading,
            rain_resistance=data.rain_resistance,
            rain_percentage=data.rain_percentage,
            is_raining=data.is_raining,
            soil_raw_reading=data.soil_raw_reading,
            soil_resistance=data.soil_resistance,
            soil_moist_percentage=data.soil_moist_percentage,
            is_soil_moist=data.is_soil_moist,
        )
        db.add(sensor2)
        db.commit()
        db.refresh(sensor2)
        return sensor2
    except Exception as e:
        print("Error: ", e)
        return


def get_latest(db: Session, skip: int = 0, limit: int = 100):
    try:
        # get the most recent lines from each table
        data_sensor_1 = (
            db.query(models.Sensor1).order_by(models.Sensor1.created_at.desc()).first()
        )
        data_sensor_2 = (
            db.query(models.Sensor2).order_by(models.Sensor2.created_at.desc()).first()
        )

        # get delay in seconds - don't forget to convert to utc all the dates to avoid issued!
        current = datetime.now(timezone.utc)
        f = "%Y-%m-%d %H:%M:%S.%f%z"
        utc = pytz.utc
        sensor_1_latest = datetime.strptime(
            str(data_sensor_1.created_at), f
        ).astimezone(utc)
        sensor_2_latest = datetime.strptime(
            str(data_sensor_2.created_at), f
        ).astimezone(utc)
        # we are only interested in the integer
        data_sensor_1.last_update_seconds = math.trunc(
            (current - sensor_1_latest).total_seconds()
        )
        data_sensor_2.last_update_seconds = math.trunc(
            (current - sensor_2_latest).total_seconds()
        )

        obj = {}
        obj["sensor_1"] = data_sensor_1
        obj["sensor_2"] = data_sensor_2

        return obj
    except Exception as e:
        print("Error: ", e)
        return


def get_chart_data(chartId: str, filter: str, db: Session):
    try:
        # handle chart type and query filter
        data = None
        if chartId == "temp_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.TempAllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.TempDaily).offset(0).all(), filter, chartId
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.TempWeekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.TempMonthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.TempYearly).offset(0).all(),
                    filter,
                    chartId,
                )
        elif chartId == "humidity_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.HumidityAllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.HumidityDaily).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.HumidityWeekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.HumidityMonthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.HumidityYearly).offset(0).all(),
                    filter,
                    chartId,
                )
        elif chartId == "pressure_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.PressureAllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.PressureDaily).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.PressureWeekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.PressureMonthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.PressureYearly).offset(0).all(),
                    filter,
                    chartId,
                )
        elif chartId == "gas_resistance_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.GasResAllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.GasResDaily).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.GasResWeekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.GasResMonthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.GasResYearly).offset(0).all(),
                    filter,
                    chartId,
                )
        elif chartId == "pm1_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM1AllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM1Daily).offset(0).all(), filter, chartId
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM1Weekly).offset(0).all(), filter, chartId
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM1Monthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM1Yearly).offset(0).all(), filter, chartId
                )
        elif chartId == "pm25_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM2AllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM2Daily).offset(0).all(), filter, chartId
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM2Weekly).offset(0).all(), filter, chartId
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM2Monthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM2Yearly).offset(0).all(), filter, chartId
                )
        elif chartId == "pm10_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM10AllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM10Daily).offset(0).all(), filter, chartId
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM10Weekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM10Monthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.PM10AllTime).offset(0).all(),
                    filter,
                    chartId,
                )
        elif chartId == "rain_chart":
            if filter == -1:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.RainFreqAllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.RainFreqDaily).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 7:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.RainFreqWeekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.RainFreqMonthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.RainFreqYearly).offset(0).all(),
                    filter,
                    chartId,
                )
        elif chartId == "moisture_chart":
            if filter == -1:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.SoilMoistFreqAllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.SoilMoistFreqDaily).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 7:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.SoilMoistFreqWeekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.SoilMoistFreqMonthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_multiple_dataset_charts(
                    db.query(models.SoilMoistFreqYearly).offset(0).all(),
                    filter,
                    chartId,
                )
        elif chartId == "rain_percentage_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.RainPercAllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.RainPercDaily).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.RainPercWeekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.RainPercMonthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.RainPercYearly).offset(0).all(),
                    filter,
                    chartId,
                )
        elif chartId == "moisture_percentage_chart":
            if filter == -1:
                data = process_labels_single_dataset_charts(
                    db.query(models.SoilMoistPercAllTime).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 0:
                data = process_labels_single_dataset_charts(
                    db.query(models.SoilMoistPercDaily).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 7:
                data = process_labels_single_dataset_charts(
                    db.query(models.SoilMoistPercWeekly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 30:
                data = process_labels_single_dataset_charts(
                    db.query(models.SoilMoistPercMonthly).offset(0).all(),
                    filter,
                    chartId,
                )
            elif filter == 365:
                data = process_labels_single_dataset_charts(
                    db.query(models.SoilMoistPercYearly).offset(0).all(),
                    filter,
                    chartId,
                )
        return data
    except Exception as e:
        print("Error: ", e)
        return


def populate_notifications_table(db: Session):
    # check table exist -> it should at db init - you don't need to create it manually
    table_exists = inspect(engine, True).has_table("notifications", schema="metrics")
    if table_exists:
        # now check if table has items
        rows = db.query(models.Notifications).count()
        if rows == 0:
            # insert data
            notification_types = [
                "sensor_1_last_update_over_10",
                "sensor_2_last_update_over_10",
                "soil_very_dry",
                "soil_very_moist",
                "started_raining",
                "stopped_raining",
            ]
            for item in notification_types:
                notification_type = models.Notifications(name=item, active=True)
                db.add(notification_type)
                db.commit()
                db.refresh(notification_type)
        else:
            print("notifications table populated")


def get_notifications(db: Session):
    try:
        # if first call, will need to populate table
        populate_notifications_table(db)
        return db.query(models.Notifications).all()
    except Exception as e:
        print("Error: ", e)
        return


def update_notifications(
    db: Session, notificationId: str, value: notifications.updateNotificationStatus
):
    try:
        db.query(models.Notifications).filter(
            models.Notifications.name == notificationId
        ).update({"active": value})
        db.commit()
        return (
            db.query(models.Notifications)
            .filter(models.Notifications.name == notificationId)
            .all()
        )
    except Exception as e:
        print("Error: ", e)
        return
