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

# AND / OR Clause
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age = 29")
result = my_cursor.fetchall()
for row in result:
    print(row)

# AND / OR Clause
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age = 100")
result = my_cursor.fetchall()
for row in result:
    print(row)