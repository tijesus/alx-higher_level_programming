#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Take in state as arguement and return its list of cities"""

    db_connect = MySQLdb.connect()
