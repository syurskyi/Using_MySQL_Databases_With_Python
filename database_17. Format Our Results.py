import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    database='testdb',
)

# Create Cursor Instance
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
# Pull Data Frfom The Table
print("NAME\tEMAIL\tAGE\tID")
print("____________________________________________________________")
for row in result:
    print(row[0] + " \t%s" %row[1] + " \t%s" %row[2] + " \t%s" %row[3])

