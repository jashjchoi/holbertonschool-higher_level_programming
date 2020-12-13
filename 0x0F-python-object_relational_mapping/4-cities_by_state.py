#!/usr/bin/python3
"""lists all cities from the db hbtn_0e_4_usa"""
import MySQLdb
import sys


def cities_by_states():
    """takes 3 arguments argv to list from db
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    """creates a cursor and executes query"""
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    for i in cur.fetchall():
        print(i)
    """closes cursor and db"""
    cur.close()
    db.close()


if __name__ == "__main__":
    cities_by_states()
