#!/usr/bin/python3
"""Deletes all State objects with a name
   containing the letter 'a'
   from the db hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def del_state_with_A():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.name.contains('a'))\
                              .order_by(State.id).all()
    for state in res:
        session.delete(state)
    session.commit()
    session.close()

if __name__ == "__main__":
    del_state_with_A()
