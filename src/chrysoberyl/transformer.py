# encoding: UTF-8

def convert_chrysoberyl_data(data):
    """Prep for Jinja/HTML5"""
    count = 0
    for key in data:
        count += 1
        node = data[key]
        new_fields = {}
        for field in node.keys():
            new_fields[field.replace('-', '_')] = node[field]
        node.update(new_fields)
        for field in ('description', 'commentary', 'as_a_prerequisite'):
            node[field + '_html'] = markdown_field(data, node, field)
        if 'sample' in node:
            node['sample_html'] = markdown.markdown(
                '\n'.join(['    ' + l for l in node['sample'].split('\n')])
            )
            
    print "%d nodes converted." % count


def transform_dates(thing):
    """Prep for json"""
    if isinstance(thing, ApproximateDate):
        return thing.stamp()
    elif isinstance(thing, list):
        return [transform_dates(x) for x in thing]
    elif isinstance(thing, dict):
        return dict([(k, transform_dates(v)) for k, v in thing.iteritems()])
    else:
        return thing
