curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
      "name": "jdbc_source_postgres_01",
      "config": {
              "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
              "connection.url": "jdbc:postgresql://<postgres-server-ip>:<port>/<database-name>",
              "connection.user": "<user-name>",
              "connection.password": "<password>",
              "topic.prefix": "",
              "table.whitelist": "<table1>, <table2>"
              }
      }'
