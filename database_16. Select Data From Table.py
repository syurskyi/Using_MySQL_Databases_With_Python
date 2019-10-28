import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    database='testdb',
)

# Create Cursor Instance
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()

for row in result:
    print(row[3])

my_cursor.execute("SELECT name FROM users")
result = my_cursor.fetchall()

for row in result:
    print(row[3])

my_cursor.execute("SELECT name FROM users")
result = my_cursor.fetchone()

for row in result:
    print(row[3])