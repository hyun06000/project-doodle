from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "{driver}://{user}:{pswd}@{host}:{port}/{dbname}"

engine = create_engine(
    SQLALCHEMY_DB_URL.format(
        driver="postgresql+psycopg2",
        user="mockingUSER",
        pswd="mockingPSWD",
        host="127.0.0.1",
        port="6543",
        dbname="mockingDB"
    )
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()