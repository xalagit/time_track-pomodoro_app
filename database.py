import sqlite3
import os

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/pomodoro.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_time TEXT,
            end_time TEXT,
            duration INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def log_session(start_time, end_time, duration):
    conn = sqlite3.connect("data/pomodoro.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO sessions (start_time, end_time, duration)
        VALUES (?, ?, ?)
    ''', (start_time.isoformat(), end_time.isoformat(), duration))
    conn.commit()
    conn.close()
