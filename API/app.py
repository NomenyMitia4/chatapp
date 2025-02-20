from flask import Flask, request
from flask_cors import CORS # type: ignore
from controller.user_controller import UserController
from controller.message_controller import MessageController

app = Flask(__name__)

user = UserController()
message = MessageController()

cors = CORS(app, origins="*", methods=['GET', 'POST'])

@app.route("/api/chatApp/addUser", methods=["POST"])
def addUser():
    return user.post(request)

@app.route("/api/chatApp/getAllUser", methods=["GET"])
def getAllUser():
    return user.get()

@app.route("/api/chatApp/getAllMessages", methods=["GET"])
def getAllMessages():
    return message.get()

@app.route("/api/chatApp/sendMessage", methods=["POST"])
def sendMessages():
    return message.post(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8000", debug=True)