# Use Ubuntu 20.04 base image
FROM ubuntu:20.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install required packages
RUN apt-get update && apt-get install -y \
    nginx \
    mysql-server \
    php7.4-fpm \
    php7.4-mysql \
    php7.4-cli \
    php7.4-mbstring \
    php7.4-common \
    php7.4-pdo \
    php7.4-curl \
    php7.4-xml \
    php7.4-json \
    curl \
    supervisor \
    && apt-get clean

# Configure MySQL (simple config for demo)
RUN service mysql start && \
    mysql -e "CREATE DATABASE IF NOT EXISTS mydb;" && \
    mysql -e "CREATE USER 'myuser'@'%' IDENTIFIED BY 'password';" && \
    mysql -e "GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'%';" && \
    mysql -e "FLUSH PRIVILEGES;"

# Copy Nginx default site config
COPY nginx-default.conf /etc/nginx/sites-available/default

# Copy your PHP code into container (adjust your path accordingly)
COPY www/html/ /var/www/html/

# Set permissions for www data
RUN chown -R www-data:www-data /var/www/html

# Supervisor config to run both services
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports for Nginx and MySQL
EXPOSE 80 3306

# Start supervisor (will start nginx, php-fpm, and mysql)
CMD ["/usr/bin/supervisord", "-n"]
