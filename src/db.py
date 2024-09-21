import sqlite3

def init_db():
    conn = sqlite3.connect('audit_results.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS results 
                      (id INTEGER PRIMARY KEY, audit_type TEXT, result TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def save_audit_result(audit_type, result):
    conn = sqlite3.connect('audit_results.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (audit_type, result, date) VALUES (?, ?, datetime('now'))", 
                   (audit_type, result))
    conn.commit()
    conn.close()
