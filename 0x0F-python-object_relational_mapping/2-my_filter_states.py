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
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3])
    cursor = db.cursor()
    qury = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cursor.execute(qury)
    for row in cursor:
        print(row)
