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

---

```
| Config File        | Purpose                                                         |
| ------------------ | --------------------------------------------------------------- |
| `nginx.conf`       | Configures web server behavior                                  |
| `fpm-pool.conf`    | Configures PHP-FPM process pool                                 |
| `php.ini`          | Configures PHP runtime settings                                 |
| `supervisord.conf` | Manages and runs nginx & php-fpm processes inside the container |

```