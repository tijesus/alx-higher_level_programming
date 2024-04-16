#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Print out state name passed from command line."""

    db_connect = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2],
        db=argv[3]
    )
    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    states = db_cursor.fetchall()
    for state in states:
        print(state)
