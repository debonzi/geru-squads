from pyramid import httpexceptions
from squads.storage.mongodb import mongo

def get_squads(request):
    squads = mongo.db.squads.find_one()
    if not squads:
        raise httpexceptions.HTTPNotFound()
    squads.pop('_id')
    return squads
