#!/usr/bin/python3

import MySQLdb
from sys import argv
if __name__ == '__main__':
    """List all cities in the database"""

    state_name=argv[4]
    db_connect = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2],
        db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name \
                            FROM cities JOIN states ON cities.state_id \
                            = states.id ORDER BY cities.id ASC")
    cities_states = db_cursor.fetchall()
    if cities_states is not None:
        for city_state in cities_states:
            print(city_state)

