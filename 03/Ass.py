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

cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(80) NOT NULL,
    grade VARCHAR(10) NOT NULL,
    section VARCHAR(5));
            """)
conn.commit()

cur.close()
conn.close()
print("Tables created successfully")