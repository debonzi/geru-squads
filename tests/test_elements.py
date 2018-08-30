from squads.elements import (
    OrganizationChart, DataHandler, Squad, Member
)

def test_organization_chart_methods(org_chart_data1):
    org_chart = OrganizationChart(org_chart_data1)
    assert org_chart.json() == org_chart_data1
    assert isinstance(org_chart.squads, DataHandler)
    assert isinstance(org_chart.squads.consig, Squad)
    assert org_chart.squads.consig.thirtyparty is True
    assert org_chart.squads.datascience.thirtyparty is False
    assert isinstance(org_chart.squads.consig.members, list)

    assert len(org_chart.squads.consig.members) == 2

    for m in org_chart.squads.consig.members:
        assert {
            'name': m.name, 'role': m.role
        } in org_chart_data1['squads'][0]['members']

def test_create_member():
    flavio = Member()
    flavio.name = 'Flávio'
    flavio.role = 'TL'
    ana = Member()
    ana.name = 'Ana'
    ana.role = 'PO'
    assert flavio.json() == {'name': 'Flávio', 'role': 'TL'}
    assert ana.json() == {'name': 'Ana', 'role': 'PO'}

def test_create_squads():
    consig = Squad()
    consig.name = 'Crédito Consignado'
    assert consig.name == 'Crédito Consignado'
    consig.code = 'consig'
    assert consig.code == 'consig'
    consig.thirtyparty = True
    assert consig.thirtyparty == True
    assert consig.members == []
    flavio = Member()
    flavio.name = 'Flávio'
    flavio.role = 'TL'
    consig.add_member(flavio)
    assert flavio in consig.members
    assert consig._data == {
        'name': 'Crédito Consignado',
        'code': 'consig',
        'members': [{'name': 'Flávio', 'role': 'TL'}],
        'thirtyparty': True
    }


