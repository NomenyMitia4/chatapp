from database import DatabaseModel

class UserModel():
    def __init__(self, id=None, nickname=None, photo=None):
        self.database = DatabaseModel()
        self._user_id = id
        self._nickname = nickname
        self._photo = photo
        
    def _setNickname(self, nickName):
        self._nickname = nickName
        
    def _getNickname(self):
        return self._nickname
    
    def _setPhoto(self, photo):
        self._photo = photo
        
    def _getPhoto(self):
        return self._photo
    
    def _getUser(self):
        query = "SELECT * FROM user"
        result = self.database.get(query)
        
        return result
    
    def _createUser(self, data):
        query = "INSERT INTO user( nickname, photo ) VALUES ( %s, %s )"
        result = self.database.create(query, data)
        
        return result