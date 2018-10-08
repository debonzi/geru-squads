# -*- coding: utf-8 -*-
import os
from pyramid.config import Configurator

from squads.storage.mongodb import mongo


def main(global_config, **settings):
    envvar_mongo_uri = os.environ.get('MONGODB_URI', None)
    if envvar_mongo_uri:
        settings.update(
            {
                'mongo.host': envvar_mongo_uri
            }
        )
    config = Configurator(settings=settings)

    mongo.configure(settings)

    config.add_route('orgchart', '/')

    config.add_route('squads', '/api/v1/squads')
    config.add_route('squad', '/api/v1/squads/{code}')
    config.add_route('members', '/api/v1/squads/{code}/members')
    config.add_route('member', '/api/v1/squads/{code}/members/{index}')
    config.add_route('images', '/api/v1/images')
    config.scan('.views')


    return config.make_wsgi_app()
