# 🗄️ SQL and PostgreSQL

## What is SQL?
SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. It allows users to perform operations such as querying, updating, and managing data.

### Common SQL Commands:
- **SELECT**: Retrieve data from a database.
- **INSERT**: Add new data to a table.
- **UPDATE**: Modify existing data.
- **DELETE**: Remove data from a table.
- **CREATE**: Create new tables or databases.
- **DROP**: Delete tables or databases.
- **JOIN**: Combine rows from two or more tables.

---

## 🐘 What is PostgreSQL?
PostgreSQL is an open-source, advanced relational database management system (RDBMS) that supports SQL and additional features like JSON, full-text search, and custom functions.

### Key Features of PostgreSQL:
- **ACID Compliance**: Ensures reliable transactions.
- **Extensibility**: Supports custom data types and functions.
- **JSON Support**: Handles semi-structured data.
- **Concurrency**: Uses MVCC (Multi-Version Concurrency Control) for high performance.
- **Security**: Offers robust authentication and encryption.

---

## 🔧 Basic PostgreSQL Commands:

потрібно спочатку увійти в PostgreSQL
```bash
psql -U your_username -d your_database
```
де your_username — це ім'я користувача PostgreSQL, а your_database — ім'я бази даних, до якої хочеш підключитися.

```
# List Databases
\l

# Create a Table
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

# Insert Data
INSERT INTO table_name (name, age) VALUES ('Alice', 30);

# Query Data
SELECT * FROM table_name;

# Update Data
UPDATE table_name SET age = 31 WHERE name = 'Alice';

# Delete Data
DELETE FROM table_name WHERE name = 'Alice';
```

---

## 🔍 Advanced SQL Queries
```sql
-- WHERE clause
SELECT * FROM table_name WHERE age > 25;

-- ORDER BY
SELECT * FROM table_name ORDER BY age DESC;

-- GROUP BY + HAVING
SELECT age, COUNT(*) FROM table_name GROUP BY age HAVING COUNT(*) > 1;

-- LIMIT / OFFSET
SELECT * FROM table_name LIMIT 10 OFFSET 20;
```

---

## 🔗 PostgreSQL Joins
```sql
-- INNER JOIN
SELECT a.name, b.salary
FROM employees a
INNER JOIN salaries b ON a.id = b.emp_id;

-- LEFT JOIN / RIGHT JOIN
SELECT * FROM employees e LEFT JOIN departments d ON e.dept_id = d.id;
```

---

## ⚙️ Useful psql Meta-Commands
- `\dt`: List all tables
- `\d table_name`: Show table schema
- `\du`: List users
- `\q`: Quit psql

---

## 🔐 PostgreSQL User & Access Management
```sql
-- Create User
CREATE USER myuser WITH PASSWORD 'secret';

-- Grant Privileges
GRANT SELECT, INSERT ON table_name TO myuser;

-- Revoke Privileges
REVOKE INSERT ON table_name FROM myuser;
```

---

## 🧰 Tips
- Use **pgAdmin** for GUI-based interaction.
- Enable logging with `log_statement = 'all'` in `postgresql.conf`.
- Always back up with `pg_dump` and restore with `psql` or `pg_restore`.

---

## 📚 Resources:
- [PostgreSQL Official Documentation](https://www.postgresql.org/docs/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)