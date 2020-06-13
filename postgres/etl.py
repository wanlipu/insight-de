import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_file(cur, conn, filepath):
    """
    process file in csv format
    
    Args:
        cur: cursor to the database
        conn: connection to the database
        param filepath: filepath of a csv file
    
    Returns:
        None
    """

    # open csv file
    # https://stackoverflow.com/questions/17444679/reading-a-huge-csv-file
    df = pd.read_csv(filepath)

    df = df[['Trip ID', 'Taxi ID', 'Trip Start Timestamp', 'Trip End Timestamp', 'Trip Seconds', 'Trip Miles']]
    df.dropna(inplace=True)

    # insert trip records
    for index, row in df.iterrows():
        if (index+1) % 100 == 0:
            print(f"Inserting {index+1}th row...")
        cur.execute(taxi_table_insert, row)
        conn.commit()


if __name__ == "__main__":
    if len(sys.argv) == 7:
        # parse command line inputs
        dbname, user, pwd, host_ip, port, filepath= sys.argv[1:]

        conn = psycopg2.connect(f"host={host_ip} port={port} dbname={dbname} user={user} password={pwd}")
        cur = conn.cursor()
        
        process_file(cur, conn, filepath=filepath)
        
        conn.close()
    else:
        print("Please check your inputs!")