import sqlite3

def init_db():
    conn = sqlite3.connect("calc_history.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT,
            result TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_history(operation, result):
    conn = sqlite3.connect("calc_history.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (operation, result) VALUES (?, ?)", (operation, str(result)))
    conn.commit()
    conn.close()

def fetch_history():
    conn = sqlite3.connect("calc_history.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    rows = cursor.fetchall()
    conn.close()
    return rows
