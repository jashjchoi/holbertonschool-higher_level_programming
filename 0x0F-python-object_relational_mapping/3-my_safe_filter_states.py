#!/usr/bin/python3
"""Displays name argument of states table
   that is safe from MySQL injections"""
import MySQLdb
import sys


def main():
    """takes 4 arguments argv to list from db
    Only lists with states that matches the argument
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name searched
    """
    if len(sys.argv) == 5:
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
    else:
        return


if __name__ == "__main__":
    main()
