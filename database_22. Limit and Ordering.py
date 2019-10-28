import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    database='testdb',
)

# Create Cursor Instance
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users LIMIT 3")
result = my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1")
result = my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users ORDER BY name ASC")
result = my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users ORDER BY name DESC")
result = my_cursor.fetchall()
for row in result:
    print(row)