import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from tqdm import tqdm

from .query import (gen_insert_data_query, mocking_table_name, q_make_table,
                    trim_query)


async def send_query_to_db(engine, data):
    async with engine.connect() as conn:
        q_insert_data = gen_insert_data_query(mocking_table_name, data=data)
        q_insert_data = trim_query(q_insert_data)
        await conn.execute(text(q_insert_data))
        await conn.commit()


async def _async_upload_mocking_db(envs, df):
    global q_make_table

    host = envs["PG_HOST"]
    port = envs["PG_PORT"]
    user = envs["POSTGRES_USER"]
    database = envs["POSTGRES_DB"]
    password = envs["POSTGRES_PASSWORD"]

    engine = create_async_engine(
        f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"
    )
    async with engine.begin() as conn:
        q_make_table = trim_query(q_make_table)
        await conn.execute(text(q_make_table))
        await conn.commit()

    coro = []
    for i in range(len(df)):
        raw_dict = dict(df.iloc[i])
        coro.append(send_query_to_db(engine, data=raw_dict))

    await asyncio.gather(*coro)
    await engine.dispose()


def async_upload_mocking_db(envs, df, chunk_size):

    div, mod = divmod(len(df), chunk_size)
    total_chunks = div + int(bool(mod))
    for i in tqdm(list(range(total_chunks))):
        asyncio.run(
            _async_upload_mocking_db(
                envs, df.iloc[i * chunk_size : (i + 1) * chunk_size]
            )
        )
