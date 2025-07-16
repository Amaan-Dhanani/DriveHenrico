import pymongo
import pymongo.collection
import pymongo.database
from utils.helper.config import Yaml
from utils.console import console

class MongoClient:
    uri: str = Yaml().populate_environment(Yaml().get("backend.database.uri"))
    client: pymongo.MongoClient = pymongo.MongoClient(uri)
    
    console.info("Mongo Uri:", uri)
    
    database: pymongo.database.Database = client["drivehenrico"]
    
    
    
    # Collections
    sessions: pymongo.collection.Collection = database["sessions"]
    users: pymongo.collection.Collection = database["users"]
    credentials: pymongo.collection.Collection = database["credentials"]
    verification: pymongo.collection.Collection = database["verification"]