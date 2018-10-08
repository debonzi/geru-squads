from pyramid import httpexceptions
from pyramid.view import view_config, view_defaults

from squads.elements import (
    OrganizationChart,
    Squad,
    Member
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


    @view_config(route_name='squads', request_method='GET')
    def get_squads(self):
        return [s.json() for s in self.org_chart.squads]

    @view_config(route_name='squads', request_method='POST')
    def post_squads(self):
        """
        {
            "code": <slug>,
            "name": <squad name>
            "thirtyparty": True|False
        }
        """
        code = self.request.json['code']
        name = self.request.json['name']
        thirtyparty = self.request.json['thirtyparty']

        # Create a new squad
        squad = Squad()
        squad.code = code
        squad.name = name
        squad.thirtyparty = thirtyparty

        # if hasattr(self.org_chart.squads, code):
        #     self.request.response.status_code = 409
        #     return {}

        # Add squad to the current organization chart
        self.org_chart.add_squad(squad)

        # Save the new organization chart
        squads_storage.save(self.org_chart.json())

        # Change result code to created (201)
        self.request.response.status_code = 201

        # Return created squad
        return squad.json()

    @view_config(route_name='squad', request_method='GET')
    def get_squad(self):
        squad = self._get_squad_or_404()
        return squad.json()

    @view_config(route_name='squad', request_method='PUT')
    def put_squad(self):
        """
        {
            "thirtyparty": True|False
        }
        """
        squad = self._get_squad_or_404()
        thirtyparty = self.request.json['thirtyparty']

        squad.thirtyparty = thirtyparty
        squads_storage.save(self.org_chart.json())

        return squad.json()

    @view_config(route_name='members', request_method='GET')
    def get_members(self):
        squad = self._get_squad_or_404()
        return [m.json() for m in squad.members]

    @view_config(route_name='members', request_method='POST')
    def post_members(self):
        squad = self._get_squad_or_404()
        _json = self.request.json
        if 'name' not in _json or 'role' not in _json:
            raise httpexceptions.HTTPBadRequest()
        member = Member(_json)
        squad.add_member(member)

        squads_storage.save(self.org_chart.json())

        self.request.response.status_code = 201
        return member.json()

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

    @view_config(route_name='images', request_method='GET')
    def get_images(self):
        return self.org_chart.images

    @view_config(route_name='images', request_method='PUT')
    def put_images(self):
        for role, path in self.request.json.items():
            self.org_chart.add_image(role, path)

        squads_storage.save(self.org_chart.json())

        return self.org_chart.images
