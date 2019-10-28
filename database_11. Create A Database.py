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

#SHOW DATABASE
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db[0])