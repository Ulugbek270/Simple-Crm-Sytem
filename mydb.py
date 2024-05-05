import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pycharm2363',

)

cursorObj = dataBase.cursor()
cursorObj.execute("CREATE DATABASE valsep")

print("Your Database created successfully")
