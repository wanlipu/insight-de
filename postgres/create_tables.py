import sys
import psycopg2
from helper import table_stats


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
    # print(conn)
    
    return cur, conn


def drop_tables(cur, conn, table):
    """
    drop tables in the database
    
    Args:
        cur: cursor to the database
        conn: connection to the database
        table: table to be dropped
    
    Returns:
        None
    """

    query = "DROP TABLE IF EXISTS {};"

    cur.execute(query.format(table))
    conn.commit()


def create_tables(cur, conn, table):
    """
    create tables in the database
    
    Args:
        cur: cursor to the database
        conn: connection to the database
        table: table to be created
    
    Returns:
        None
    """

    query = ("""
    CREATE TABLE {}
    (trip_id text PRIMARY KEY, 
     taxi_id text,
     trip_sec int,
     trip_mile float)
     """.format(table))

    cur.execute(query)
    conn.commit()


if __name__ == "__main__":
    if len(sys.argv) == 7:
        # parse command line inputs
        dbname, user, pwd, host_ip, port, table = sys.argv[1:]

        cur, conn = connect_database(dbname, user, pwd, host_ip, port)

        drop_tables(cur, conn, table)
        create_tables(cur, conn, table)

        table_stats(cur, table)

        cur.close()
        conn.close()

    else:
        print("Please check your inputs!")