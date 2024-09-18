
#!/usr/bin/python3
"""
Contains class City
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    state_id = Column(Integer, ForeignKey('states.id'))
