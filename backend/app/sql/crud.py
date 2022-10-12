from sqlalchemy.orm import Session

from . import schemas, models

def get_user_by_email(db: Session, user_email: str):
    user = db.query(schemas.User)\
            .filter(schemas.User.email == user_email)\
            .first()
    return user

def create_user(db: Session, user:models.UserCreate):
    hashed_password = user.hashed_password
    db_user = schemas.User(
        name=user.name,
        email=user.email,
        profile=user.profile, 
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_new_tweet(db: Session, new_tweet: models.TweetCreate):
    db_new_tweet = schemas.Tweet(
        user_id=new_tweet.user_id,
        user_tweet=new_tweet.user_tweet
    )
    db.add(db_new_tweet)
    db.commit()
    db.refresh(db_new_tweet)
    return db_new_tweet
