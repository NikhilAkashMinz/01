import psycopg2

conn = psycopg2.connect(
    dbname="School",
    user="postgres",
    password="nikhil",
    host="localhost",
)

if conn:
    print("Connection to the PostgresSQL established  successfully")
else:
    print("Connection to the PostgresSQL failed")

cur = conn.cursor()

cur.execute("INSERT INTO students (first_name, grade,section) VALUES ('Saksham','Grade 10', 'A')")
cur.execute("INSERT INTO students (first_name, grade, section) VALUES ('Rahul','Grade 9','B')")
cur.execute("INSERT INTO students (first_name, grade, section) VALUES ('Ananya','Grade 8','C')")
cur.execute("INSERT INTO students (first_name, grade, section) VALUES ('Aman','Grade 7','A')")
cur.execute("INSERT INTO students (first_name, grade, section) VALUES ('Priya','Grade 10','B')")

conn.commit()
cur.close()
conn.close()
print("Tables created successfully")