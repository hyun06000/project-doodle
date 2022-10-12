from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from sql import crud
from sql import models
from sql import schemas
from sql.database import engine, SessionLocal, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sign-up/", response_model=models.User)
def create_user(
    user: models.UserCreate,
    db: Session=Depends(get_db)
):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return crud.create_user(db, user)

@app.post("/tweet/", response_model=models.Tweet)
def create_tweet(
    new_tweet: models.TweetCreate,
    db: Session=Depends(get_db)
):
    return crud.create_new_tweet(db, new_tweet)