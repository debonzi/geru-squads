import pytest
from webtest import TestApp

from pyramid import paster  # Pyramid object to read config files.
from pyramid import testing  # Pyramid object to create test config

from squads import main  # Our "create application" function
from squads.storage.mongodb import mongo as mongo_
from squads.storage import SquadsStorage

settings = paster.get_appsettings('testing.ini', name='main')
config = testing.setUp(settings=settings)

app_ = main(config, **settings)
mongo_.configure(settings)


@pytest.fixture
def squads_storage(mongodb):
    return SquadsStorage()

@pytest.fixture(scope='function')
def mongodb():
    # clear all collections
    collections = mongo_.db.collection_names()
    for c in collections:
        mongo_.db.drop_collection(c)
    return mongo_


@pytest.fixture(scope='function')
def app():
    yield app_


@pytest.fixture(scope='function')
def testapp(app):
    return TestApp(app)

@pytest.fixture
def org_chart_data1(scope='function'):
    return {
        'squads': [
            {
                'code': 'consig',
                'name': 'Consig',
                'members': [
                    {
                        'name': 'Ana',
                        'role': 'PO'
                    },
                    {
                        'name': 'Flávio',
                        'role': 'LT'
                    }
                ],
                'thirtyparty': True
            },
            {
                'code': 'originacao',
                'name': 'Originação',
                'members': [
                    {
                        'name': 'Adriana',
                        'role': 'PO'
                    },
                    {
                        'name': 'Debonzi',
                        'role': 'LT'
                    }
                ],
                'thirtyparty': True
            },
            {
                'code': 'datascience',
                'name': 'Data Science',
                'members': [
                    {
                        'name': 'Karin',
                        'role': 'PO'
                    },
                    {
                        'name': 'Chicão',
                        'role': 'LT'
                    }
                ],
                'thirtyparty': False
            }

        ],
        'images': {
            'LT': 'img_url',
            'PO': 'img_url'
        }
    }
