#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine);
    se = Session();
    rt = se.query(State).all()
    for r in rt:
        print("{}. {}".format(r.id, r.name))
        citis = r.cities;
        for citi in citis:
             print("    {}. {}".format(citi.id, citi.name))
    se.close()
