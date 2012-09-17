# encoding: UTF-8

import re

import markdown

from chrysoberyl.checker import ApproximateDate


def filekey(key):
    key = re.sub(r'(\/|\\)', '_', key)
    return key + ".html"


def pathname2url(s, prefix=None):
    s = re.sub('\%', '%25', s)
    s = re.sub(' ', '%20', s)
    s = re.sub('\"', '%22', s)
    s = re.sub('\#', '%23', s)
    s = re.sub('\:', '%3a', s)
    s = re.sub('\?', '%3f', s)
    if prefix:
        return prefix + s
    return s


def markdown_field(data, node, field, prefix=None):
    def linker(match):
        text = match.group(1)
        segments = text.split('|')
        thing = segments[0]
        link_text = thing
        if len(segments) > 1:
            link_text = segments[1]
        return '<a href="%s">%s</a>' % (
            pathname2url(filekey(thing), prefix=prefix), link_text
        )
    if field in node:
        html = markdown.markdown(node[field])
        html = re.sub(r'\[\[(.*?)\]\]', linker, html)
        return html
    else:
        return None


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
        for field in ('description', 'commentary'):
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
