from model.message_model import MessageModel
from flask import jsonify, request


class MessageController():
    def __init__(self):
        self.message = MessageModel()
        
    def post(self, data):
        try:
            data = data.get_json()
            if not data:
                return {"error": "No JSON data received"}

            create = self.message._createMessage(data)
        except Exception as e:
            print(e)
        
        if create:
            return {'message': 'User created successfully', 'data': data}, 201
        else:
            return {'message': 'Failed to create user'}, 400
    
    def get(self):
        data = self.message._getMessages()
        return jsonify(data)
    
    def put(self):
        return "This is the route to update the user"
    
    def delete(self):
        return "This is the route to delete the user"