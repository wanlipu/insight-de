curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
      "name": "jdbc_sink_redshift_01",
      "config": {
              "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
              "connection.url": "jdbc:redshift://<url>:<port>/<database-name>",
              "connection.user": "<user-name>",
              "connection.password": "<password>",
              "topics": "<topic1>, <topic2>",
	      "auto.create": "true"
              }
      }'
