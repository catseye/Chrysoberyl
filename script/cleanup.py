import json
import sys
from subprocess import check_output
import re

from feedmark.main import read_document_from
from feedmark.checkers import Schema
from feedmark.formats.markdown import feedmark_htmlize
from feedmark.formats.markdown import feedmark_markdownize


ARTICLES = (
    ('Distribution Organization',                 None,),
    ('Electronics Projects',                      'Electronics Project',),
    ('Games',                                     'Game',),
    ('Game Implementations',                      'Game Implementation',),
    ('List of Unfinished Interesting Esolangs',   'Unfinished Esolang',),
    ('Musical Compositions',                      'Musical Composition',),
    ('Pictures',                                  'Picture',),
    ('Movies',                                    'Movie',),
    ('Retrocomputing',                            None,),
    ('Texts',                                     'Text',),
    ('Tools',                                     'Tool',),
    ('Formats',                                   'Format',),
    ('Platforms',                                 'Platform',),
    ('Archived',                                  'Tool',),
    ('Languages',                                 'Language',),
    ('Language Implementations',                  'Language Implementation',),
    ('Automata',                                  'Language',),
    ('Gewgaws',                                   'Gewgaw',),
    ('Events',                                    'Event',),
    ('General Information',                       None,),
    ('Project Dependencies',                      'Project Dependency',),
    ('HTML5 Installations',                       'HTML5 Installation',),
    ('News',                                      None,),
)


def document_name(title):
    if title == 'News':
        return "NEWS.md"
    else:
        return "article/{}.md".format(title)


def rewrite_documents(refdex):
    for title, schema in ARTICLES:
        print("{}...".format(title))
        filename = document_name(title)
        document = read_document_from(filename)

        # TODO FIXME!
        document.reference_links = rewrite_reference_links(refdex, document.reference_links)
        for section in document.sections:
            section.reference_links = rewrite_reference_links(refdex, section.reference_links)

        if schema:
            schema_document = read_document_from("schema/{}.md".format(schema))
            schema = Schema(schema_document)
            results = schema.check_documents([document])
            if results:
                raise ValueError(json.dumps(results, indent=4, sort_keys=True))

            s = feedmark_markdownize(document, schema=schema)
            with open(document.filename, 'w') as f:
                f.write(s.encode('UTF-8'))


if __name__ == '__main__':

    with codecs.open('refdex.json', 'r', encoding='utf-8') as f:
        refdex = json.loads(f.read())

    rewrite_documents(refdex)
