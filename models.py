from sqlalchemy.orm import declarative_base
from sqlalchemy import *

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)

    email = Column(String, unique=True)

    password = Column(String)

    role = Column(String)


class WeatherRecord(Base):
    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True)

    city = Column(String)

    temperature = Column(Float)

    humidity = Column(Float)

    condition = Column(String)

    wind_speed = Column(Float)

    timestamp = Column(DateTime)