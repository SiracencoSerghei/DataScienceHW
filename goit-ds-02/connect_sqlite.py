import sqlite3
from contextlib import contextmanager

database = './todo.db'

@contextmanager
def connect_to_db(db_name):
    """Context manager for SQLite database connection."""
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"SQLite error: {e}")
        raise
    finally:
        if conn:
            conn.close()
            print("Connection closed.")
            