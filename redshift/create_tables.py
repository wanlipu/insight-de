import sys
import psycopg2


def connect_database(dbname, user, pwd, host_ip, port="5439"):
    """
    create a new database on redshift cluster
    
    Args:
        dbname: database name to connect to server
        user: user name
        pwd: user password
        host_ip: ip for database server
        port: port for database server
    
    Returns:
        cur: cursor to the database
        conn: connection to the database
    """

    # connect to default database
    conn = psycopg2.connect(f"host={host_ip} port={port} dbname={dbname} user={user} password={pwd}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
        
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
    (id int PRIMARY KEY,
     trip_id text, 
     taxi_id text,
     trip_sec int,
     trip_mile float)
     """.format(table))
     
    cur.execute(query)
    conn.commit()


def table_stats(cur, table):
    """
    output table stats in the database
    
    Args:
        cur: cursor to the database
        table: table to be queried
    
    Returns:
        None
    """

    cur.execute(f"SELECT count(*) FROM {table};")
    
    for result in cur.fetchall():
        print(f'There are {result[0]} rows in the table')

    cur.execute(f"SELECT COUNT(DISTINCT(trip_id)) FROM {table};")
    
    for result in cur.fetchall():
        print(f'There are {result[0]} distinct trips')

    cur.execute(f"SELECT COUNT(DISTINCT(taxi_id)) FROM {table};")
    
    for result in cur.fetchall():
        print(f'There are {result[0]} distinct taxi')

    cur.execute(f"SELECT SUM(trip_mile) FROM {table};")
    
    for result in cur.fetchall():
        print(f'Sum of all trip distance is {result[0]}')

    cur.execute(f"SELECT SUM(trip_sec) FROM {table};")
    
    for result in cur.fetchall():
        print(f'Sum of all trip time is {result[0]}')


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

        cur.close()
        conn.close()

    else:
        print("Please check your inputs!")

    