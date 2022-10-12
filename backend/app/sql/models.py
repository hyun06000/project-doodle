from pydantic import BaseModel


class UserBase(BaseModel):
    email:str
    name:str
    profile:str

class UserCreate(UserBase):
    hashed_password:str

class User(UserBase):
    id:int
    
    class Config:
        orm_mode = True


class TweetBase(BaseModel):
    user_id: int
    user_tweet: str

class TweetCreate(TweetBase):
    pass

class Tweet(TweetBase):
    id: int
    
    class Config:
        orm_mode = True