from database import DatabaseModel
from datetime import datetime

class MessageModel():
    def __init__(self, id=None, sender_id=None, receiver_id=None, content=None, times=datetime.now()):
        self.database = DatabaseModel()
        self._id = id
        self._sender_id = sender_id
        self._receiver_id = receiver_id
        self._content = content
        self._times = times
        
    def _setContent(self, content):
        self._content = content
        
    def _getContent(self):
        return self._content
    
    def _setTimes(self, times):
        self._times = times
        
    def _getTimes(self):
        return self._times
    
    def _getMessages(self):
        try:
            query = "SELECT * FROM messages as m INNER JOIN user as u1 on u1.user_id = m.sender_id INNER JOIN user as u2 on u2.user_id = m.receiver_id"
            result = self.database.get(query)
            print(result)
        except Exception as e:
            print(e)
            
        return result
    
    def _createMessage(self, data):
        query = "INSERT INTO messages( sender_id, receiver_id, content ) VALUES ( %s, %s, %s)"
        result = self.database.create(query, data)
        
        return result