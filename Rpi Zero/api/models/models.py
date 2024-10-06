# ORM models
from sqlalchemy import Boolean, Column, Integer, String, Float, TIMESTAMP, text, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import func

from db.connection import Base
from db.connection import engine


#### SENSOR TABLES ###
class Sensor1(Base):
    __tablename__ = "sensor_1"

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=True, index=True)
    pressure = Column(Float, nullable=True, index=True)
    humidity = Column(Float, nullable=True, index=True)
    gas_resistance = Column(Float, nullable=True, index=True)
    altitude = Column(Float, nullable=True, index=True)
    pm_1 = Column(Float, nullable=True, index=True)
    pm_2 = Column(Float, nullable=True, index=True)
    pm_10 = Column(Float, nullable=True, index=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        nullable=False,
        index=True,
    )

    __table_args__ = {"schema": "metrics"}


class Sensor2(Base):
    __tablename__ = "sensor_2"

    id = Column(Integer, primary_key=True)
    rain_raw_reading = Column(Float, nullable=True, index=True)
    rain_resistance = Column(Float, nullable=True, index=True)
    rain_percentage = Column(Float, nullable=True, index=True)
    is_raining = Column(Boolean, nullable=True, index=True)
    soil_raw_reading = Column(Float, nullable=True, index=True)
    soil_resistance = Column(Float, nullable=True, index=True)
    soil_moist_percentage = Column(Float, nullable=True, index=True)
    is_soil_moist = Column(Boolean, nullable=True, index=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        nullable=False,
        index=True,
    )

    __table_args__ = {"schema": "metrics"}


#### NOTIFICATIONS TABLE ###


class Notifications(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    active = Column(Boolean, nullable=False, index=True)

    __table_args__ = {"schema": "metrics"}


class NotificationsLog(Base):
    __tablename__ = "notifications_log"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False, index=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        nullable=False,
        index=True,
    )

    __table_args__ = {"schema": "metrics"}


#### DEFINES THE VIEWS ###


## TEMPERATURE
class TempDaily(Base):
    __table__ = Table(
        "temperature_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class TempWeekly(Base):
    __table__ = Table(
        "temperature_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class TempMonthly(Base):
    __table__ = Table(
        "temperature_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class TempYearly(Base):
    __table__ = Table(
        "temperature_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class TempAllTime(Base):
    __table__ = Table(
        "temperature_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## HUMIDITY
class HumidityDaily(Base):
    __table__ = Table(
        "humidity_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class HumidityWeekly(Base):
    __table__ = Table(
        "humidity_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class HumidityMonthly(Base):
    __table__ = Table(
        "humidity_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class HumidityYearly(Base):
    __table__ = Table(
        "humidity_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class HumidityAllTime(Base):
    __table__ = Table(
        "humidity_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## PRESSURE
class PressureDaily(Base):
    __table__ = Table(
        "pressure_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PressureWeekly(Base):
    __table__ = Table(
        "pressure_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PressureMonthly(Base):
    __table__ = Table(
        "pressure_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PressureYearly(Base):
    __table__ = Table(
        "pressure_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PressureAllTime(Base):
    __table__ = Table(
        "pressure_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## GAS RESISTANCE
class GasResDaily(Base):
    __table__ = Table(
        "gas_resistance_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class GasResWeekly(Base):
    __table__ = Table(
        "gas_resistance_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class GasResMonthly(Base):
    __table__ = Table(
        "gas_resistance_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class GasResYearly(Base):
    __table__ = Table(
        "gas_resistance_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class GasResAllTime(Base):
    __table__ = Table(
        "gas_resistance_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## PM1
class PM1Daily(Base):
    __table__ = Table(
        "pm_1_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM1Weekly(Base):
    __table__ = Table(
        "pm_1_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM1Monthly(Base):
    __table__ = Table(
        "pm_1_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM1Yearly(Base):
    __table__ = Table(
        "pm_1_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM1AllTime(Base):
    __table__ = Table(
        "pm_1_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## PM2
class PM2Daily(Base):
    __table__ = Table(
        "pm_2_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM2Weekly(Base):
    __table__ = Table(
        "pm_2_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM2Monthly(Base):
    __table__ = Table(
        "pm_2_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM2Yearly(Base):
    __table__ = Table(
        "pm_2_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM2AllTime(Base):
    __table__ = Table(
        "pm_2_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## PM10
class PM10Daily(Base):
    __table__ = Table(
        "pm_10_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM10Weekly(Base):
    __table__ = Table(
        "pm_10_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM10Monthly(Base):
    __table__ = Table(
        "pm_10_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM10Yearly(Base):
    __table__ = Table(
        "pm_10_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class PM10AllTime(Base):
    __table__ = Table(
        "pm_10_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## RAIN PERCENTAGE
class RainPercDaily(Base):
    __table__ = Table(
        "rain_percentage_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class RainPercWeekly(Base):
    __table__ = Table(
        "rain_percentage_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class RainPercMonthly(Base):
    __table__ = Table(
        "rain_percentage_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class RainPercYearly(Base):
    __table__ = Table(
        "rain_percentage_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class RainPercAllTime(Base):
    __table__ = Table(
        "rain_percentage_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## SOIL MOISTURE PERCENTAGE
class SoilMoistPercDaily(Base):
    __table__ = Table(
        "soil_moist_percentage_daily_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class SoilMoistPercWeekly(Base):
    __table__ = Table(
        "soil_moist_percentage_weekly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class SoilMoistPercMonthly(Base):
    __table__ = Table(
        "soil_moist_percentage_monthly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class SoilMoistPercYearly(Base):
    __table__ = Table(
        "soil_moist_percentage_yearly_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class SoilMoistPercAllTime(Base):
    __table__ = Table(
        "soil_moist_percentage_all_time_average",
        Base.metadata,
        Column("avg", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## RAIN FREQUENCY
class RainFreqDaily(Base):
    __table__ = Table(
        "is_raining_frequency_daily_average",
        Base.metadata,
        Column("is_raining", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class RainFreqWeekly(Base):
    __table__ = Table(
        "is_raining_frequency_weekly_average",
        Base.metadata,
        Column("is_raining", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class RainFreqMonthly(Base):
    __table__ = Table(
        "is_raining_frequency_monthly_average",
        Base.metadata,
        Column("is_raining", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class RainFreqYearly(Base):
    __table__ = Table(
        "is_raining_frequency_yearly_average",
        Base.metadata,
        Column("is_raining", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class RainFreqAllTime(Base):
    __table__ = Table(
        "is_raining_frequency_all_time_average",
        Base.metadata,
        Column("is_raining", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


## SOIL MOISTURE FREQUENCY
class SoilMoistFreqDaily(Base):
    __table__ = Table(
        "is_soil_moist_frequency_daily_average",
        Base.metadata,
        Column("is_soil_moist", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class SoilMoistFreqWeekly(Base):
    __table__ = Table(
        "is_soil_moist_frequency_weekly_average",
        Base.metadata,
        Column("is_soil_moist", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class SoilMoistFreqMonthly(Base):
    __table__ = Table(
        "is_soil_moist_frequency_monthly_average",
        Base.metadata,
        Column("is_soil_moist", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class SoilMoistFreqYearly(Base):
    __table__ = Table(
        "is_soil_moist_frequency_yearly_average",
        Base.metadata,
        Column("is_soil_moist", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )


class SoilMoistFreqAllTime(Base):
    __table__ = Table(
        "is_soil_moist_frequency_all_time_average",
        Base.metadata,
        Column("is_soil_moist", Boolean, primary_key=True),
        Column("count", Float, primary_key=True),
        autoload_with=engine,
        schema="metrics",
    )
