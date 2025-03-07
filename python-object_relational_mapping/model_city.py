#!/usr/bin/python3
"""
contains the class definition of a City
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base


Base = declarative_base()


class City(Base):
    """
    This is the city class
    """
    __tablename__ = 'cities'

    id = Column('id', Integer(),
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer(),
                      ForeignKey('states.id'),
                      nullable=False)
