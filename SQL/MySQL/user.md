# user

## diff between localhost and 127.0.0.1
when you use localhost, the socket connector is used (port is not used). Whereas, when you use 127.0.0.1, TCP/IP connector is used.

## show grants
  SHOW GRANTS; #for current user
  SHOW GRANTS FOR 'user_name';
  SHOW GRANTS FOR 'root'@'localhost';
  SHOW GRANTS FOR 'root'@'%';
  SHOW GRANTS FOR 'admin'@'192.168.0.1';
  
## create user
  CREATE USER 'usr'@'%' IDENTIFIED BY 'new_password';
  GRANT ALL PRIVILEGES ON *.* TO 'usr'@'%';
  GRANT ALL PRIVILEGES ON db.* TO 'usr'@'%'; 
  FLUSH PRIVILEGES;
  
  #new version
  GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE ON *.* TO `usr`@`%` WITH GRANT OPTION;
 
  
## delete user
  DROP USER 'usr'@'%';
  
## select user
  SELECT user FROM mysql.user
  
## change password
  UPDATE mysql.user SET Password=PASSWORD('pwd') WHERE User='usr' and Host='%';
  FLUSH PRIVILEGES; 