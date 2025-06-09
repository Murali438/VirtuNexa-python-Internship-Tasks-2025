import sqlite3

def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT,
            details TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_to_db(operation, details):
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (operation, details) VALUES (?, ?)", (operation, details))
    conn.commit()
    conn.close()
