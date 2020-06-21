import psycopg2
import pandas as pd


def connect_database(dbname, user, pwd, host_ip="127.0.0.1", port="5432"):
    """
    connect to database on postgres server on aws
    
    Args:
        dbname: name of the database which is to be created
        user: user name
        pwd: user password
        host_ip: ip for database server
        port: port for database server
    
    Returns:
        cur: cursor to the database
        conn: connection to the database
    """
    
    # connect to database
    conn = psycopg2.connect(f"host={host_ip} port={port} dbname={dbname} user={user} password={pwd}")
    cur = conn.cursor()
    
    return cur, conn


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
    VALUES (%s, %s, %s, %s);
    """.format(table))

    # open csv file
    # https://stackoverflow.com/questions/17444679/reading-a-huge-csv-file
    df = pd.read_csv(filepath)

    df = df[['Trip ID', 'Taxi ID', 'Trip Seconds', 'Trip Miles']]

    df.dropna(inplace=True)

    # insert trip records
    for index, row in df.iterrows():
        cur.execute(taxi_table_insert, row)
        conn.commit()


def table_stats(cur, table):
    """
    generate table stats
    
    Args:
        cur: cursor to the database
        table: table to be queried
    
    Returns:
        stats: list for table stats
    """

    stats = []

    cur.execute(f"SELECT count(*) FROM {table};")
    
    for result in cur.fetchall():
        stats.append(result[0])
        print(f'There are {result[0]} rows in the table')

    cur.execute(f"SELECT COUNT(DISTINCT(trip_id)) FROM {table};")
    
    for result in cur.fetchall():
        stats.append(result[0])
        print(f'There are {result[0]} distinct trips')

    cur.execute(f"SELECT COUNT(DISTINCT(taxi_id)) FROM {table};")
    
    for result in cur.fetchall():
        stats.append(result[0])
        print(f'There are {result[0]} distinct taxi')

    cur.execute(f"SELECT SUM(trip_mile) FROM {table};")
    
    for result in cur.fetchall():
        stats.append(result[0])
        print(f'Sum of all trip distance is {result[0]}')

    cur.execute(f"SELECT SUM(trip_sec) FROM {table};")
    
    for result in cur.fetchall():
        stats.append(result[0])
        print(f'Sum of all trip time is {result[0]}')
    
    return stats