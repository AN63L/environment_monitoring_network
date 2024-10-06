# db libs
from db.connection import engine
from sqlalchemy import text
from db.connection import engine
from models import models
from sqlalchemy.orm import sessionmaker

# date processing libs
from datetime import datetime, timezone

# set log level
import logging

logging.basicConfig(level=logging.INFO)

# mailgun API libs
import requests

# environment variables
import os
from dotenv import load_dotenv

load_dotenv()
TO_EMAIL = os.getenv("TO_EMAIL")
MAIL_GUN_API_KEY = os.getenv("MAIL_GUN_API_KEY")
MAIL_GUN_API_URL = os.getenv("MAIL_GUN_API_URL")
MAIL_GUN_FROM_EMAIL_ADDRESS = os.getenv("MAIL_GUN_FROM_EMAIL_ADDRESS")


def execute_statement(statement):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(statement))
            return result.mappings().all()
    except Exception as e:
        print("Error executing statement: ", e)


def send_email(notification_type):
    try:
        print("sending notification for type: ", notification_type)
        subject = "Notification from environment system:  %s" % str(notification_type)
        message = "New notification received !"
        resp = requests.post(
            MAIL_GUN_API_URL,
            auth=("api", MAIL_GUN_API_KEY),
            data={
                "from": MAIL_GUN_FROM_EMAIL_ADDRESS,
                "to": TO_EMAIL,
                "subject": subject,
                "text": message,
            },
        )
        if resp.status_code == 200:
            logging.info(f"Successfully sent an email to '{TO_EMAIL}' via Mailgun API.")
        else:
            logging.error(f"Could not send the email, reason: {resp.text}")
    except Exception as e:
        print("ERROR sending notification: ", e)


def check_last_log_for_type(notification_type):
    try:
        print("checking last notification log for type: ", notification_type)
        statement = """SELECT created_at FROM metrics.notifications_log WHERE type = '{}' ORDER BY created_at DESC LIMIT 1""".format(
            str(notification_type)
        )
        response = execute_statement(statement)
        # notification never sent
        if len(response) == 0:
            return True
        # check if already sent today
        if notification_type == "sensor_1_last_update_over_10":
            if get_date_diff_in_minutes(response[0]["created_at"]) > 1440:
                return True
        if notification_type == "sensor_2_last_update_over_10":
            if get_date_diff_in_minutes(response[0]["created_at"]) > 1440:
                return True
        # check if already sent today
        if notification_type == "soil_very_dry":
            if get_date_diff_in_minutes(response[0]["created_at"]) > 1440:
                return True
        if notification_type == "soil_very_moist":
            if get_date_diff_in_minutes(response[0]["created_at"]) > 1440:
                return True
        # we don't want to send a notification every time every time the sensor detects it is raining
        # check if a started_raining was sent and no stopped raining was sent afterwards
        # if wasn't then should be sent
        if notification_type == "started_raining":
            last_time_started_raining = response[0]["created_at"]
            statement = """SELECT created_at FROM metrics.notifications_log WHERE type = '{}' ORDER BY created_at DESC LIMIT 1""".format(
                "stopped_raining"
            )
            response = execute_statement(statement)
            last_time_stopped_raining = response[0]["created_at"]
            if last_time_stopped_raining > last_time_started_raining:
                return True
        # we don't want to send a notification every time every time the sensor detects it isn't raining
        # check if a started_raining was sent and no stopped raining was sent afterwards
        # if wasn't sent then
        if notification_type == "stopped_raining":
            last_time_stopped_raining = response[0]["created_at"]
            statement = """SELECT created_at FROM metrics.notifications_log WHERE type = '{}' ORDER BY created_at DESC LIMIT 1""".format(
                "started_raining"
            )
            response = execute_statement(statement)
            last_time_started_raining = response[0]["created_at"]
            if last_time_stopped_raining < last_time_started_raining:
                return True
        return False
    except Exception as e:
        print("ERROR checking log table: ", e)


# This will throw the following error
# Class 'sqlalchemy.orm.decl_api.DeclarativeMeta' is not mapped; was a class (models.models.NotificationsLog) supplied where an instance was required?
# But it still works
def insert_log_item(notification_type):
    try:
        print("inserting log item for type: ", notification_type)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(models.NotificationsLog(type=notification_type))
        session.commit()
        session.refresh(models.NotificationsLog)
    except Exception as e:
        print("ERROR inserting log item: ", e)


def get_date_diff_in_minutes(last_received):
    current = datetime.now(timezone.utc)
    minutes_diff = int((current - last_received).total_seconds() / 60.0)
    return minutes_diff


def check_preferences(notification_type):
    statement = """SELECT active FROM metrics.notifications WHERE name = '{}'""".format(
        str(notification_type)
    )
    response = execute_statement(statement)
    return response[0]["active"]


def process_notification_sensor_1():
    pref = check_preferences("sensor_1_last_update_over_10")
    print("pref: ", pref)
    if pref:
        data = execute_statement(
            "SELECT created_at FROM metrics.sensor_1 ORDER BY created_at DESC LIMIT 1"
        )
        minutes_diff = get_date_diff_in_minutes(data[0]["created_at"])
        print("minutes_diff: ", minutes_diff)
        if minutes_diff > 10:
            to_send = check_last_log_for_type("sensor_1_last_update_over_10")
            if to_send:
                print("SENT")
                send_email("sensor_1_last_update_over_10")
                insert_log_item("sensor_1_last_update_over_10")
            else:
                print("NOT SENT")


def process_notification_sensor_2():
    pref = check_preferences("sensor_2_last_update_over_10")
    if pref:
        data = execute_statement(
            "SELECT created_at FROM metrics.sensor_2 ORDER BY created_at DESC LIMIT 1"
        )
        print("data: ", data[0])
        minutes_diff = get_date_diff_in_minutes(data[0]["created_at"])
        print("minutes_diff: ", minutes_diff)
        if minutes_diff > 10:
            to_send = check_last_log_for_type("sensor_2_last_update_over_10")
            if to_send:
                print("SENT")
                send_email("sensor_2_last_update_over_10")
                insert_log_item("sensor_2_last_update_over_10")
            else:
                print("NOT SENT")


def process_notification_started_raining():
    pref = check_preferences("started_raining")
    if pref:
        data = execute_statement(
            "SELECT is_raining FROM metrics.sensor_2 ORDER BY created_at DESC LIMIT 1"
        )
        is_raining = data[0]["is_raining"]
        print("is_raining: ", is_raining)
        if is_raining:
            to_send = check_last_log_for_type("started_raining")
            if to_send:
                print("SENT")
                send_email("started_raining")
                insert_log_item("started_raining")
            else:
                print("NOT SENT")


def process_notification_stopped_raining():
    pref = check_preferences("stopped_raining")
    if pref:
        data = execute_statement(
            "SELECT is_raining FROM metrics.sensor_2 ORDER BY created_at DESC LIMIT 1"
        )
        is_raining = data[0]["is_raining"]
        print("is_raining: ", is_raining)
        if not is_raining:
            to_send = check_last_log_for_type("stopped_raining")
            if to_send:
                print("SENT")
                send_email("stopped_raining")
                insert_log_item("stopped_raining")
            else:
                print("NOT SENT")


def process_notification_soil_very_dry():
    pref = check_preferences("soil_very_dry")
    if pref:
        data = execute_statement(
            "SELECT soil_moist_percentage FROM metrics.sensor_2 ORDER BY created_at DESC LIMIT 1"
        )
        perc = round(float(data[0]["soil_moist_percentage"]), 1)
        print("perc: ", perc)
        if perc < 0.3:
            to_send = check_last_log_for_type("soil_very_dry")
            if to_send:
                print("SENT")
                send_email("soil_very_dry")
                insert_log_item("soil_very_dry")
            else:
                print("NOT SENT")


def process_notification_soil_very_moist():
    pref = check_preferences("soil_very_moist")
    if pref:
        data = execute_statement(
            "SELECT soil_moist_percentage FROM metrics.sensor_2 ORDER BY created_at DESC LIMIT 1"
        )
        perc = round(float(data[0]["soil_moist_percentage"]), 1)
        print("perc: ", perc)
        if perc > 0.7:
            to_send = check_last_log_for_type("soil_very_moist")
            if to_send:
                print("SENT")
                send_email("soil_very_moist")
                insert_log_item("soil_very_moist")
            else:
                print("NOT SENT")
