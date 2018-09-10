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

    def __iter__(self):
        for _, squad in self._data.items():
            yield squad


class OrganizationChart(object):
    def __init__(self, data={}):
        self._squads = DataHandler({})
        self._images = data.get('images', {})
        self._deserialize(data)

    @classmethod
    def create(cls, squads, images={}):
        org_char = cls()
        for s in squads:
            org_char.add_squad(s)
        for iname, ipath in images.items():
            org_char.add_image(iname, ipath)
        return org_char

    def _deserialize(self, data):
        squads = data.get('squads', [])
        for s in squads:
            self.add_squad(s)

    def json(self):
        return {
            'squads': [s.json() for s in self._squads],
            'images': self._images
        }

    def add_squad(self, squad):
        if isinstance(squad, Squad):
            self._squads.add(squad.code, squad)
        else:
            self._squads.add(squad['code'], Squad(squad))

    def add_image(self, role, path):
        self._images[role] = path

    @property
    def squads(self):
        return self._squads
