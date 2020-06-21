import sys
import psycopg2
from query_tables import connect_database, table_stats, close_connection


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
    (id int PRIMARY KEY,
     trip_id text, 
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

        cur, conn = create_database(dbname, user, pwd, host_ip, port)

        drop_tables(cur, conn, table)
        create_tables(cur, conn, table)

        print('******RedShift*****')
        table_stats(cur, table)
        print('*******************')

        close_connection(conn, cur)

    else:
        print("Please check your inputs!")

    