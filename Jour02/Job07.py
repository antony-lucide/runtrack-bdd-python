import mysql.connector


db = mysql.connector.connect(host='localhost',user='root',password='jijo', database='entreprise')
curseur = db.cursor()

curseur.execute('SELECT * FROM employes WHERE salaire > 3;')
var = curseur.fetchall()
print(var)