#!/usr/bin/python3
"""Write a script that creates the State “California”
    with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""
from sys import argv
from relationship_city import City, Base
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_state_city():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_list = session.query(State).order_by(State.id).all()
    for s in new_list:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("    {}: {}".format(c.id, c.name))
    session.close()

if __name__ == "__main__":
    list_state_city()
