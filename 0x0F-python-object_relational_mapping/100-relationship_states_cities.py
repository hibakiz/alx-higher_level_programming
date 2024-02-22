#!/usr/bin/python3
"""
Task 100
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

    cal_state = State(name='California')
    san_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
