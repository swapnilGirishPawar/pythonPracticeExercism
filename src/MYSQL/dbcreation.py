import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="swapnil123",
    database="metabase"
)
mycursor = mydb.cursor()
"""Create database in server"""
# mycursor.execute("CREATE DATABASE metabase")

"""creating table in the database"""
# mycursor.execute("CREATE TABLE users (Name VARCHAR(255), Addess VARCHAR(255))")

"""Showing the table in the database"""
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

"""Create primary key when creating the table:"""
# db = mydb.cursor()
# db.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

"""Inserting data into table"""
# sql = "INSERT INTO customers (name, address) VALUES(%s, %s)"
# val = ('amol', 'India 34')
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted !")

"""get id of row"""
# print(mycursor.lastrowid)

"""Select from table"""
# mycursor.execute("SELECT * from customers")
# res = mycursor.fetchall()
# for x in res:
#     print(x)

"""deleting the data"""
# sql = "DELETE FROM customers where name='pawar'"
# sql1 = "SELECT * from customers"
# # mycursor.execute(sql)
# # mydb.commit()
# mycursor.execute(sql1)
# res = mycursor.fetchall()
# for x in res:
#     print(x)
