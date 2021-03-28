#!/usr/bin/python3
"""lists all State objects from the db hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine


def list_state_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    result = engine.execute('SELECT * FROM states ORDER BY states.id ASC')
    for i in result:
        print("{}: {}".format(i[0], i[1]))

if __name__ == "__main__":
    list_state_obj()
