import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'Yoyom@043mysql'
)

#prepare cursoe oibject
cursorObj = dataBase.cursor()

#create database
cursorObj.execute("CREATE DATABASE myfirstdb")

# initla setup steps
# make sure you have mysql installed on your machine
# make sure you have installed mysql-connector-python
# make sure you have installed django
# migrate the database      python3 manage.py migrate
# create a super user       python3 manage.py createsuperuser
# run the server            python3 manage.py runserver

print("Database created successfully")