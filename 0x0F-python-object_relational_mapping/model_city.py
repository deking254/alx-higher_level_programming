#!/usr/bin/python3
"""that contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
Base = declarative_base()


class City(Base):
    """the class for the city object"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
