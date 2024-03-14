-- Create new useer for database
-- CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
-- GRANT PRIVILEGE ON database.table TO 'username'@'host';
-- PRIVILEGES: CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
