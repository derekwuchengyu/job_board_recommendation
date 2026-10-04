import os,sys
import numpy as np
import pandas as pd
from clickhouse_driver import Client
from clickhouse_driver import connect
from dotenv import load_dotenv
load_dotenv()

CH_HOST = os.getenv('CH_HOST', 'localhost')
CH_DB = os.getenv('CH_DB', 'recsys')
CH_SRC_PREFIX = os.getenv('CH_SRC_PREFIX', 'src_')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_DB = os.getenv('MYSQL_DB')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

client = Client(CH_HOST)
conn = connect('clickhouse://' + CH_HOST)
cursor = conn.cursor()

import time 


if __name__ == "__main__":
    print("開始匯入")
    db_names = ['job_basic','profile_basic','profile_condition','profile_description',
                'profile_experience','resume_submit_active','profile_match']

    total_start = time.time()
    for name in db_names:
        start = time.time()
        db_name = f"{CH_SRC_PREFIX}{name}"
               
        sql = f"DROP TABLE IF EXISTS  {CH_DB}.{db_name}"
        cursor.execute(sql)
        cursor.fetchall()
        sql =f"CREATE TABLE {CH_DB}.{db_name} ENGINE = ReplacingMergeTree  \
        ORDER BY id AS  \
        SELECT * FROM mysql('{MYSQL_HOST}', '{MYSQL_DB}', '{name}', '{MYSQL_USER}', '{MYSQL_PASSWORD}')"

        client.execute(sql)
        end = time.time()

        print("匯入:" ,db_name , ", 執行時間:" ,(end - start))
    print("總執行時間: (%.2f seconds)" %(time.time() - total_start))