from flask_restful import Resource
from database import DatabaseModel

class UserResource(Resource):
    def __init__(self):
        self.user_id = 0
        self.nickname = "default"
        self.photo = "photo.png"
    
    def post(self):
        return 'This is the route to post something'
    
    def get(self):
        database = DatabaseModel()
        
        return "This is the route to get the user"