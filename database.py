import sqlite3
import datetime
from config import LOG_DB

def init_db():
    """Initialize SQLite database and table"""
    conn = sqlite3.connect(LOG_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_report(data):
    """Save a report to SQLite"""
    conn = sqlite3.connect(LOG_DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reports (timestamp, data) VALUES (?, ?)",
        (str(datetime.datetime.now()), str(data))
    )
    conn.commit()
    conn.close()
