import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    database='testdb',
)

# Create Cursor Instance
my_cursor = mydb.cursor()

sql_stuff = 'INSERT INTO users (name, email, age) VALUES (%s, %s, %s)'
records = [
    ('Tim', 'tim@tim.com', 32),
    ('Mary', 'mary@mary.com', 21),
    ('Steve', 'steve@steve.com', 57),
    ('Tina', 'tina@tina.com', 29),
]

my_cursor.executemany(sql_stuff, records)
mydb.commit()