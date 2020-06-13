import sys
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database(dbname, newdb, user, pwd, host_ip="127.0.0.1", port="5432"):
    # connect to default database
    conn = psycopg2.connect(f"host={host_ip} port={port} dbname={dbname} user={user} password={pwd}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create database with UTF8 encoding
    cur.execute(f"DROP DATABASE IF EXISTS {newdb}")
    cur.execute(f"CREATE DATABASE {newdb} WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to insightde database
    conn = psycopg2.connect(f"host={host_ip} port={port} dbname={newdb} user={user} password={pwd}")
    cur = conn.cursor()
    print(conn)
    
    return cur, conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    if len(sys.argv) == 7:
        dbname, newdb, user, pwd, host_ip, port= sys.argv[1:]

        cur, conn = create_database(dbname, newdb, user, pwd, host_ip, port)
        drop_tables(cur, conn)
        create_tables(cur, conn)

        conn.close()