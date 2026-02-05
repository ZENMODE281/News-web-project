import sqlite3
from contextlib import closing

DB_PATH = "headlines.db"

def init_db():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS headlines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                title TEXT NOT NULL,
                url TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()

def save_headlines(source, items):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        c = conn.cursor()
        for item in items:
            title = item["title"]
            url = item.get("url")
            c.execute("""
                INSERT INTO headlines (source, title, url)
                VALUES (?, ?, ?)
            """, (source, title, url))
        conn.commit()

def get_latest_headlines(limit=50):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        c = conn.cursor()
        c.execute("""
            SELECT source, title, url, created_at
            FROM headlines
            ORDER BY created_at DESC
            LIMIT ?
        """, (limit,))
        return c.fetchall()