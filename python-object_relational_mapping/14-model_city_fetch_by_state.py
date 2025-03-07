#!/usr/bin/python3
"""
In this task we will delete all State starting by `a`
from the database `hbtn_0e_6_usa`
"""
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    engine = sa.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
        )

    conn = engine.connect()
    Session = sessionmaker(bind=conn)
    session = Session()

    state_city = session.query(State, City)\
        .filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in state_city:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
