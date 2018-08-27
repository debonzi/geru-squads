from squads.elements import OrganizationChart, DataHandler, Squad
from squads.elements import Member

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

def test_create_organization_chart():
    flavio = Member()
    flavio.name = 'Flávio'
    assert flavio._data['name'] == 'Flávio'
    flavio.role = 'TL'
    # ana = Member()
    # ana.name = 'Ana'
    # ana.role = 'PO'
