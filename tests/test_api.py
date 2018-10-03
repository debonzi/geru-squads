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
