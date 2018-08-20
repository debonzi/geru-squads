from pymongo import MongoClient


class MongoDB:
    def configure(self, settings):
        mongo = MongoClient(host=settings['mongo.host'])
        db_name = settings['mongo.db_name']
        self.db = mongo[db_name]

mongo = MongoDB()
