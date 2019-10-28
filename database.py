import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    database='testdb',
)

# Create Cursor Instance
my_cursor = mydb.cursor()

# Create A Database
# my_cursor.execute("CREATE DATABASE testdb")

# Show Database
# my_cursor.execute("SHOW DATABASES")
#
# my_cursor.exucute('CREATE TABLE users (name VARCHAR(255), '
#                   'email VARCHAR(255), '
#                   'age INTEGER(10), '
#                   'user_id INTEGER AUTO_INCREMENT PRIMARY KEY)')
#
# my_cursor.execute('SHOW TABLES')
#
# for table in my_cursor:
#     print(table[0])

# sql_stuff = 'INSERT INTO users (name, email, age) VALUES (%s, %s, %s)'
# record1 = ('John', 'john@codemy', 40)
#
# my_cursor.execute(sql_stuff, record1)
# mydb.commit()

# sql_stuff = 'INSERT INTO users (name, email, age) VALUES (%s, %s, %s)'
# records = [
#     ('Tim', 'tim@tim.com', 32),
#     ('Mary', 'mary@mary.com', 21),
#     ('Steve', 'steve@steve.com', 57),
#     ('Tina', 'tina@tina.com', 29),
# ]
#
# my_cursor.executemany(sql_stuff, records)
# mydb.commit()

