import sys
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def connect_database(newdb, user, pwd, host_ip="127.0.0.1", port="5432"):
    """
    create a new database on postgres server on aws
    
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

    # # connect to default database
    # conn = psycopg2.connect(f"host={host_ip} port={port} dbname={dbname} user={user} password={pwd}")
    # conn.set_session(autocommit=True)
    # cur = conn.cursor()
    
    # # create database with UTF8 encoding
    # cur.execute(f"DROP DATABASE IF EXISTS {newdb}")
    # cur.execute(f"CREATE DATABASE {newdb} WITH ENCODING 'utf8' TEMPLATE template0")

    # # close connection to default database
    # conn.close()    
    
    # connect to insightde database
    conn = psycopg2.connect(f"host={host_ip} port={port} dbname={newdb} user={user} password={pwd}")
    cur = conn.cursor()
    print(conn)
    
    return cur, conn


def drop_tables(cur, conn):
    """
    drop tables in the database
    
    Args:
        cur: cursor to the database
        conn: connection to the database
    
    Returns:
        None
    """

    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    create tables in the database
    
    Args:
        cur: cursor to the database
        conn: connection to the database
    
    Returns:
        None
    """

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def query(cur):

    cur.execute("SELECT count(*) FROM taxi;")
    
    for result in cur.fetchall():
        print(f'There are {result[0]} rows in the table')

    # cur.execute("SELECT COUNT(DISTINCT(trip_id)) FROM taxi;")
    
    # for result in cur.fetchall():
    #     print(f'There are {result[0]} distinct trips')

    cur.execute("SELECT COUNT(DISTINCT(taxi_id)) FROM taxi;")
    
    for result in cur.fetchall():
        print(f'There are {result[0]} distinct taxi')

    cur.execute("SELECT SUM(trip_mile) FROM taxi;")
    
    for result in cur.fetchall():
        print(f'Sum of all trip distance is {result[0]}')

    cur.execute("SELECT SUM(trip_sec) FROM taxi;")
    
    for result in cur.fetchall():
        print(f'Sum of all trip time is {result[0]} secs')

def close_connection(conn, cur):
    cur.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) == 6:
        # parse command line inputs
        dbname, user, pwd, host_ip, port= sys.argv[1:]

        cur, conn = connect_database(dbname, user, pwd, host_ip, port)

        # drop_tables(cur, conn)
        # create_tables(cur, conn)

        query(cur)

        close_connection(conn, cur)
    else:
        print("Please check your inputs!")