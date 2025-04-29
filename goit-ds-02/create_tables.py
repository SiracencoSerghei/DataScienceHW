from sqlite3 import Error
from connect_sqlite import connect_to_db, database


def create_table(conn, table):
    """
    Create a table in the SQLite database
    :param conn: Connection object
    :param table: SQL statement to create a table
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)


# Створення таблиці користувачів
users = """
DROP TABLE IF EXISTS users
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
"""

# Створення таблиці статусів
status = """
DROP TABLE IF EXISTS status
CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);
"""

# Створення таблиці завдань
tasks = """
DROP TABLE IF EXISTS tasks
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES status (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);
"""

if __name__ == '__main__':


    # Підключення до бази даних і створення таблиць
    with connect_to_db(database) as conn:
        if conn is not None:
            create_table(conn, users)
            create_table(conn, status)
            create_table(conn, tasks)
            print("Tables created successfully.")
        else:
            print("Error! cannot create the database connection.")
