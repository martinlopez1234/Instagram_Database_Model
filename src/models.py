import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    bio = Column(String(250), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    photo = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at= Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    accepted = Column(String(250), nullable=False)
 
class Likes(Base):
    __tablename__ = 'likes'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) 
    post_id = Column(Integer, ForeignKey("posts.id"))

class Comments(Base):
    __tablename__ = 'comments'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) 
    post_id = Column(Integer, ForeignKey("posts.id"))
    content = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at= Column(String(250), nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')