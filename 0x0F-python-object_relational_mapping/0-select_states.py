#!/usr/bin/python3
"""lists all states from database hbtn_0e_0_usa"""
import MySQLdb
import sys


def get_states():
    """takes 3 arguments to list from db
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)

    """closes cursor and db"""
    cur.close()
    db.close()

if __name__ == "__main__":
    get_states()
