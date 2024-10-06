import os
from dotenv import load_dotenv

load_dotenv(".env")

print("connecting to db....")
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import reflection
from sqlalchemy import MetaData, Table, select
from sqlalchemy.ext.automap import automap_base

SQLALCHEMY_DATABASE_URL = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PWD")}@{os.getenv("DB_IP")}/{os.getenv("DB_NAME")}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


print("CONNECTED")
