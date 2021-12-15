import mysql.connector as mysql

conn = mysql.connect(user="root", password="", database='db_Sahabat_Masyarakat', host="localhost", port='3306')
c = conn.cursor()

c.execute("DROP DATABASE db_Sahabat_Masyarakat")