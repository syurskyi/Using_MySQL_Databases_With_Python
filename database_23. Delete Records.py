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

# DELETE RECORDS
my_sql = "DELETE FROM users WHERE user_id = 6"
my_cursor.execute(my_sql)
mydb.commit()