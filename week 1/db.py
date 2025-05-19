import sqlite3

def init_db():
    conn = sqlite3.connect('calculator.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history (expression TEXT)''')
    conn.commit()
    conn.close()

def save_to_db(expression):
    conn = sqlite3.connect('calculator.db')
    c = conn.cursor()
    c.execute("INSERT INTO history (expression) VALUES (?)", (expression,))
    conn.commit()
    conn.close()
