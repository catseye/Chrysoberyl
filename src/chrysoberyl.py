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

from chrysoberyl.checker import check_chrysoberyl_data
from chrysoberyl.feed import make_news_feed
from chrysoberyl.renderer import convert_chrysoberyl_data, Renderer
from chrysoberyl.localrepos import troll_docs, bitbucket_repos


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
                              "write them, and supporting materials, "
                              "into the given directory")
    optparser.add_option("--troll-docs",
                         dest="troll_docs", action='store_true',
                         default=False,
                         help="assume that hg clones of reference "
                              "distributions are available in DIR, and look "
                              "through each reference distribution for "
                              "anything that looks like documentation, and "
                              "update documentation.yaml with those "
                              "filenames.")
    optparser.add_option("--display-repos",
                         dest="display_repos", action='store_true',
                         default=False)
    (options, args) = optparser.parse_args(sys.argv[1:])

    print "Loading Chrysoberyl data..."
    data = load_chrysoberyl_dir(options.data_dir)
    check_chrysoberyl_data(data)

    if options.check_links:
        raise NotImplementedError

    if options.display_repos:
        repos = []
        for (dist, user, repo) in bitbucket_repos(data):
            repos.append(repo)
        print '\n'.join(sorted(repos))
        sys.exit(0)

    if options.troll_docs:
        troll_docs(data, options.clone_dir, options.data_dir)
        print "Re-run to incorporate docs in loaded data."
        sys.exit(0)

    if options.output_to:
        filename = os.path.join(options.output_to, 'chrysoberyl.json')
        with codecs.open(filename, 'w', 'utf-8') as file:
            json.dump(data, file, encoding='utf-8', default=unicode)
        convert_chrysoberyl_data(data)
        r = Renderer(data, 'templates', options.output_to)
        r.render_chrysoberyl_data()
        for filename in ['chrysoberyl-query.js']:
            shutil.copy("static/%s" % filename, options.output_to)
        make_news_feed(data, os.path.join(options.output_to, 'news.xml'))
