import os
import sqlite3

from contextlib import contextmanager

@contextmanager
def create_connection(db_file):
    conn = None
    try:
        db_dir = os.path.dirname(db_file)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)
            print(f"Directory created: {db_dir}")

        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")

        yield conn
        conn.rollback()
        conn.close()
        print("Connection closed.")

    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        yield None

