#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    query = 'mysql+mysqldb://{}:{}@localhost/{}'
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    engine = create_engine(query.format(a, b, c), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    se = Session()
    state_new = State(name="Carlifonia")
    city_new = City(name='San Francisco', state=state_new)
    se.add(city_new)
    se.commit()
    se.close()
