from copy import deepcopy
from squads.storage import SquadsStorage

def test_get_from_empty_collection(squads_storage):
    assert squads_storage.latest() == {}

def test_save_and_get(squads_storage):
    din = {'name': 'test_1'}
    dout = deepcopy(din)
    squads_storage.save(din)
    assert squads_storage.latest() == dout
