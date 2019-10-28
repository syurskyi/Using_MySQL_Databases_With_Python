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

# UPDATING RECORDS
my_sql = "UPDATE users SET age = 40 WHERE name = 'John'"

my_sql = "UPDATE users SET age = 40 WHERE user_id = 6 "

my_cursor.execute(my_sql)
mydb.commit