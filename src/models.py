import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person) """

class User(Base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Naves(Base):
    __tablename__= "naves"
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__= "personajes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    estatura = Column(Integer, nullable=True)
    color_ojos = Column(String(100), nullable=True)

class Planetas(Base):
    __tablename__= "planetas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    population = Column(Integer, nullable=True)
    gravity = Column(Integer, nullable=True)

class Favoritos_Naves(Base):
    __tablename__= "favoritos_naves"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_nave = Column(Integer, ForeignKey('naves.id'))

class Favoritos_Planetas(Base):
    __tablename__= "favoritos_planetas"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_planeta = Column(Integer, ForeignKey('planetas.id'))

class Favoritos_Personajes(Base):
    __tablename__= "favoritos_personajes"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_personaje = Column(Integer, ForeignKey('personajes.id'))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')