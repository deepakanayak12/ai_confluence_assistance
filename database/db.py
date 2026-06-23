import sqlite3
import os

DATA_DIR = 'data'
DB_FILE = 'confluence.db'


def _ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def get_db_connection():
    """Get connection to the single confluence.db database."""
    _ensure_data_dir()
    database_path = os.path.join(DATA_DIR, DB_FILE)
    conn = sqlite3.connect(database_path)
    return conn


def create_tables():
    """Create both confluence_data and error_logs tables in the same database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS confluence_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS error_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            error TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()


def insert_data(data):
    """Insert successful data into confluence_data table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO confluence_data (data) VALUES (?)', (data,))
    conn.commit()
    conn.close()


def insert_error_log(error):
    """Insert error into error_logs table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO error_logs (error) VALUES (?)', (error,))
    conn.commit()
    conn.close()
