#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
import sys


def get_n_states():
    """Takes 3 arguments argv to list from db
    Only lists with states that start with N
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

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()
    for i in rows:
        print(i)

    """closes cursor and db"""
    cur.close()
    db.close()

if __name__ == "__main__":
    get_n_states()
