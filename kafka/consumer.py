from time import sleep
from json import dumps, loads
from kafka import KafkaConsumer
import cassandra
from cassandra.cluster import Cluster


if __name__ == "__main__":

if len(sys.argv) == 6:
    
    bootstrap_servers = sys.argv[1:4] # xxx.xxx.xx.xxx:9092, .., ..
    topic = sys.argv[4]
    cassandra_hosts = [5:]

    consumer = KafkaConsumer(
        topic = topic,
        bootstrap_servers = bootstrap_servers,
        auto_offset_reset = "earliest",
        enable_auto_commit = True,
        group_id = "cassandra"
        )
    
    # cluster = Cluster(cassandra_hosts)
    # session = cluster.connect()

    count = 0
    for message in consumer:
        message = message.value
        print(count)
        print(message)
        count += 1

        if count == 100:
            break

    # session.shutdown()
    # cluster.shutdown()


    


