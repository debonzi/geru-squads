from squads.elements import OrganizationChart, XDict, Squad


def test_organization_chart_methods(org_chart_data1):
    org_chart = OrganizationChart(org_chart_data1)
    assert org_chart.json() == org_chart_data1
    assert isinstance(org_chart.squads, XDict)
    assert isinstance(org_chart.squads.Consig, Squad)
    """
    Como acessar o squad Data Science se não posso ter metodos com espaco

    org_chart.squads.Data Science não é uma sintaxe válida.
    """
