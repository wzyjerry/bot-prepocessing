import json
from urllib import request
template = 'http://166.111.5.228:8765/v1/agent/%s/entity/%s?api_key=%s'
agent = '5bfe0b04c4952f342f394a42'
entities = [
    '5bfe0ef9c4952f342f394a44',
    '5bfe111cc4952f342f394a45',
    '5bfe127cc4952f342f394a47',
    '5bfe132cc4952f342f394a48',
    '5bfe137dc4952f342f394a49',
    '5bfe2702c4952fd462c4af3f',
    '5c3d7d0ec4952fa7a503edb7',
    '5c3d7d22c4952fa7a503edb8',
    '5c3d7d40c4952fa7a503edb9',
    '5c3d7d56c4952fa7a503edba']
api_key = '131c3bd317d49d6260334bf671acbc6c8105f732323ed8f1'

for entity in entities:
    url = template % (agent, entity, api_key)
    req = request.Request(url)
    res = request.urlopen(req)
    data = res.read().decode('utf-8')
    data = json.loads(data)
    with open('data/entities/%s.txt' % data['description'], 'w', encoding='utf-8') as fout:
        for item in data['entries']:
            fout.write('%s\n' % item)
