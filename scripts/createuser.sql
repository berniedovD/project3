CREATE USER 'appdbuser'@'%' IDENTIFIED BY 'tortola1';
GRANT ALL PRIVILEGES ON *.* TO 'appdbuser'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
