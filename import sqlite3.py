import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL 
)
""")

cursor.executemany("""
INSERT INTO customers (id, name)
VALUES (?, ?)
""", [
    (1, 'Ivan'),
    (2, 'Peter'),
    (3, 'Kolya'),
    (4, 'Serj')
])

cursor.executemany("""
INSERT INTO orders (id, customer_id, amount)
VALUES (?, ?, ?)
""", [
    (1, 3, 100500),
    (2, 1, 100.5),
    (3, 4, 123),
    (4, 2, 246),
    (5, 1, 369.5)
])

conn.commit()

cursor.execute("SELECT * FROM customers")
print(cursor.fetchall())

cursor.execute("SELECT * FROM orders")
print(cursor.fetchall())

conn.close()