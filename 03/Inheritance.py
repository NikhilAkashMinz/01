import psycopg2

conn = psycopg2.connect(
    dbname="School",
    user="postgres",
    password="nikhil",
    host="localhost",
)

cur = conn.cursor()
cur.execute("SELECT * FROM students;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()