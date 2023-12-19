from pymongo import MongoClient

# URL de conexión de MongoDB Atlas
mongo_uri = "mongodb+srv://many3487:XMJ86STWK7@pia.ebz9chq.mongodb.net/"

client = MongoClient(mongo_uri)

def collection_user():
    db = client['Aplicacion']
    collection = db['users']
    return collection