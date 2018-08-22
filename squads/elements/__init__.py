# {
#     'squads': [
#         {
#             'nome': 'Consig',
#             'membros': [
#                 {
#                     'nome': 'Ana',
#                     'papel': 'PO'
#                 },
#                 {
#                     'nome': 'Flávio',
#                     'papel': 'LT'
#                 }
#             ],
#             'terceiros': True
#         },
#         {
#             'nome': 'Originação',
#             'membros': [
#                 {
#                     'nome': 'Adriana',
#                     'papel': 'PO'
#                 },
#                 {
#                     'nome': 'Debonzi',
#                     'papel': 'LT'
#                 }
#             ],
#             'terceiros': True

#         }
#     ],
#     'images': {
#         'LT': 'img_url',
#         'PO': 'img_url'
#     }    
# }

class Squad(object):
    def __init__(self, data):
        self._data = data


class XDict(object):
    def __init__(self, data):
        self._data = data

    def add(self, name, data):
        self._data[name] = data

    def __getattr__(self, item):
        """ Permite acessar valores do dict self._data como se fossem
        attributos de um objeto do tipo XDict"""
        if item in self._data:
            return self._data[item]
        raise Exception('Item not found')



class OrganizationChart(object):
    def __init__(self, data):
        self._data = data
        self._squads = XDict({})
        self._deserialize()

    def _deserialize(self):
        squads = self._data['squads']
        for s in squads:
            self._squads.add(s['name'], Squad(s))

    def json(self):
        return self._data

    @property
    def squads(self):
        return self._squads
