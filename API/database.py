import mysql.connector
import json

class DatabaseModel():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='chatapp')
            self.connection.autocommit = True
            self.cur = self.connection.cursor(dictionary=True)
            print("Connection to the database established...")
        except:
            print("Error connection to the database...")
            
    def get(self, query):
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()
        except:
            print("Error")
            
        return result
    
    def create(self, query, data=None):
        if data is None:
            data = []
        try:
            # query = "INSERT INTO user(name, password) VALUES(%s, %s)"
            self.cur.execute(query, tuple(data.values()))
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            return f"Failed to add user: {e}"
        
        return "User added successfully"
        