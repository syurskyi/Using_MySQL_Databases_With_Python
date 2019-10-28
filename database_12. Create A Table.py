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

#CREATE TABLE
my_cursor.exucute('CREATE TABLE users (name VARCHAR(255), '
                  'email VARCHAR(255), '
                  'age INTEGER(10), '
                  'user_id INTEGER AUTO_INCREMENT PRIMARY KEY)')

#SHOW DATABASE
my_cursor.execute('SHOW TABLES')

for table in my_cursor:
    print(table[0])
