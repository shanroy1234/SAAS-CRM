
from sqlalchemy import Column,Integer,String,ForeignKey
from app.database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String,unique=True)

class Lead(Base):
    __tablename__='leads'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    status=Column(String)
    owner_id=Column(Integer,ForeignKey('users.id'))
