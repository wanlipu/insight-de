import sys
import psycopg2
import pandas as pd
from helper import table_stats


def process_file(cur, conn, table, filepath):
    """
    process file in csv format, insert processed data into database
    
    Args:
        cur: cursor to the database
        conn: connection to the database
        table: table to insert data
        param filepath: filepath of a csv file
    
    Returns:
        None
    """

    taxi_table_insert = ("""
    INSERT INTO {} (trip_id, taxi_id, trip_sec, trip_mile)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (trip_id) 
    DO NOTHING;
    """.format(table))

    # open csv file
    # https://stackoverflow.com/questions/17444679/reading-a-huge-csv-file
    df = pd.read_csv(filepath)

    # df = df[['Trip ID', 'Taxi ID', 'Trip Start Timestamp', 'Trip End Timestamp', 'Trip Seconds', 'Trip Miles']]
    df = df[['Trip ID', 'Taxi ID', 'Trip Seconds', 'Trip Miles']]

    df.dropna(inplace=True)

    # insert trip records
    for index, row in df.iterrows():
        if (index+1) % 100 == 0:
            print(f"Inserting {index+1}th row...")
        cur.execute(taxi_table_insert, row)
        conn.commit()


if __name__ == "__main__":
    if len(sys.argv) == 8:
        # parse command line inputs
        dbname, user, pwd, host_ip, port, filepath, table = sys.argv[1:]

        conn = psycopg2.connect(f"host={host_ip} port={port} dbname={dbname} user={user} password={pwd}")
        cur = conn.cursor()
        
        process_file(cur, conn, table, filepath=filepath)
        table_stats(cur, table)
        
        cur.close()
        conn.close()
    else:
        print("Please check your inputs!")