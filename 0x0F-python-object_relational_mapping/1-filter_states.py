#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """List states starting  with N"""

    db_connect = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], password=argv[2], db=argv[3]
    )

    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states ORDER BY states.id ASC")

    states = db_cursor.fetchall()

    for state in states:
        """ getting the first character of the state
            if s = {1, "Nevad"} to access first character
            s[1] targets Nevad and s[0] targets N
            :. s[1][0] == N
        """
        if state[1][0] == "N":
            print(state)
