#!/usr/bin/env python
# encoding: UTF-8

"""
A script to process the Chrysoberyl database.

If no options are given, the database will simply be loaded and checked
for consistency.\
"""

import codecs
import json
from optparse import OptionParser
import os
import shutil
import sys

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from chrysoberyl.checker import check_chrysoberyl_data, ApproximateDate
from chrysoberyl.feed import make_news_feed
from chrysoberyl.renderer import convert_chrysoberyl_data, Renderer
from chrysoberyl.localrepos import troll_docs, survey_repos, test_repos


def load_chrysoberyl_dir(dirname):
    data = {}

    count = 0
    for root, dirnames, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.endswith('.yaml'):
                count += 1
                file = open(os.path.join(root, filename))
                data.update(yaml.load(file, Loader=Loader))
                file.close()
        del dirnames[:]  # don't automatically descend

    print "%d files read." % count
    return data


def transform_dates(thing):
    if isinstance(thing, ApproximateDate):
        return thing.stamp()
    elif isinstance(thing, list):
        return [transform_dates(x) for x in thing]
    elif isinstance(thing, dict):
        return dict([(k, transform_dates(v)) for k, v in thing.iteritems()])
    else:
        return thing


def jsonify(data):
    return transform_dates(data)


if __name__ == '__main__':
    optparser = OptionParser("[python] chrysoberyl.py {options}\n" + \
                             __doc__)
    optparser.add_option("-c", "--clone-dir",
                         dest="clone_dir", metavar='DIR', default='..',
                         help="specify location of the hg clones "
                              "of reference distributions (default: ..)")
    optparser.add_option("-d", "--data-dir",
                         dest="data_dir", metavar='DIR', default='data',
                         help="specify location of the Chrysoberyl "
                              "Yaml data files (default: data)")
    optparser.add_option("-l", "--check-links",
                         dest="check_links", action='store_true',
                         default=False,
                         help="check all web links for sanity "
                              "(no 404's, etc.)")
    optparser.add_option("-o", "--output-to",
                         dest="output_to", metavar='DIR',
                         help="render all nodes (as HTML5 files) and "
                              "write them into the given directory")
    optparser.add_option("--script-dir",
                         dest="script_dir", metavar='DIR',
                         help="write scripts into the given directory")
    optparser.add_option("--feed-dir",
                         dest="feed_dir", metavar='DIR',
                         help="write feeds into the given directory")
    optparser.add_option("--troll-docs",
                         dest="troll_docs", action='store_true',
                         default=False,
                         help="assume that hg clones of reference "
                              "distributions are available in DIR, and look "
                              "through each reference distribution for "
                              "anything that looks like documentation, and "
                              "update documentation.yaml with those "
                              "filenames.")
    optparser.add_option("--survey-repos",
                         dest="survey_repos", action='store_true',
                         default=False)
    (options, args) = optparser.parse_args(sys.argv[1:])

    print "Loading Chrysoberyl data..."
    data = load_chrysoberyl_dir(options.data_dir)
    check_chrysoberyl_data(data)

    if options.check_links:
        raise NotImplementedError

    if options.survey_repos:
        survey_repos(data, options.clone_dir)
        sys.exit(0)

    if options.troll_docs:
        troll_docs(data, options.clone_dir, options.data_dir)
        print "Re-run to incorporate docs in loaded data."
        sys.exit(0)

    if options.output_to:
        filename = os.path.join(options.output_to, 'chrysoberyl.json')
        with codecs.open(filename, 'w', 'utf-8') as file:
            json.dump(jsonify(data), file, encoding='utf-8', default=unicode)
        convert_chrysoberyl_data(data)
        r = Renderer(data, 'templates', options.output_to)
        r.render_chrysoberyl_data()
        for filename in ['chrysoberyl-query.js']:
            shutil.copy(os.path.join('static', filename),
                        options.script_dir)
      
    if options.feed_dir:
        make_news_feed(data, options.feed_dir, 'atom_15_news.xml', limit=15)
        make_news_feed(data, options.feed_dir, 'atom_30_news.xml', limit=30)
        make_news_feed(data, options.feed_dir, 'atom_all_news.xml')
