from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import relationship


from .database import Base

class User(Base):
    __tablename__ = "users"
    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True)
    name            = Column(String, default="")
    profile         = Column(String, default="")
    hashed_password = Column(String, default="")

    tweets = relationship("Tweet", back_populates="users")

class Tweet(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_tweet = Column(String)

    users = relationship("User", back_populates="tweets")