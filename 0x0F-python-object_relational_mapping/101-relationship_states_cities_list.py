#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the DB
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

    st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
