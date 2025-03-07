#!/usr/bin/python3
"""
In this task we will delete all State starting by `a`
from the database `hbtn_0e_6_usa`
"""
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    state = session.query(State).filter(
            State.name.like('%a%')
            ).delete()
    session.commit()

    session.close()
