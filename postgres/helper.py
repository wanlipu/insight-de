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