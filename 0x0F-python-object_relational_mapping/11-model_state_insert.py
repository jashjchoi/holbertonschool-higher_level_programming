#!/usr/bin/python3
"""Add the new State obj "Louisiana"
   from the db hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_new_state():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_st = State(name="Louisiana")
    session.add(new_st)
    session.commit()
    res = session.query(State).filter_by(name="Louisiana").first()
    print("{}".format(res.id))
    session.close()

if __name__ == "__main__":
    add_new_state()
