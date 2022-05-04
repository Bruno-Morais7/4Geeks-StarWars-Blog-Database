import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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
    email = Column(String(200))

class Login(Base):
    __tablename__ = 'login'
    id = Column(String, ForeignKey('user.email'), primary_key=True)
    password = Column()
    login = relationship(User)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    favorites = relationship(User)
    

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    comment = relationship(Favorites)

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(String(50))
    terrain = Column(String(50))
    comment = relationship(Favorites)

    def to_dict(self):
        return {"name": self.name}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')