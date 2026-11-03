cursor.execute(
    "INSERT INTO customers (id, name) VALUES (?, ?)",
    (5, "Alex")
)

conn.commit()
conn.close()