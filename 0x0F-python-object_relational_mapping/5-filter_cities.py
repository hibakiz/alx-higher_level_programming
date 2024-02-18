#!/usr/bin/python3
"""
lists all states starts with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    lists all states from the database hbtn_0e_0_usa
    """
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cursor = db.cursor()
    qury = "SELECT cities.id, cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name LIKE BINARY '{}'".format(argv[4])
    cursor.execute(qury)
    print(", ".join([row[1] for row in cursor]))
