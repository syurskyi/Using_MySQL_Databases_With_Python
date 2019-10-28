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

# WHERE and LIKE WILDCARDS
my_cursor.execute("SELECT * FROM users WHERE name LIKE 'J%'")
result = my_cursor.fetchall()
for row in result:
    print(row)