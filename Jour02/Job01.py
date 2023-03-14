import mysql.connector


db = mysql.connector.connect(host='localhost',user='root',password='123456')

db.cursor()


print(db)