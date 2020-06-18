# DROP TABLES

taxi_table_drop = "DROP TABLE IF EXISTS taxi"


# CREATE TABLES

taxi_table_create = ("""
    CREATE TABLE taxi
    (trip_id text PRIMARY KEY, 
     taxi_id text,
     trip_sec int,
     trip_mile float)
""")


# INSERT RECORDS

taxi_table_insert = ("""
    INSERT INTO taxi (trip_id, taxi_id, trip_sec, trip_mile)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (trip_id) 
    DO NOTHING;
""")

# QUERY LISTS

create_table_queries = [taxi_table_create]
drop_table_queries = [taxi_table_drop]