import sys
import psycopg2
from helper import connect_database, process_file, table_stats


if __name__ == "__main__":
    if len(sys.argv) == 8:
        # parse command line inputs
        dbname, user, pwd, host_ip, port, filepath, table = sys.argv[1:]

        # connect to database
        cur, conn = connect_database(dbname, user, pwd, host_ip, port)

        # load data
        process_file(cur, conn, table, filepath=filepath)
        
        print('*****PostgreSQL****')
        table_stats(cur, table)
        print('*******************')

        cur.close()
        conn.close()
    else:
        print("Please check your inputs!")