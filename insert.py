data = {
    'squads': [
        {
            'nome': 'Consig',
            'membros': [
                {
                    'nome': 'Ana',
                    'papel': 'PO'
                },
                {
                    'nome': 'Flávio',
                    'papel': 'LT'
                }
            ],
            'terceiros': True
        },
        {
            'nome': 'Originação',
            'membros': [
                {
                    'nome': 'Adriana',
                    'papel': 'PO'
                },
                {
                    'nome': 'Debonzi',
                    'papel': 'LT'
                }
            ],
            'terceiros': True
        }
    ],
    'images': {
        'LT': 'img_url',
        'PO': 'img_url'
    }
}

from squads.storage import squads_storage

document = squads_storage.save(data)
mongo.db.squads.find_one()