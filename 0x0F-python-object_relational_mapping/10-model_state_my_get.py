#!/usr/bin/python3
"""prints the State obj with the name passed as arg
   from the db hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        res = session.query(State).filter_by(name=argv[4]).first()
        print("{}".format(res.id))
    except:
        print("Not found")
    session.close()

if __name__ == "__main__":
    get_state()
