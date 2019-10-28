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

#INSERT ONE RECORD
sql_stuff = 'INSERT INTO users (name, email, age) VALUES (%s, %s, %s)'
record1 = ('John', 'john@codemy', 40)

my_cursor.execute(sql_stuff, record1)
mydb.commit()

