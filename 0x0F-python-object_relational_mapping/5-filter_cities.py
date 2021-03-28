#!/usr/bin/python3
"""takes in the name of a state as an arg
lists all cities of that state
using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def filter_cities():
    """takes 3 arguments argv to list from db
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    """creates a cursor and executes query"""
    cur = db.cursor()
    cmd = """SELECT cities.name
             FROM cities, states
             WHERE BINARY states.name = %s
             AND cities.state_id = states.id
             ORDER BY cities.id ASC"""
    cur.execute(cmd, (sys.argv[4],))
    states = cur.fetchall()
    print(", ".join(i[0] for i in states))
    """closes cursor and db"""
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
