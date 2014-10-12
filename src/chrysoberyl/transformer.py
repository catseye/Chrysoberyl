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


def markdown_contents(contents, prefix=None):
    """Convert the contents of a field containing markdown and Chrysoberyl
    cross-references (indicated with [[double brackets]]) into HTML.

    """
    def linker(match):
        text = match.group(1)
        segments = text.split('|')
        thing = segments[0]
        space = 'node'  # FIXME hardcoded
        spaces = thing.split('/')
        if len(spaces) > 1:
            space = spaces[0]
            thing = spaces[1]
        link_text = thing
        if len(segments) > 1:
            link_text = segments[1]
        return '<a href="%s">%s</a>' % (
            pathname2url((prefix if prefix else '') + filekey(thing)),
            link_text
        )
    html = markdown.markdown(contents)
    html = re.sub(r'\[\[(.*?)\]\]', linker, html)
    return html


def markdown_field(data, node, field, prefix=None):
    if field in node:
        return markdown_contents(node[field], prefix=prefix)
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
