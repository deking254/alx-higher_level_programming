#!/usr/bin/python3
import sqlalchemy;
from sqlalchemy import Column, Integer, String;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.orm import relationship;
import MySQLdb;

Base = declarative_base();
class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship('City', back_populates="state", cascade="all, delete-orphan")
