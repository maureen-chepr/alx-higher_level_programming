#!/usr/bin/python3
"""
links to the MySQL table states
"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, host, database = sys.argv[1:5]
    statement = 'mysql+mysqldb://{}:{}@{}/{}'.format(username, password, host, database)
    engine = create_engine(statement, pool_pre_ping=True)
    Base.metadata.create_all(engine)
