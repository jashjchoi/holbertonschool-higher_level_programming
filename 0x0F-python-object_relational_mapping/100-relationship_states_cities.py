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


def rel_state_city():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='California')
    new_state.cities = [City(name='San Francisco')]
    session.add(new_state)
    session.commit()
    session.close()

if __name__ == "__main__":
    rel_state_city()
