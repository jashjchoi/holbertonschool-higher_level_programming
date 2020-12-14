#!/usr/bin/python3
""" lists all State objects that contain the letter 'a'
    from the db hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_state_with_A():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.name.contains('a'))\
                              .order_by(State.id).all()
    for state in res:
        print("{}: {}".format(state.id, state.name))
    session.close()

if __name__ == "__main__":
    filter_state_with_A()
