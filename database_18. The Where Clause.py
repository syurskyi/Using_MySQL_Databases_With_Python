import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    database='testdb',
)

# Create Cursor Instance
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users WHERE age = 55")
result = my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users WHERE age <= 55")
result = my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users WHERE age => 55")
result = my_cursor.fetchall()
for row in result:
    print(row)

