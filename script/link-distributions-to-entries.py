import re
import json

# generate this with:
# feedmark article/*.md --by-property > by-property.json
with open('by-property.json', 'r') as f:
    data = json.loads(f.read())

newdata = {}
for key in ('defining-distribution', 'reference distribution', 'in distribution', 'reference-distribution', 'in-distribution', 'distribution'):
    subdata = data[key]
    for subkey, value in subdata.items():
        assert subkey not in newdata, subkey
        newdata[subkey] = value

#print json.dumps(newdata, indent=4, sort_keys=True)
#with open('extracted-dists.json', 'r') as f:
#    data = json.loads(f.read())

by_name = {}
for key, value in newdata.iteritems():
    match = re.match(r'^\[(.*?)\]\((.*?)\)', value)
    assert match, value
    name = match.group(1)
    link = match.group(2)
    by_name.setdefault(name, []).append(key)

#print json.dumps(by_name, indent=4, sort_keys=True)

with open('distribution/distributions.json', 'r') as f:
    distributions = json.loads(f.read())

for key, node in distributions.iteritems():
    if key in by_name:
        node['entries'] = by_name[key]

print json.dumps(distributions, indent=4, sort_keys=True)