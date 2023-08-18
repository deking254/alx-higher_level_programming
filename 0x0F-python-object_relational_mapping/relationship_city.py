#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey;
from sqlalchemy.orm import relationship;
from relationship_state import Base
import MySQLdb;

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")
