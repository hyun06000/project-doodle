import os
import argparse
import time
import pandas as pd

from utils.tools import upload_mocking_db
from utils.async_tools import async_upload_mocking_db

from dotenv import load_dotenv
load_dotenv()

def get_args():
    parser = argparse.ArgumentParser(description='Upload Data to mocking DB.')
    parser.add_argument(
        "-f",
        '--fraction', 
        type=float,
        default=0.1,
        help='how many ratio of data you want to update'
    )
    parser.add_argument(
        "-A",
        '--asyncio', 
        type=bool,
        default=False,
        help='how many ratio of data you want to update'
    )
    args = parser.parse_args()
    return args


def main():
    envs = os.environ

    args = get_args()
    chunk_size = 10000
    df = pd.read_csv("./sparse_truncated_data.csv")
    top_three_country_df = df[df["country"].isin(["India","Taiwan","China"])]
    
    top_three_country_df = top_three_country_df.\
        sample(frac=args.fraction, random_state=227)
    
    print("::::: pandas head :::::")
    print(top_three_country_df.head())
    print(f"::::: pandas df_lan = {len(top_three_country_df)} :::::")

    if args.asyncio:
        async_upload_mocking_db(envs, top_three_country_df, chunk_size)
    else:
        upload_mocking_db(envs, top_three_country_df, chunk_size)
    
    print("`upload_mocking_db.py` is done")
    
if __name__ == "__main__":
    tic = time.time()
    main()
    toc = time.time()
    print("time to run main ::: ", toc-tic)
