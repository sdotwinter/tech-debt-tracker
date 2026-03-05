import sqlite3
from pathlib import Path

def db_path(root:Path): return root/'tech_debt.db'
def init_db(root:Path):
    c=sqlite3.connect(db_path(root)); c.execute('CREATE TABLE IF NOT EXISTS debt(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,area TEXT,impact INTEGER,effort INTEGER,risk INTEGER,status TEXT DEFAULT "open")'); c.commit(); c.close()
def add_item(root:Path,title:str,area:str,impact:int,effort:int,risk:int):
    c=sqlite3.connect(db_path(root)); c.execute('INSERT INTO debt(title,area,impact,effort,risk,status) VALUES (?,?,?,?,?,"open")',(title,area,impact,effort,risk)); c.commit(); c.close()
def list_items(root:Path,status:str='all'):
    c=sqlite3.connect(db_path(root))
    if status=='all': rows=c.execute('SELECT id,title,area,impact,effort,risk,status FROM debt ORDER BY id').fetchall()
    else: rows=c.execute('SELECT id,title,area,impact,effort,risk,status FROM debt WHERE status=? ORDER BY id',(status,)).fetchall()
    c.close(); return rows
def close_item(root:Path,item_id:int):
    c=sqlite3.connect(db_path(root)); c.execute('UPDATE debt SET status="closed" WHERE id=?',(item_id,)); c.commit(); c.close()
