from flask import Flask, request
from controller.user_controller import UserController

app = Flask(__name__)

user = UserController()

@app.route("/api/chatApp/addUser", methods=["POST"])
def addUser():
    return user.post(request)

@app.route("/api/chatApp/getAllUser", methods=["GET"])
def getAllUser():
    return user.get()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8000", debug=True)