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
    resp.json == populated_storage['squads']
