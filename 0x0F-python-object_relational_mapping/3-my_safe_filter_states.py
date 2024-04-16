#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Print out state name passed from command line."""

    state_name = argv[4]
    db_connect = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2],
        db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = db_cursor.fetchall()
    for state in states:
        if state[1] == state_name:
            print(state)
