#!/usr/bin/python3
"""
lists all states starts with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    lists all states from the database hbtn_0e_0_usa
    """
    username = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(f"mysql+mysqldb://{username}:\
                            {password}@localhost:3306/{db}")
    Base.metadata.bind = engine
    dbsession = sessionmaker(bind=engine)
    session = dbsession()
    cities = session.query(City, State).join(State)

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
