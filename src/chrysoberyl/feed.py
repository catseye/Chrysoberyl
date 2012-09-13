import atomize
import datetime

URL = 'http://catseye.tc/feeds/news.xml'

def make_news_feed(data, filename):
    entries = []
    for key in data:
        node = data[key]
        if node['type'] != 'News Item':
            continue
        # Tue, 17 May 2011 23:43:10 GMT
        news_date = datetime.datetime.strptime(
            node['news-date'], "%a, %d %b %Y %H:%M:%S GMT"
        )
        entry = atomize.Entry(title=key,
                              guid=URL + "/" + key,
                              updated=news_date)
        entries.append(entry)

    feed = atomize.Feed(title="Cat's Eye Technologies: New Developments",
                        updated=datetime.datetime.utcnow(),
                        guid=URL,
                        author='Chris Pressey',
                        self_link=URL,
                        entries=entries)

    feed.write_file(filename)
