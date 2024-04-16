#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Take in state as arguement and return its list of cities"""

    db_connect = MySQLdb.connect(host="localHost", port=3306,
                                 user=argv[1], password=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
                FROM `cities`\
                INNER JOIN `states`\
                   ON `cities`.`state_id` = `states`.`id` \
                ORDER BY `cities`.`id`")
    city = db_cursor.fetchall()
    for city in city:
        print(city)
