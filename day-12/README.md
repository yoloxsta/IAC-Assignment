```
ubuntu@:~/Music-cost$ ls
Mail_Logs  generate_report.py  run_monthly_report.sh  send_email.py  venv
ubuntu@:~/Music-cost$

----

DB Migration
---

+------------------+           Backup/Restore           +------------------+
|     EC2 A        |  ----------------------------->   |     EC2 B        |
| Source DB: mydb  |   mydb_backup.dump               | Target DB: mydb  |
| User: myuser     |                                   | User: myuser     |
| Sample Data      |                                   | Restored Data    |
+------------------+                                   +------------------+

pg_migration_lab.sh >>

#!/bin/bash

# ============================
# CONFIGURATION
# ============================
SRC_DB="mydb"
SRC_USER="myuser"
SRC_PASS="mypassword"
SRC_IP="localhost"  # EC2 A

DST_DB="mydb"
DST_USER="myuser"
DST_PASS="mypassword"
DST_IP="10.0.0.2"   # EC2 B
SSH_KEY="mykey.pem" # for EC2 B
DST_USER_SSH="ubuntu"

BACKUP_FILE="mydb_backup.dump"

# ============================
# 1. Install PostgreSQL on SOURCE (EC2 A)
# ============================
sudo apt update
sudo apt install -y postgresql postgresql-contrib
sudo systemctl enable postgresql
sudo systemctl start postgresql

# ============================
# 2. Create DB and user on SOURCE
# ============================
sudo -i -u postgres psql -c "CREATE USER $SRC_USER WITH PASSWORD '$SRC_PASS';"
sudo -i -u postgres psql -c "CREATE DATABASE $SRC_DB OWNER $SRC_USER;"

# ============================
# 3. Create table and insert data
# ============================
sudo -i -u postgres psql -d $SRC_DB -c "
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);
INSERT INTO employees (name, department, salary) VALUES
('Alice', 'IT', 5000),
('Bob', 'HR', 4000),
('Charlie', 'Finance', 4500)
ON CONFLICT DO NOTHING;
"

# ============================
# 4. Backup DB
# ============================
sudo -i -u postgres pg_dump -U $SRC_USER -F c $SRC_DB > $BACKUP_FILE

# ============================
# 5. Transfer backup to DESTINATION (EC2 B)
# ============================
scp -i $SSH_KEY $BACKUP_FILE $DST_USER_SSH@$DST_IP:/home/$DST_USER_SSH/

# ============================
# 6. Install PostgreSQL on DESTINATION (EC2 B) via SSH
# ============================
ssh -i $SSH_KEY $DST_USER_SSH@$DST_IP << EOF
sudo apt update
sudo apt install -y postgresql postgresql-contrib
sudo systemctl enable postgresql
sudo systemctl start postgresql

sudo -i -u postgres psql -c "CREATE USER $DST_USER WITH PASSWORD '$DST_PASS';"
sudo -i -u postgres psql -c "CREATE DATABASE $DST_DB OWNER $DST_USER;"

# ============================
# 7. Restore DB
# ============================
sudo -i -u postgres pg_restore -U $DST_USER -d $DST_DB -1 /home/$DST_USER_SSH/$BACKUP_FILE

# ============================
# 8. Verify data
# ============================
sudo -i -u postgres psql -d $DST_DB -c "SELECT * FROM employees;"

EOF

echo "Migration completed! ✅"

---
chmod +x pg_migration_lab.sh
./pg_migration_lab.sh

```

## Db migration between 2 containers

```
docker-compose.yml

version: "3.9"
services:
  pgsrc:
    image: postgres:15
    container_name: pgsrc
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydb
    networks:
      - pgnet
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser"]
      interval: 5s
      retries: 5

  pgtgt:
    image: postgres:15
    container_name: pgtgt
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydb
    networks:
      - pgnet
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser"]
      interval: 5s
      retries: 5

networks:
  pgnet:
    driver: bridge

---

migrate.sh >>

#!/bin/bash
set -e

echo "🚀 Starting containers..."
docker compose up -d

echo "⏳ Waiting for PostgreSQL containers to be ready..."
sleep 10

echo "📦 Creating table and inserting data into Source DB..."
docker exec -i pgsrc psql -U myuser -d mydb <<EOF
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);
INSERT INTO employees (name, department, salary) VALUES
('Alice', 'IT', 5000),
('Bob', 'HR', 4000),
('Charlie', 'Finance', 4500);
EOF

echo "✅ Source DB data:"
docker exec pgsrc psql -U myuser -d mydb -c "SELECT * FROM employees;"

echo "💾 Backing up data from Source DB..."
docker exec pgsrc pg_dump -U myuser -F c mydb > mydb_backup.dump

echo "📤 Restoring backup into Target DB..."
cat mydb_backup.dump | docker exec -i pgtgt pg_restore -U myuser -d mydb

echo "🔍 Target DB data after migration:"
docker exec pgtgt psql -U myuser -d mydb -c "SELECT * FROM employees;"

echo "🎉 Migration complete!"

```

## cron

```
/opt/pg_backup.sh

#!/bin/bash
DATE=$(date +%F)
BACKUP_DIR="/opt/pg_backups"
mkdir -p $BACKUP_DIR

docker exec pgsrc pg_dump -U myuser -F c mydb > $BACKUP_DIR/mydb_$DATE.dump

# Optional: remove backups older than 30 days
find $BACKUP_DIR -type f -mtime +30 -delete

```
