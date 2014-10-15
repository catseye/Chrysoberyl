# encoding: UTF-8

"""Functions for transforming Chrysoberyl data (typically loaded from Yaml
files) into a form suitable for rendering in Jinja2 templates.

"""

import re

import markdown

from chrysoberyl.checker import ApproximateDate


def filekey(key):
    """Convert a key into a form that can be used as a filename."""
    key = re.sub(r'(\/|\\|\#)', '_', key)
    return key + ".html"


def sleek_key(key):
    """Convert a key into a form that can be used as a 'sleek' node link."""
    return re.sub(r'(\/|\\|\#| )', '_', key)


def pathname2url(s):
    """Convert a filename into a form that can be used as a link in an
    HTML document.

    """
    # we wrote our own because urllib.pathname2url doesn't handle Unicode well
    # and actually, ours is just quote, no pathname functionality
    s = re.sub('\%', '%25', s)
    s = re.sub(' ', '%20', s)
    s = re.sub('\"', '%22', s)
    s = re.sub('\#', '%23', s)
    s = re.sub('\:', '%3a', s)
    s = re.sub('\?', '%3f', s)
    return s


def link(universe, key, link_text, title=None, sleek=False, extra_attr='', prefix='../'):
    (space, key, node) = universe.get_space_key_node(key)
    type_ = node['type']
    if self.universe.get_node(type_).get('suppress-page-generation', False):
        raise KeyError('link to non-page (%s) node %s' % (type_, key))
    title_attr = ''
    if title is not None:
        title_attr = ' title="%s"' % title
    if sleek:
        href = pathname2url(preifx + space.name + '/' + sleek_key(key))
    else:
        href = pathname2url(prefix + space.name + '/' + filekey(key))
    return '<a %shref="%s"%s>%s</a>' % (
        extra_attr, href, title_attr, link_text
    )


def markdown_contents(universe, contents, prefix=None):
    """Convert the contents of a field containing markdown and Chrysoberyl
    cross-references (indicated with [[double brackets]]) into HTML.

    """
    def linker(match):
        text = match.group(1)
        segments = text.split('|')
        if len(segments) == 1:
            segments.append(segments[0])  # omg
        return link(universe, segments[0], segments[1], prefix=prefix)
    html = markdown.markdown(contents)
    html = re.sub(r'\[\[(.*?)\]\]', linker, html)
    return html


def markdown_field(universe, data, node, field, prefix=None):
    if field in node:
        return markdown_contents(universe, node[field], prefix=prefix)
    else:
        return None


def transform_dates(thing):
    """Recursively convert dates in the given Python object into a form
    suitable for JSON.

    """
    if isinstance(thing, ApproximateDate):
        return thing.stamp()
    elif isinstance(thing, list):
        return [transform_dates(x) for x in thing]
    elif isinstance(thing, dict):
        return dict([(k, transform_dates(v)) for k, v in thing.iteritems()])
    else:
        return thing
