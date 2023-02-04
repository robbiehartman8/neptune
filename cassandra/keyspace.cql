-- create keyspace command
CREATE KEYSPACE IF NOT EXISTS neptune WITH replication = {'class':'SimpleStrategy' , 'replication_factor' : 1};