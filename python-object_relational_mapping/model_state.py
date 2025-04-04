#!/usr/bin/python3
"""
contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    This is the state class
    """
    __tablename__ = 'states'

    id = Column('id', Integer(),
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column('name', String(128), nullable=False)
