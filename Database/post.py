"""Postgres DB example."""

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="mb",
    port=5432,
)

cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS employee ("
    "id INT PRIMARY KEY, "
    "name VARCHAR(40))"
)

cursor.execute(
    "INSERT INTO employee (id, name) VALUES (102, 'test1')"
)

cursor.execute("SELECT * FROM employee")

for row in cursor.fetchall():
    print(row)

conn.commit()
cursor.close()
conn.close()
