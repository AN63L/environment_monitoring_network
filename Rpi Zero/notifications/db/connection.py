import os
from dotenv import load_dotenv

load_dotenv(".env")

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PWD")}@{os.getenv("DB_IP")}/{os.getenv("DB_NAME")}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
