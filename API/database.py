import mysql.connector

class DatabaseModel():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='chatapp')
            self.connection.autocommit = True
            self.cur = self.connection.cursor(dictionary=True)
            print("Connection to the database established...")
        except:
            print("Error connection to the database...")