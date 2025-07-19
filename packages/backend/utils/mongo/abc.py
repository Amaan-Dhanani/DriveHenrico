"""
Class abstractions for the database side of things
"""


# === Base ===
from pymongo.collection import Collection
from pymongo.results import InsertOneResult, UpdateResult

# === Type Hinting ===
from typing import Any, Mapping, Type, TypeVar, Union
from abc import ABC, abstractmethod

# === Utilities ===
from utils.mongo.Client import MongoClient

from utils.types.user import User
from utils.types.verification import Verification

T = TypeVar("T")

def data_cast(value: Any, _type: Type[T]) -> T:
    """
    Used to cast certain keyword arguments into a specific type or wrapper
    
    :param Any value: Key within kwargs or index position in args that will be casted
    :param Type[T] _type: Dataclass object or type object
    """
    
    return _type(value) # type: ignore
    

class MongoCollectionBase(ABC):
    """
    Abstraction class for mongo collections, used as a interface layer 
    between the developer and the mongo database
    """
    
    def __init__(self, collection: Collection) -> None:
        """
        :param Collection collection: Mongo collection object, saved in self
        """
        super().__init__()
        
        self.collection = collection  
        
    def insert(self, document: Mapping[str, Any], *args, **kwargs) -> InsertOneResult:
        return self.collection.insert_one(document, *args, **kwargs)  

    def _find(self, filter: Any) -> Any:
        """
        Attempts to find a document with the given filter
        
        :param Any filter: filter object, passed through to mongo to determine what is deleted
        """
        return self.collection.find_one(filter)
    
    def _delete(self, filter: Any) -> None:
        """
        Finds and removes a document from the collection object
        
        :param Any filter: filter object, passed through to mongo to determine what is deleted
        """
        self.collection.delete_one(filter)
    
    def _exists(self, *args, **kwargs) -> bool:
        """
        Checks if a document exists by calling the abstract find method
        """
        if not self.find(*args, **kwargs):
            return False
        return True
    
    def _update(self, filter: Mapping[str, Any], update: Mapping[str, Any], *args, **kwargs) -> UpdateResult:
        """
        Updates a document, template method
        """
        return self.collection.update_one(filter, update, *args, **kwargs)
    
        
    @abstractmethod
    def find(self, *args, **kwargs) -> Any:
        """
        Abstract method used in conjunction with the `_find` method. this method should call `_find`
        """
        pass
        
    @abstractmethod
    def delete(self, *args, **kwargs) -> None:
        """
        Abstract method used in conjunction with the supplied `_delete` method. This method should call `_delete`
        """
        pass
    
    @abstractmethod
    def exists(self, *args, **kwargs) -> bool:
        """
        Abstract method used in conjunction with the supplied `_exists` method. This method should call `_exists`
        """
        pass
    
    @abstractmethod
    def update(self, filter: Mapping[str, Any], update: Mapping[str, Any], *args, **kwargs) -> UpdateResult:
        """
        Abstract method used in conjunction with the supplied `_update` method. this method should call `_update`
        """
        pass
    
    
class UsersCollection(MongoCollectionBase):
    """
    Abstract User Collection class to help manage users within the database
    """
    
    def __init__(self, collection: Collection = MongoClient.users) -> None:
        super().__init__(collection)
        
    
    def find(self, id: str) -> Any:
        """
        Finds a given user with a specified id
        
        :param str id: User ID
        
        :returns: Document of user
        """
        return self._find({"_id": id})
    
    def get(self, id: str) -> Union[User, None]:
        """
        Gets the current user with a specified id
        
        :param str id: User ID
        
        :returns: User object or None
        """
        if not self.exists(id=id):
            return None
        return User(**self.find(id=id))
    
    def delete(self, id: str) -> None:
        """
        Deletes a user via a given id
        
        :param str id: User ID
        """
        return self._delete({"_id": id})
    
    def exists(self, id: str) -> bool:
        return self._exists(id=id)
    
    def update(self, id: str, operation: str, data: Mapping[str, Any]) -> UpdateResult:
        """
        Updates a user with a given `id` and `operation`
        
        :param str id: User ID
        :param str operation: Mongo Operation
        :param str data: Update data
        """
        return self._update({"_id": id}, {operation: data})

class VerificationCollection(MongoCollectionBase):
    """
    Abstract Verification Collection class to help manage verification structures within the database
    """
    
    def __init__(self, collection: Collection = MongoClient.verification) -> None:
        super().__init__(collection)
        
    
    def find(self, id: str) -> Any:
        """
        Finds a given user with a specified id
        
        :param str id: User ID
        
        :returns: Document of user
        """
        return self._find({"_id": id})
    
    def get(self, id: str) -> Union[Verification, None]:
        """
        Gets the current user with a specified id
        
        :param str id: Verification ID
        
        :returns: Verification object or None
        """
        if not self.exists(id=id):
            return None
        
        return Verification(**self.find(id=id))
    
    def delete(self, id: str) -> None:
        """
        Deletes a verification via a given id
        
        :param str id: Verification ID
        """
        return self._delete({"_id": id})
    
    def exists(self, id: str) -> bool:
        return self._exists(id=id)
    
    def update(self, id: str, operation: str, data: Mapping[str, Any]) -> UpdateResult:
        """
        Updates a verification object with a given `id` and `operation`
        
        :param str id: Verification ID
        :param str operation: Mongo Operation
        :param str data: Update data
        """
        return self._update({"_id": id}, {operation: data})
    
class CredentialsCollection(MongoCollectionBase):
    """
    Abstract Credentials Collection class to help manage credential structures within the database
    """
    
    def __init__(self, collection: Collection = MongoClient.credentials) -> None:
        super().__init__(collection)
        
    
    def find(self, id: str) -> Any:
        """
        Finds a given user with a specified id
        
        :param str id: Account | Credential ID, 
        
        :returns: Document of credentials
        """
        return self._find({"_id": id})
    
    def get(self, id: str) -> Union[Verification, None]:
        """
        Gets the current user with a specified id
        
        :param str id: Account | Credential ID
        
        :returns: Credential object or None
        """
        if not self.exists(id=id):
            return None
        
        return Verification(**self.find(id=id))
    
    def delete(self, id: str) -> None:
        """
        Deletes a credential via a given id
        
        :param str id: Account | Credential ID
        """
        return self._delete({"_id": id})
    
    def exists(self, id: str) -> bool:
        return self._exists(id=id)
    
    def update(self, id: str, operation: str, data: Mapping[str, Any]) -> UpdateResult:
        """
        Updates a credential object with a given `id` and `operation`
        
        :param str id: Credential ID
        :param str operation: Mongo Operation
        :param str data: Update data
        """
        return self._update({"_id": id}, {operation: data})

users_collection = UsersCollection()
verification_collection = VerificationCollection()
credentials_collection = CredentialsCollection()