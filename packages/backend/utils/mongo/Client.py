import pymongo
import pymongo.collection
import pymongo.database
from siblink import Config
from utils.helper.config import Yaml

class MongoClient:
    uri = Yaml().get("backend.database.uri")
    client: pymongo.MongoClient = pymongo.MongoClient(uri)
    
    print("Client Connection: ", uri)
    
    database: pymongo.database.Database = client["drivehenrico"]
    
    # Collections
    sessions: pymongo.collection.Collection = database["sessions"]
    users: pymongo.collection.Collection = database["users"]
    credentials: pymongo.collection.Collection = database["credentials"]