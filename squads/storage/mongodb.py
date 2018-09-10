from pymongo import MongoClient


class MongoDB:
    def configure(self, settings):
        mongo_ = MongoClient(settings['mongo.host'])
        db_name = settings['mongo.db_name']
        self.db = mongo_[db_name]

mongo = MongoDB()
