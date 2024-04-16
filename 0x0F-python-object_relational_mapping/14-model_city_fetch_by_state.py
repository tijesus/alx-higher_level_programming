#!/usr/bin/python3
"""
This script that lists all cities
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from model_city import State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Cheacking the database"""
    db_path = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_path)
    Session = sessionmaker(bind=engine)

    session = Session()

    states_cities = session.query(City, State).join(State).all()
    for city, state in states_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
