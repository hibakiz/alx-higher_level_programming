#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    lists all states from the database hbtn_0e_0_usa
    """
    arg = list(sys.argv)
    db = MySQLdb.connect(
        host="localhost", port=3306, user=arg[1], passwd=arg[2], db=arg[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
