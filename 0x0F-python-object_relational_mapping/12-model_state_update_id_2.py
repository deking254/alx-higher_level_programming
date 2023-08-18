#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
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
    rt = se.query(State).filter(State.id.like("2")).all()
    if rt[0].id == 2:
        rt[0].name = "New Mexico"
    se.commit()
    se.close()
