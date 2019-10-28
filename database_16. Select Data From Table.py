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

#PULL DATA FROM THE TABLE
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()

for row in result:
    print(row[3])

#PULL DATA FROM THE TABLE
my_cursor.execute("SELECT name FROM users")
result = my_cursor.fetchall()

for row in result:
    print(row[3])

#PULL DATA FROM THE TABLE
my_cursor.execute("SELECT name FROM users")
result = my_cursor.fetchone()

for row in result:
    print(row[3])