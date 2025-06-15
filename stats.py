import sqlite3

def get_total_today():
    conn = sqlite3.connect("data/pomodoro.db")
    c = conn.cursor()
    c.execute('''
        SELECT SUM(duration) FROM sessions
        WHERE DATE(start_time) = DATE('now', 'localtime')
    ''')
    result = c.fetchone()
    conn.close()
    total_secs = result[0] if result and result[0] else 0
    total_mins = total_secs // 60
    return total_mins

def get_total_week():
    conn = sqlite3.connect("data/pomodoro.db")
    c = conn.cursor()
    c.execute('''
        SELECT SUM(duration) FROM sessions
        WHERE strftime('%W', start_time) = strftime('%W', 'now', 'localtime')
        AND strftime('%Y', start_time) = strftime('%Y', 'now', 'localtime')
    ''')
    result = c.fetchone()
    conn.close()
    total_secs = result[0] if result and result[0] else 0
    total_mins = total_secs // 60
    return total_mins

def get_total_month():
    conn = sqlite3.connect("data/pomodoro.db")
    c = conn.cursor()
    c.execute('''
        SELECT SUM(duration) FROM sessions
        WHERE strftime('%m', start_time) = strftime('%m', 'now', 'localtime')
        AND strftime('%Y', start_time) = strftime('%Y', 'now', 'localtime')
    ''')
    result = c.fetchone()
    conn.close()
    total_secs = result[0] if result and result[0] else 0
    total_mins = total_secs // 60
    return total_mins

def get_hourly_distribution(formatter):
    conn = sqlite3.connect("data/pomodoro.db")
    c = conn.cursor()
    c.execute('''
        SELECT strftime('%H', start_time) as hour, SUM(duration) as total
        FROM sessions
        GROUP BY hour
        ORDER BY total DESC
        LIMIT 5
    ''')
    rows = c.fetchall()
    conn.close()
    if not rows:
        return "Sin datos aún."
    result = ""
    for hour, total in rows:
        result += f"Hora {hour}: {formatter(total)}\n"
    return result

def format_h_mm(total_secs):
    hours = total_secs // 3600
    mins = (total_secs % 3600) // 60
    return f"{hours}:{mins:02}"
