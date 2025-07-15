#!/bin/bash

# Start MySQL service
service mysql start

# Initialize database if needed (optional)
# mysql -e "CREATE DATABASE IF NOT EXISTS mydb;"
# mysql -e "CREATE USER IF NOT EXISTS 'myuser'@'localhost' IDENTIFIED BY 'password';"
# mysql -e "GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'localhost';"
# mysql -e "FLUSH PRIVILEGES;"

# Start PHP-FPM service
service php7.0-fpm start

# Start Nginx service
nginx -g "daemon off;"
