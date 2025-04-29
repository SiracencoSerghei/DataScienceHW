import sqlite3
from contextlib import contextmanager

database = './example.db'


@contextmanager
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        yield conn
        conn.commit()  # якщо все добре — зберігаємо
    except sqlite3.Error as e:
        if conn:
            conn.rollback()  # у разі помилки — відкочуємо
        print("DB error:", e)
        raise
    finally:
        if conn:
            conn.close()
 
 