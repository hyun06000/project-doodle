import os
import re

from dotenv import load_dotenv

load_dotenv()


def trim_query(q):
    q = re.sub(r"\n", "", q)
    q = re.sub(r"[\s]+", " ", q)
    return q


envs = os.environ

mocking_table_name = envs["POSTGRES_TABLE"]

q_truncate_table = f"""
TRUNCATE TABLE IF EXISTS {mocking_table_name} CONTINUE IDENTITY RESTRICT;
"""

q_make_table = f"""
CREATE TABLE IF NOT EXISTS {mocking_table_name} (
    country VARCHAR(128) NOT NULL,
    entry_id SERIAL NOT NULL,
    date DATE NOT NULL,
    item_id SERIAL NOT NULL,
    item_unit_id SERIAL NOT NULL,
    price_min FLOAT8 NOT NULL,
    price_max FLOAT8 NOT NULL,
    price_avg FLOAT8 NOT NULL,
    currency VARCHAR(128) NOT NULL,
    period VARCHAR(1) NOT NULL
);
"""


def gen_insert_data_query(table_name, data):
    q = f"INSERT INTO {table_name} ( "
    for i, column_name in enumerate(data.keys()):
        q += str(column_name)
        if i != len(data) - 1:
            q += ","
        q += " "

    q += ") VALUES ( "
    for i, value in enumerate(data.values()):
        if isinstance(value, str):
            q += f"'{value}'"
        else:
            q += str(value)
        if i != len(data) - 1:
            q += ","
        q += " "
    q += ");"

    return q
