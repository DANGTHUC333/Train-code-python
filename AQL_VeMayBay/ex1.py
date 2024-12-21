import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345a."
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE ql_vemaybay")