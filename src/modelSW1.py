import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250),nullable=False)
    lastname = Column(String(250),nullable=False)
    email = Column(String(200),nullable=False)
    password = Column(String,nullable=False)


class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey(User.id))
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    planet = Column(String(40), ForeignKey('planet.id'))
    person = Column(String(25), ForeignKey('person.id'))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    birth_year = Column(Date, nullable=False)
    homeworld = Column(String(50), ForeignKey('planet.id'))
    eye_color = Column(String(10))
    gender = Column(String(15))
    hair_color = Column(String(20))
    height = Column(Integer)
    mass = Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagramSW1.png')