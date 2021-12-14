import sqlite3
import os

db_path = "db/main.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

if not(os.path.exists(db_path)):
    cursor.execute("create table todo(title, detail);")

cursor.execute("insert into todo values (?,?)", ("散歩", "ジャパンに買い物に行く"))

cursor.execute("select * from todo")
print(cursor.fetchall())
