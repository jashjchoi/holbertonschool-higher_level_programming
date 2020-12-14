#!/usr/bin/python3
"""takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa
   where name matches the argument"""
import MySQLdb
import sys


def filter_states():
    """takes 4 arguments argv to list from db
    Only lists with states that matches the argument
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name searched
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    """creates a cursor and executes query"""
    cur = db.cursor()

    cur.execute("SELECT * FROM states\
                WHERE BINARY name='{:s}'\
                ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for i in rows:
        print(i)

    """closes cursor and db"""
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
