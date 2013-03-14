# encoding: UTF-8

"""Dispatch to the command given on the command-line.

"""

import codecs
import json
from optparse import OptionParser
import os
import re
import sys

from chrysoberyl.checker import check_chrysoberyl_data
from chrysoberyl.feed import make_news_feed
from chrysoberyl.loader import load_chrysoberyl_dirs
from chrysoberyl.localrepos import (
    bitbucket_repos,
    troll_docs, survey_repos, get_latest_release_tag, lint_dists
)
from chrysoberyl.renderer import Renderer
from chrysoberyl.transformer import (
    convert_chrysoberyl_data, transform_dates
)
from chrysoberyl.util import do_it


def check(args, optparser):
    """Check the Chrysoberyl database for consistency.

    """
    options, args = optparser.parse_args(args)
    load_and_check(options.data_dirs.split(':'))
    return 0


def survey(args, optparser):
    """Survey local clones of distributions.

    """
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dirs.split(':'))
    survey_repos(data, options.clone_dir)
    return 0


def lint(args, optparser):
    """Lint local clones of distributions.

    """
    optparser.add_option("--host-language",
                         dest="host_language", metavar='LANG',
                         default=None,
                         help="lint only those distributions containing "
                              "implementations in this language")
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dirs.split(':'))
    lint_dists(data, options.clone_dir, host_language=options.host_language)
    return 0


def troll(args, optparser):
    """Troll local hg clones of distributions listed in Chrysoberyl,
    looking through each distribution for anything that looks like
    documentation, and update documentation.yaml with those
    filenames.

    """
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dirs.split(':'))
    troll_docs(data, options.clone_dir, options.data_dirs.split(':'))
    return 0


def render(args, optparser):
    """Render all nodes to a set of HTML5 files.

    """
    optparser.add_option("--node-dir",
                         dest="node_dir", metavar='DIR',
                         default='../catseye.tc/node',
                         help="write rendered nodes into this directory")
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dirs.split(':'))
    filename = os.path.join(options.node_dir, 'chrysoberyl.json')
    with codecs.open(filename, 'w', 'utf-8') as file:
        json.dump(transform_dates(data), file, encoding='utf-8',
                  default=unicode)
    convert_chrysoberyl_data(data)
    r = Renderer(data,
        options.template_dirs, options.node_dir, options.clone_dir
    )
    r.render_chrysoberyl_data()


def announce(args, optparser):
    """Create news feeds from news item nodes in Chrysoberyl.

    """
    optparser.add_option("--feed-dir",
                         dest="feed_dir", metavar='DIR',
                         default='../catseye.tc/feeds',
                         help="write feeds into this directory")
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dirs.split(':'))
    convert_chrysoberyl_data(data)
    make_news_feed(data, options.feed_dir, 'atom_15_news.xml', limit=15)
    make_news_feed(data, options.feed_dir, 'atom_30_news.xml', limit=30)
    make_news_feed(data, options.feed_dir, 'atom_all_news.xml')


def release(args, optparser):
    """Create a distfile from the latest tag in a local distribution repo.

    """
    optparser.add_option("--distfiles-dir",
                         dest="distfiles_dir", metavar='DIR',
                         default='../catseye.tc/distfiles',
                         help="write distfile into this directory")
    distro = args.pop(0)
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dirs.split(':'))
    tag = get_latest_release_tag(data, distro, options.clone_dir)
    if not tag:
        print "ERROR: repository not tagged"
        return 1
    match = re.match(r'^rel_(\d+)_(\d+)_(\d+)_(\d+)$', tag)
    if not match:
        print "ERROR: not a release tag: %s" % tag
        return 1
    v_maj = match.group(1)
    v_min = match.group(2)
    r_maj = match.group(3)
    r_min = match.group(4)
    filename = '%s-%s.%s-%s.%s.zip' % (distro, v_maj, v_min, r_maj, r_min)
    print """\
  - version: "%s.%s"
    revision: "%s.%s"
    url: http://catseye.tc/distfiles/%s
""" % (v_maj, v_min, r_maj, r_min, filename)
    full_filename = os.path.join(options.distfiles_dir, filename)
    if os.path.exists(full_filename):
        print "ERROR: distfile already exists: %s" % full_filename
        do_it("unzip -v %s" % full_filename)
        return 1
    excludes = ' '.join(['-X %s' % x
                         for x in ('.hgignore', '.gitignore',
                                   '.hgtags', '.hg_archival.txt')])
    cwd = os.getcwd()
    os.chdir(os.path.join(options.clone_dir, distro))
    do_it("hg archive -t zip -r %s %s %s" % (tag, excludes, full_filename))
    os.chdir(cwd)


def catalog(args, optparser):
    """Create a toolshelf catalog from distribution nodes.

    """
    options, args = optparser.parse_args(args)
    data = load_and_check(options.data_dirs.split(':'))
    for (key, user, repo) in bitbucket_repos(data):
        print 'bb:%s/%s' % (user, repo)

### helpers ###


def load_and_check(dirnames):
    print "Loading Chrysoberyl data..."
    data = load_chrysoberyl_dirs(dirnames)
    check_chrysoberyl_data(data)
    return data


### driver ###

COMMANDS = {
    'check': check,
    'render': render,
    'announce': announce,
    'troll': troll,
    'survey': survey,
    'lint': lint,
    'release': release,
    'catalog': catalog,
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
    optparser.add_option("-d", "--data-dirs",
                         dest="data_dirs", metavar='DIRS', default='data',
                         help="colon-separated list of directories "
                              "containing Chrysoberyl Yaml data files "
                              "(default: %default)")
    optparser.add_option("-t", "--template-dirs",
                         dest="template_dirs", metavar='DIRS',
                         default='templates',
                         help="colon-separated list of directories "
                              "containing Chrysoberyl templates "
                              "(default: %default)")

    sys.exit(func(args, optparser))
