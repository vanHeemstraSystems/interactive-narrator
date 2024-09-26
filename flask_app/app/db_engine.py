#!/usr/bin/env python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# create the database
engine = create_engine('sqlite:///app.db', echo=True)

