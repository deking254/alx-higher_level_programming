#!/usr/bin/python3
"""the files model_city.py and model_state.py, and save them as """
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import MySQLdb
Base = declarative_base()


class State(Base):
    """create the state class definition"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cas = "all, delete-orphan"
    cities = relationship('City', back_populates="state", cascade=cas)
