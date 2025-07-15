### Day-10 (PHP-Docker-Nginx-Mysql)

```
docker exec -it mysql-container mysql -u root -p

>> secret

USE mydb;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
);

INSERT INTO users (name, email) VALUES ('Soe Tint Aung', 'soe@example.com');

Then, http://localhost:8080, refresh
```