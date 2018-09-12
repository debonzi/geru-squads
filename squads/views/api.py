from pyramid import httpexceptions
from pyramid.view import view_config, view_defaults

from squads.elements import (
    OrganizationChart,
    Squad
)
from squads.storage import squads_storage

@view_defaults(renderer='json')
class OrgChartViews:
    def __init__(self, request):
        self.request = request
        self.org_chart = OrganizationChart(squads_storage.latest())

    def _get_squad_or_404(self):
        code = self.request.matchdict.get('code')
        squad = getattr(self.org_chart.squads, code, None)
        if not squad:
            raise httpexceptions.HTTPNotFound()
        return squad


    @view_config(route_name='orgchart')
    def get_org_chart(self):
        return self.org_chart.json()


    @view_config(route_name='squads')
    def get_squads(self):
        return [s.json() for s in self.org_chart.squads]

    @view_config(route_name='squad')
    def get_squad(self):
        squad = self._get_squad_or_404()
        return squad.json()

    @view_config(route_name='members')
    def get_members(self):
        squad = self._get_squad_or_404()
        return [m.json() for m in squad.members]

    @view_config(route_name='member')
    def get_member(self):
        squad = self._get_squad_or_404()
        try:
            index = int(self.request.matchdict.get('index'))
            member = squad.members[index]
        except IndexError:
            raise httpexceptions.HTTPNotFound()
        except ValueError:
            raise httpexceptions.HTTPBadRequest()
        return member.json()
