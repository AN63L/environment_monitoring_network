import sys
import datetime

# environment variables
import os
from dotenv import load_dotenv

load_dotenv()
RPI_USERNAME = os.getenv("RPI_USERNAME")

# functional files
from utils import crud

NOTIFICATION_TYPES = [
    "sensor_1_last_update_over_10",
    "sensor_2_last_update_over_10",
    "soil_very_dry",
    "soil_very_moist",
    "started_raining",
    "stopped_raining",
]


# returns -1 if error
# returns 0 if all okay
def main(notification_type):
    try:
        print("starting script execution...")

        # check if valid notification type
        if notification_type not in NOTIFICATION_TYPES:
            print("invalid notification type")
            return -1

        # every 10 minutes
        # Last sensor 1 data acquisition
        if notification_type == "sensor_1_last_update_over_10":
            crud.process_notification_sensor_1()
        # Last sensor 2 data acquisition
        if notification_type == "sensor_2_last_update_over_10":
            crud.process_notification_sensor_2()

        # hourly
        # Started raining
        if notification_type == "started_raining":
            crud.process_notification_started_raining()
        # Stopped raining
        if notification_type == "stopped_raining":
            crud.process_notification_stopped_raining()

        # daily
        # Soil very dry
        if notification_type == "soil_very_dry":
            crud.process_notification_soil_very_dry()
        # Soil very wet
        if notification_type == "soil_very_moist":
            crud.process_notification_soil_very_moist()

        print("COMPLETED EXECUTION...")
        return 0
    except Exception as e:
        print("MAIN ERROR: ", e)
        return -1


if __name__ == "__main__":
    # logs the data to logs/<file-name>.log
    notification_type = sys.argv[1]
    file_name = (
        datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
        + "_"
        + sys.argv[1]
        + ".log"
    )
    path = "/home/" + str(RPI_USERNAME) + "/notifications/logs/" + file_name
    sys.stdout = open(path, "w")
    print("notification_type: ", notification_type)
    main(notification_type)
