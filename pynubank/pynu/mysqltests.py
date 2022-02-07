import mysql.connector

USER = 'root'
PASSWORD = 'root'
HOST = '172.17.0.1'
PORT = 3306
DATABASE = 'NuExpenses'

cnx = mysql.connector.connect(user=USER,
                              password=PASSWORD,
                              host=HOST,
                              port=PORT,
                              database=DATABASE)

query = ("SELECT * FROM expenses")

cursor = cnx.cursor()

print(cursor.execute(query))

cnx.close()