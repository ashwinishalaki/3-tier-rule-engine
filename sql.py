import sqlite3

def create_tables():
    conn = sqlite3.connect('rule_engine.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_profiles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        age INTEGER,
                        department TEXT,
                        income REAL,
                        spend REAL
                     )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS rules (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        rule_expression TEXT
                     )''')
    conn.commit()
    conn.close()

def save_user_profile(user):
    conn = sqlite3.connect('rule_engine.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_profiles (age, department, income, spend) VALUES (?, ?, ?, ?)',
                   (user.age, user.department, user.income, user.spend))
    conn.commit()
    conn.close()
