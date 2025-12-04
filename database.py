import sqlite3
from datetime import datetime

DB_FILE = 'sentiment_history.db'

def init_db():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sentiments
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  text TEXT, 
                  sentiment TEXT, 
                  timestamp TEXT)''')
    conn.commit()
    return conn

# Khởi tạo kết nối toàn cục cho module này
conn = init_db()

def save_result(text, sentiment):
    try:
        c = conn.cursor()
        # Lưu định dạng ISO string (YYYY-MM-DD HH:MM:SS)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Parameterized query chống SQL Injection
        c.execute("INSERT INTO sentiments (text, sentiment, timestamp) VALUES (?, ?, ?)", 
                  (text, sentiment, timestamp))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Lỗi Database: {e}")

def get_recent_history(limit=50):
    try:
        c = conn.cursor()
        c.execute("SELECT timestamp, text, sentiment FROM sentiments ORDER BY id DESC LIMIT ?", (limit,))
        return c.fetchall()
    except sqlite3.Error as e:
        print(f"Lỗi Database: {e}")
        return []