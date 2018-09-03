
# class Member():
#     def __init__(self, data=None):
#         if data:
#             self.name = data['name']
#             self.role = data['role']
#         else:
#             self.name = None
#             self.role = None
    
#     def json(self):
#         return {
#             'name': self.name,
#             'role': self.role
#         }


class Member(object):
    def __init__(self, data=None):
        init_data = {
            'name': None,
            'role': None
        }
        self._data = data if data else init_data

    @property
    def name(self):
        return self._data['name']

    @name.setter
    def name(self, value):
        self._data['name'] = value

    @property
    def role(self):
        return self._data['role']

    @role.setter
    def role(self, value):
        self._data['role'] = value

    def json(self):
        return self._data


class Squad(object):
    def __init__(self, data=None):
        init_data = {
            'name': None,
            'code': None,
            'thirtyparty': None,
            'members': []
        }
        self._data = data if data else init_data
        self._members = [Member(member) for member in self._data['members']]

    @property
    def members(self):
        return self._members

    def add_member(self, member):
        self._members.append(member)
        self._data['members'].append(member.json())

    @property
    def thirtyparty(self):
        return self._data['thirtyparty']

    @thirtyparty.setter
    def thirtyparty(self, value):
        self._data['thirtyparty'] = value

    @property
    def name(self):
        return self._data['name']

    @name.setter
    def name(self, value):
        self._data['name'] = value

    @property
    def code(self):
        return self._data['code']

    @code.setter
    def code(self, value):
        self._data['code'] = value

    def json(self):
        return self._data


class DataHandler(object):
    def __init__(self, data):
        self._data = data

    def add(self, name, data):
        self._data[name] = data

    def __getattr__(self, item):
        """ Permite acessar valores do dict self._data como se fossem
        attributos de um objeto do tipo DataHandler"""
        if item in self._data:
            return self._data[item]
        raise Exception('Item not found')



class OrganizationChart(object):
    def __init__(self, data):
        self._data = data
        self._squads = DataHandler({})
        self._deserialize()

    def _deserialize(self):
        squads = self._data['squads']
        for s in squads:
            self._squads.add(s['code'], Squad(s))

    def json(self):
        return self._data

    @property
    def squads(self):
        return self._squads
