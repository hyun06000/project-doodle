from sqlalchemy import create_engine

from .query import mocking_table_name


def upload_mocking_db(envs, df, chunk_size):
    host = envs["PG_HOST"]
    port = envs["PG_PORT"]
    user = envs["POSTGRES_USER"]
    database = envs["POSTGRES_DB"]
    password = envs["POSTGRES_PASSWORD"]

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )
    df.to_sql(mocking_table_name, engine, if_exists="replace", chunksize=chunk_size)
