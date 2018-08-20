from squads.storage.mongodb import mongo

def get_squads(request):
    squads = mongo.db.squads.find_one()
    squads.pop('_id')
    return squads