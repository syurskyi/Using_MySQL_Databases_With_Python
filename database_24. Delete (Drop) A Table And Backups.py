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

# DELETE DROP TABLE
my_sql = "DROP TABLE users"
my_cursor.execute(my_sql)

