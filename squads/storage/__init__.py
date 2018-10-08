import pymongo
from .mongodb import mongo


COLLECTION_NAME = 'organization_charts'

class SquadsStorage:
    def latest(self):
        collection = mongo.db[COLLECTION_NAME]
        cursor = collection.find({}, {'_id': False}).sort('$natural', pymongo.DESCENDING).limit(1)
        return cursor.next() if cursor.count() > 0 else {}

    def save(self, data):
        collection = mongo.db[COLLECTION_NAME]
        return collection.insert_one(data)


squads_storage = SquadsStorage()
