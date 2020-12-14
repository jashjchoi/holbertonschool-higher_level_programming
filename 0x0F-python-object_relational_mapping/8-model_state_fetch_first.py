#!/usr/bin/python3
"""prints the first State object from the db hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def first_state_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        res = session.query(State).first()
        print("{}: {}".format(res.id, res.name))
    except:
        print("Nothing")
    session.close()

if __name__ == "__main__":
    first_state_obj()
