from sqlalchemy import Column,Integer,String
from database import Base
from sqlalchemy.sql import func


class user(Base):
    # email id password_hash 
    __tablename__ = "users"
    id = Column(Integer, primary_key =True , index =True)
    email = Column(String, unique =True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)