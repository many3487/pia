from config import collection_user
from bson import ObjectId

class ModelUser:
    def __init__(self):
        self.collection = collection_user()

    def _convert_objectid_to_str(self, user):
        user["_id"] = str(user["_id"])
        return user

    def find_user_by_usuario(self, usuario):
        query = {"usuario": usuario}
        result = self.collection.find(query)
        users = [self._convert_objectid_to_str(user) for user in result]
        return users
    
    def insert_user(self, user_data):
        # Insertar el nuevo usuario en la base de datos
        self.collection.insert_one(user_data)