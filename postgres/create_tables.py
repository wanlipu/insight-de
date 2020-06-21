import sys
import psycopg2
from helper import process_file, table_stats


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
    (id SERIAL PRIMARY KEY,
     trip_id text, 
     taxi_id text,
     trip_sec int,
     trip_mile float)
     """.format(table))

    cur.execute(query)
    conn.commit()


if __name__ == "__main__":
    if len(sys.argv) == 8:
        # parse command line inputs
        dbname, user, pwd, host_ip, port, table, filepath = sys.argv[1:]

        # connect to database
        cur, conn = connect_database(dbname, user, pwd, host_ip, port)

        # drop table and create table
        drop_tables(cur, conn, table)
        create_tables(cur, conn, table)

        # load sample data
        process_file(cur, conn, table, filepath=filepath)

        print('*****PostgreSQL****')
        table_stats(cur, table)
        print('*******************')

        cur.close()
        conn.close()

    else:
        print("Please check your inputs!")