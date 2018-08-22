import pytest
from webtest import TestApp

from pyramid import paster  # Pyramid object to read config files.
from pyramid import testing  # Pyramid object to create test config

from squads import main  # Our "create application" function
from squads.storage.mongodb import mongo as mongo_


settings = paster.get_appsettings('testing.ini', name='main')
config = testing.setUp(settings=settings)

app_ = main(config, **settings)
mongo_.configure(settings)


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
                'name': 'Consig',
                'membros': [
                    {
                        'name': 'Ana',
                        'papel': 'PO'
                    },
                    {
                        'name': 'Flávio',
                        'papel': 'LT'
                    }
                ],
                'terceiros': True
            },
            {
                'name': 'Originação',
                'membros': [
                    {
                        'name': 'Adriana',
                        'papel': 'PO'
                    },
                    {
                        'name': 'Debonzi',
                        'papel': 'LT'
                    }
                ],
                'terceiros': True
            },
            {
                'name': 'Data Science',
                'membros': [
                    {
                        'name': 'Karin',
                        'papel': 'PO'
                    },
                    {
                        'name': 'Chicão',
                        'papel': 'LT'
                    }
                ],
                'terceiros': True
            }

        ],
        'images': {
            'LT': 'img_url',
            'PO': 'img_url'
        }
    }
