#!/usr/bin/python3

"""
This is a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=arg[1],
        passwd=arg[2], db=arg[3],
        charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
        """SELECT *
        FROM states
        ORDER BY id ASC"""
        )
    state_rows = cur.fetchall()
    for state in state_rows:
        if (state[1][0] == 'N'):
            print(state)
    cur.close()
    conn.close()