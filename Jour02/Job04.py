import mysql.connector


db = mysql.connector.connect(host='localhost',user='root',password='123456', database='LaPlateforme')
curseur = db.cursor()

curseur.execute('SELECT nom capacite FROM salles;')
var = curseur.fetchall()
print(var)
