"""
Database models.

Declare all your db models here.
Depending on the ORM that you are using, each model will be used to map the
database to an ORM object.

You can also map the database models to Pydantic model (typically in response.py)
See: https://fastapi.tiangolo.com/tutorial/sql-databases/

Below is an example of an SQLAlchemy Model
"""
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
