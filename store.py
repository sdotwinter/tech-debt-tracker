import sqlite3
from pathlib import Path

DB=Path.home()/'.tech-debt-tracker'/'debt.db'

def conn():
    DB.parent.mkdir(parents=True, exist_ok=True)
    c=sqlite3.connect(DB)
    c.execute('''CREATE TABLE IF NOT EXISTS debt(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT, area TEXT, impact INTEGER, effort INTEGER, risk INTEGER, notes TEXT
    )''')
    return c

def add_item(title, area, impact, effort, risk, notes=''):
    c=conn(); c.execute('INSERT INTO debt(title,area,impact,effort,risk,notes) VALUES(?,?,?,?,?,?)',(title,area,impact,effort,risk,notes)); c.commit(); c.close()

def list_items():
    c=conn(); rows=c.execute('SELECT id,title,area,impact,effort,risk,notes FROM debt ORDER BY id DESC').fetchall(); c.close(); return rows
