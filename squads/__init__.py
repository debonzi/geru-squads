# -*- coding: utf-8 -*-
from pyramid.config import Configurator

from squads.storage.mongodb import mongo
from squads.views.api import get_squads

def main(global_config, **settings):
    config = Configurator(settings=settings)

    mongo.configure(settings)

    config.add_route('squads', '/')
    config.add_view(get_squads, route_name='squads', renderer='json')


    return config.make_wsgi_app()
