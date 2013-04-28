# encoding: UTF-8

"""Functions for generating Atom feeds from news item nodes in Chrysoberyl.

"""

import datetime
from operator import itemgetter
import os

import atomize

from chrysoberyl.transformer import filekey, markdown_field, pathname2url


BASEURL = 'http://catseye.tc/feeds/'


def make_news_feed(data, dir, filename, limit=None):
    """Generate Atom feeds from Article nodes in the given Chrysoberyl
    data.

    """
    url = BASEURL + filename
    filename = os.path.join(dir, filename)
    articles = []
    for key in data:
        node = data[key]
        if node['type'] != 'Article':
            continue
        n = {}
        n.update(node)
        n['key'] = key
        # Note, these are now done differently from how md2html()
        # is done in the templates elsewhere
        for field_name in ('summary', 'description', 'commentary'):
            field = markdown_field(data, node, field_name,
                                   prefix='http://catseye.tc/node/')
            if field is not None:
                n[field_name + '_html'] = field.encode("ascii",
                                                       "xmlcharrefreplace")
        articles.append(n)

    articles.sort(key=itemgetter('publication-date'), reverse=True)
    entries = []
    for n in articles:
        title = n['key']
        guid = url + "/" + n['key']
        updated = n['publication-date']
        nodelink = pathname2url(filekey(n['key']),
                                prefix='http://catseye.tc/node/')
        summary_contents = n['description_html']
        if n.get('summary', None) is not None:
            summary_contents = (n['summary_html'] +
                '<p><a href="%s">Read more...</a></p>' % nodelink)
        summary = atomize.Summary(summary_contents, content_type='html')
        links = [atomize.Link(nodelink, content_type='text/html',
                              rel='alternate')]
        entry = atomize.Entry(title=title, guid=guid, updated=updated,
                              summary=summary, links=links)
        entries.append(entry)

    if limit and len(entries) > limit:
        entries = entries[:limit]

    feed = atomize.Feed(title="Cat's Eye Technologies: New Developments",
                        updated=datetime.datetime.utcnow(),
                        guid=url,
                        author='Chris Pressey',
                        self_link=url,
                        entries=entries)

    feed.write_file(filename)
