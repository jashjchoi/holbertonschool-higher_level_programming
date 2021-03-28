#!/usr/bin/python3
"""prints all City objects
   from the db hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_st():
    """sorted in ascending order by cities.id
       results must be display as:
       <state name>: (<city id>) <city name>
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in res:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

if __name__ == "__main__":
    fetch_cities_by_st()
