from model.user_model import UserModel
from flask import jsonify, request


class UserController():
    def __init__(self):
        self.user = UserModel()
        
    def post(self, data):
        try:
            data = data.get_json()
            if not data:
                return {"error": "No JSON data received"}

            create = self.user._createUser(data) 
        except Exception as e:
            print(e)
        
        if create:
            return {'message': 'User created successfully', 'data': data}, 201
        else:
            return {'message': 'Failed to create user'}, 400
    
    def get(self):
        data = self.user._getUser()
        return jsonify(data)
    
    def put(self):
        return "This is the route to update the user"
    
    def delete(self):
        return "This is the route to delete the user"