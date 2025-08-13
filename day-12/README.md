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
