import json

from feedmark.checkers import Schema
from feedmark.formats.markdown import feedmark_markdownize
from feedmark.loader import read_document_from, read_refdex_from


def document_name(title):
    if title == 'News':
        return "NEWS.md"
    else:
        return "article/{}.md".format(title)


def rewrite_documents(articles, refdex):
    for title, schema in articles:
        if title in ('News',):
            continue
        print("{}...".format(title))
        filename = document_name(title)
        document = read_document_from(filename)
        document.rewrite_reference_links(refdex)

        if schema:
            schema_document = read_document_from("schema/{}.md".format(schema))
            schema = Schema(schema_document)
            results = schema.check_documents([document])
            if results:
                raise ValueError(json.dumps(results, indent=4, sort_keys=True))

        text = feedmark_markdownize(document, schema=schema)
        with open(document.filename, 'w') as f:
            f.write(text.encode('UTF-8'))


def accumulate_article_refdex(articles, refdex):
    for title, schema in articles:
        if title in ("News", "HTML5 Installations",):
            continue
        print("{}...".format(title))
        filename = document_name(title)
        document = read_document_from(filename)
        for section in document.sections:
            refdex[section.title] = {
                'filename': document.filename,
                'anchor': section.anchor
            }


def regenerate_refdex(articles):
    INPUT_REFDEXES = [
        'misc-refdex/games-refdex.json',
        'misc-refdex/texts-refdex.json',
        'misc-refdex/retrocomputing-refdex.json',
        'misc-refdex/languages-refdex.json',
        'misc-refdex/misc-refdex.json',
    ]
    refdex = read_refdex_from(INPUT_REFDEXES)
    accumulate_article_refdex(articles, refdex)
    with open('refdex.json', 'w') as f:
        f.write(json.dumps(refdex, indent=4, sort_keys=True).encode('UTF-8'))


if __name__ == '__main__':
    articles_doc = read_document_from('article/README.md')
    articles_map = dict([(section.title, {
        "title": section.title,
        "image_url": section.properties.get("image_url"),
        "schema": section.properties.get("schema"),
    }) for section in articles_doc.sections])
    articles = []
    for title, properties in articles_map.items():
        articles.append((title, properties['schema']))

    regenerate_refdex(articles)
    refdex = read_refdex_from(['refdex.json'], input_refdex_filename_prefix='../')
    rewrite_documents(articles, refdex)
