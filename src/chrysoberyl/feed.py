import atomize
import datetime
from operator import itemgetter

URL = 'http://catseye.tc/feeds/news.xml'

def make_news_feed(data, filename):
    newses = []
    for key in data:
        node = data[key]
        if node['type'] != 'News Item':
            continue
        # Tue, 17 May 2011 23:43:10 GMT
        news_date = datetime.datetime.strptime(
            node['news-date'], "%a, %d %b %Y %H:%M:%S GMT"
        )
        n = {}
        n.update(node)
        n['key'] = key
        n['news-date'] = news_date
        n['description_html'] = \
            n['description_html'].encode("ascii", "xmlcharrefreplace") 
        newses.append(n)

    newses.sort(key=itemgetter('news-date'), reverse=True)
    entries = [atomize.Entry(title=n['key'],
                             guid=URL + "/" + n['key'],
                             updated=n['news-date'],
                             summary=atomize.Summary(n['description_html'], content_type='html'),
                             links=[atomize.Link(n['news-link'], content_type='text/html', rel='alternate')])
               for n in newses]

    feed = atomize.Feed(title="Cat's Eye Technologies: New Developments",
                        updated=datetime.datetime.utcnow(),
                        guid=URL,
                        author='Chris Pressey',
                        self_link=URL,
                        entries=entries)

    feed.write_file(filename)
