import datetime
from operator import itemgetter
import os

import atomize

from chrysoberyl.transformer import filekey, markdown_field, pathname2url


BASEURL = 'http://catseye.tc/feeds/'

def make_news_feed(data, dir, filename, limit=None):
    url = BASEURL + filename
    filename = os.path.join(dir, filename)
    newses = []
    for key in data:
        node = data[key]
        if node['type'] != 'News Item':
            continue
        news_date = node['news-date']
        n = {}
        n.update(node)
        n['key'] = key
        n['news-date'] = news_date
        for field_name in ('description', 'commentary'):
            field = markdown_field(data, node, field_name,
                                   prefix='http://catseye.tc/node/')
            if field is not None:
                n[field_name + '_html'] = field.encode("ascii",
                                                       "xmlcharrefreplace")
        newses.append(n)

    newses.sort(key=itemgetter('news-date'), reverse=True)
    entries = []
    for n in newses:
        title = n['key']
        guid = url + "/" + n['key']
        updated = n['news-date']
        summary = atomize.Summary(n['description_html'], content_type='html')
        nodelink = pathname2url(filekey(n['key']),
                                prefix='http://catseye.tc/node/')
        links = [atomize.Link(nodelink, content_type='text/html', rel='alternate')]
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
