import sqlite3
import os

db_path = "db/main.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("create table todo(id integer, title text, detail text);")

# qmark style
cursor.execute("insert into todo values (?,?,?)", (5, "散歩", "ジャパンに買い物に行く"))

# named style
cursor.execute("insert into todo values (:id,:title,:detail)",
               {"id": 3, "title": "買い物", "detail": "ヨドバシカメラで買い物する"})

conn.commit()

cursor.execute("select * from todo")
print(cursor.fetchall())

conn.close()
