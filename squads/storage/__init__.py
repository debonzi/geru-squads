from .mongodb import mongo

class SquadsStorage:
    def save(self, data):
        collection = mongo.db['squads']
        return collection.insert_one(data)

squads_storage = SquadsStorage()
