import sqlite3

db_path = "db/main.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("select * from todo")
res = cursor.fetchall()

print(res)
