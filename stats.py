import sqlite3

def get_total_today():
    conn = sqlite3.connect("data/pomodoro.db")
    c = conn.cursor()
    c.execute('''
        SELECT COUNT(*) FROM sessions
        WHERE DATE(start_time) = DATE('now', 'localtime')
    ''')
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0
