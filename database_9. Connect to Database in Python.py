import mysql.connector

#SET MYSQL CONNECTION
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    database='testdb',
)

print(mydb)