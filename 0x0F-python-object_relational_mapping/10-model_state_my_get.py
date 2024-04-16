#!/usr/bin/python3
"""
This script that lists all states
passed from commandline in `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Cheacking the database to get state"""

    db_path = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_path)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name == argv[4]).first()
    if states is not None:
        print('{0}'.format(states.id))
    else:
        print("Not found")