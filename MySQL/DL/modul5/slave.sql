CHANGE MASTER TO 
MASTER_HOST='localhost',
MASTER_USER='replication_user',
MASTER_PASSWORD='12345678',
MASTER_PORT=3307,
MASTER_LOG_FILE='mysql-bin.000002',
MASTER_LOG_POS=154,
MASTER_CONNECT_RETRY=60;

stop slave;
start slave;

SELECT * FROM replicationdb.simples;