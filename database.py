import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='Mysql',
    passwd='root',
)

# Create Cursor Instance
my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE testdb")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db[0])

