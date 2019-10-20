import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='syurskyi',
    passwd='',
)

print(mydb)