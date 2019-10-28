import mysql.connector

# SET MYSQL CONNECTION
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    database='testdb',
)

# Create Cursor Instance
my_cursor = mydb.cursor()

#WHERE CLAUSE
my_cursor.execute("SELECT * FROM users WHERE age = 55")
result = my_cursor.fetchall()
for row in result:
    print(row)

#WHERE CLAUSE
my_cursor.execute("SELECT * FROM users WHERE age <= 55")
result = my_cursor.fetchall()
for row in result:
    print(row)

#WHERE CLAUSE
my_cursor.execute("SELECT * FROM users WHERE age => 55")
result = my_cursor.fetchall()
for row in result:
    print(row)

