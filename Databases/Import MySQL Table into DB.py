import mysql.connector

cnx = mysql.connector.connect(user='root', password='test', host='127.0.0.1', database='test')

mycursor= cnx.cursor()
mycursor.execute("CREATE TABLE users (ID VARCHAR(255), Name VARCHAR(255), Department VARCHAR(255), Location VARCHAR(255), Pay VARCHAR(255))")

cnx.close()