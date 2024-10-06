from pydantic import BaseModel


class Sensor1Base(BaseModel):
    temperature: float
    pressure: float
    humidity: float
    gas_resistance: float
    altitude: float
    pm_1: float
    pm_2: float
    pm_10: float

    class Config:
        orm_mode = True


class Sensor2Base(BaseModel):
    rain_raw_reading: float
    rain_resistance: float
    rain_percentage: float
    is_raining: bool
    soil_raw_reading: float
    soil_resistance: float
    soil_moist_percentage: float
    is_soil_moist: bool

    class Config:
        orm_mode = True


class Sensor1Create(Sensor1Base):
    pass

    class Config:
        orm_mode = True


class Sensor2Create(Sensor2Base):
    pass

    class Config:
        orm_mode = True


class Sensor1(Sensor1Base):
    id: int

    class Config:
        from_attributes: True
        orm_mode = True


class Sensor2(Sensor2Base):
    id: int

    class Config:
        from_attributes: True
        orm_mode = True
