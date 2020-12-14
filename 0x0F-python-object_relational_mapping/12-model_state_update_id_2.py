#!/usr/bin/python3
"""Change the name of a State object
   from the db hbtn_0e_6_usa
   2: Arizona => 2: New Mexico
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter_by(id="2").first()
    res.name = "New Mexico"
    session.commit()
    session.close()

if __name__ == "__main__":
    update_state()
