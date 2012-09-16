# encoding: UTF-8

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


def check(args, optparser):
    """Check the Chrysoberyl database for consistency.

    """
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dir)
    return 0


def survey(args, optparser):
    """Survey repos.

    """
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dir)
    survey_repos(data, options.clone_dir)
    return 0


def troll(args, optparser):
    """Troll local hg clones of distributions listed in Chrysoberyl,
    looking through each distribution for anything that looks like
    documentation, and update documentation.yaml with those
    filenames.

    """
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dir)
    troll_docs(data, options.clone_dir, options.data_dir)
    print "Re-run to incorporate docs in loaded data."
    return 0


def render(args, optparser):
    """Render all nodes to a set of HTML5 files.

    """
    optparser.add_option("--node-dir",
                         dest="node_dir", metavar='DIR',
                         help="write rendered nodes into this directory")
    optparser.add_option("--script-dir",
                         dest="script_dir", metavar='DIR',
                         help="write scripts into this directory")
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dir)
    filename = os.path.join(options.node_dir, 'chrysoberyl.json')
    with codecs.open(filename, 'w', 'utf-8') as file:
        json.dump(jsonify(data), file, encoding='utf-8', default=unicode)
    convert_chrysoberyl_data(data)
    r = Renderer(data, 'templates', options.node_dir)
    r.render_chrysoberyl_data()
    for filename in ['chrysoberyl-query.js']:
        shutil.copy(os.path.join('static', filename),
                    options.script_dir)


def announce(args, optparser):
    """Create news feeds from news item nodes in Chrysoberyl.

    """
    optparser.add_option("--feed-dir",
                         dest="feed_dir", metavar='DIR',
                         help="write feeds into this directory")
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dir)
    convert_chrysoberyl_data(data)
    make_news_feed(data, options.feed_dir, 'atom_15_news.xml', limit=15)
    make_news_feed(data, options.feed_dir, 'atom_30_news.xml', limit=30)
    make_news_feed(data, options.feed_dir, 'atom_all_news.xml')


def release(args, optparser):
    """Create a distfile from the latest tag in a local distribution repo.

    """
    optparser.add_option("--distfiles-dir",
                         dest="distfiles_dir", metavar='DIR',
                         help="write distfile into this directory")
    distro = args.pop(0)
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dir)
    v_maj = '1'
    v_min = '0'
    r_maj = '2012'
    r_min = '0915'
    tag = 'rel_%s_%s_%s_%s' % (v_maj, v_min, r_maj, r_min)
    filename = '%s-%s.%s-%s.%s.zip' % (distro, v_maj, v_min, r_maj, r_min)
    excludes = '-X .hgignore -X .gitignore -X .hg_archival.txt'
    print "hg archive -t zip -r %s %s %s/%s" % (tag, excludes, options.distfiles_dir, filename)
    print """\
  - version: "%s.%s"
    revision: "%s.%s"
    url: http://catseye.tc/distfiles/%s
""" % (v_maj, v_min, r_maj, r_min, filename)

### helpers ###

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


def load_and_check(dirname):
    print "Loading Chrysoberyl data..."
    data = load_chrysoberyl_dir(dirname)
    check_chrysoberyl_data(data)
    return data


### driver ###

COMMANDS = {
    'check': check,
    'render': render,
    'announce': announce,
    'troll': troll,
    'survey': survey,
    'release': release,
}


def usage():
    sys.stderr.write("Usage: chrysoberyl <command> [args...]\n")
    sys.stderr.write("  where <command> is one of:\n")
    for command in sorted(COMMANDS.keys()):
        sys.stderr.write("    %s\n" % command)
    sys.exit(1)


def perform(args):
    try:
        command = args[0]
    except IndexError:
        usage()
    args = args[1:]
    func = COMMANDS.get(command, None)
    if func is None:
        usage()
    message = "chrysoberyl %s [options]\n\n%s" % (command, func.__doc__)
    message = message.rstrip()
    optparser = OptionParser(message)
    optparser.add_option("-c", "--clone-dir",
                         dest="clone_dir", metavar='DIR', default='..',
                         help="specify location of the hg clones "
                              "of reference distributions (default: ..)")
    optparser.add_option("-d", "--data-dir",
                         dest="data_dir", metavar='DIR', default='data',
                         help="specify location of the Chrysoberyl "
                              "Yaml data files (default: data)")

    sys.exit(func(args, optparser))
