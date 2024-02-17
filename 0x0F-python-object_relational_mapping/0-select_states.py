#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

arg = list(sys.argv)
db = MySQLdb.connect(user=arg[1], password=arg[2], database=arg[3])
cursor = db.cursor()
cursor.execute("""SELECT * FROM states ORDER BY id ASC;""")
i = 0
for row in cursor:
    print(row)
