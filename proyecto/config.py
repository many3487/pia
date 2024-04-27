from pymongo import MongoClient
import contraseñas as c
print(c.usuario)
# URL de conexión de MongoDB Atlas
mongo_uri = f"mongodb+srv://{c.usuario}:{c.password}@pia.ebz9chq.mongodb.net/"

client = MongoClient(mongo_uri)

def collection_user():
    db = client['Aplicacion']
    collection = db['users']
    return collection