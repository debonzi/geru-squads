def test_root_empty(testapp, mongodb): # mongodb para zera as collections
    resp = testapp.get('/')
    assert resp.status_code == 200
    assert resp.json == {'squads': [], 'images': {}}


def test_root_data(testapp, populated_storage):
    resp = testapp.get('/')
    assert resp.status_code == 200
    assert resp.json == populated_storage


def test_squads(testapp, populated_storage):
    resp = testapp.get('/api/v1/squads')
    assert resp.json == populated_storage['squads']

def test_create_squad(testapp, mongodb):
    data = {
        "code": "consig" ,
        "name": "Geru Consignado",
        "thirtyparty": True
    }

    resp = testapp.post_json('/api/v1/squads', data)
    assert resp.status_code == 201
    assert resp.json == {
        "code": "consig" ,
        "name": "Geru Consignado",
        "thirtyparty": True,
        "members": []
    }

# def test_create_duplicate_squad(testapp, mongodb):
#     data = {
#         "code": "consig" ,
#         "name": "Geru Consignado",
#         "thirtyparty": True
#     }

#     resp1 = testapp.post_json('/api/v1/squads', data)

#     resp2 = testapp.post_json('/api/v1/squads', data)

#     assert resp2.status_code == 409
#     assert resp2.json == {}

def test_put_on_squad(testapp, mongodb):
    data = {
        "code": "consig" ,
        "name": "Geru Consignado",
        "thirtyparty": True
    }

    resp = testapp.post_json('/api/v1/squads', data)
    assert resp.status_code == 201

    resp = testapp.put_json('/api/v1/squads/consig', {"thirtyparty": False})
    assert resp.status_code == 200
    assert resp.json == {
        "code": "consig" ,
        "name": "Geru Consignado",
        "thirtyparty": False,
        "members": []
    }

    resp = testapp.get('/api/v1/squads/consig')
    assert resp.json == {
        "code": "consig" ,
        "name": "Geru Consignado",
        "thirtyparty": False,
        "members": []
    }

def test_create_member(testapp, mongodb):
    data = {
        "code": "consig" ,
        "name": "Geru Consignado",
        "thirtyparty": True
    }

    resp = testapp.post_json('/api/v1/squads', data)

    data = {
        'name': 'Adriana',
        'role': 'PO'
    }

    resp = testapp.post_json('/api/v1/squads/consig/members', data)
    assert resp.status_code == 201
    assert resp.json == data

def test_create_member_bad_json(testapp, mongodb):
    data = {
        "code": "consig" ,
        "name": "Geru Consignado",
        "thirtyparty": True
    }

    resp = testapp.post_json('/api/v1/squads', data)

    data = {
        'nam': 'Adriana',
        'bla': 'PO'
    }

    resp = testapp.post_json('/api/v1/squads/consig/members', data, status=400)
    assert resp.status_code == 400


def test_get_images(testapp, mongodb, populated_storage):
    resp = testapp.get('/api/v1/images')
    assert resp.status_code == 200
    assert resp.json == {
        'LT': 'img_url',
        'PO': 'img_url'
    }


def test_put_image(testapp, mongodb):
    images_data = {
        'PO': 'po_url',
        'LT': 'lt_url'
    }
    resp = testapp.put_json('/api/v1/images', images_data)
    assert resp.status_code == 200
    assert resp.json == images_data
    assert testapp.get('/api/v1/images').json == images_data

def test_change_image(testapp, mongodb, populated_storage):
    images_data = {
        'PO': 'po_url'
    }
    resp = testapp.put_json('/api/v1/images', images_data)
    get_resp = testapp.get('/api/v1/images')

    assert resp.status_code == 200
    assert resp.json != images_data
    assert testapp.get('/api/v1/images').json != images_data
    assert get_resp.json == {
        'PO': 'po_url',
        'LT': 'img_url'
    }
