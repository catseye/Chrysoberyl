# encoding: UTF-8

"""Parse command line and execute the command(s) given on it.

"""

import codecs
import json
from optparse import OptionParser
import os
import sys

from chrysoberyl.checker import check_chrysoberyl_data
from chrysoberyl.feed import make_news_feed
from chrysoberyl.loader import (
    load_chrysoberyl_dirs, load_config, overlay_yaml
)
from chrysoberyl.objects import Universe
from chrysoberyl.renderer import Renderer
from chrysoberyl.transformer import transform_dates


# experimental loose toolshelf integration
if 'TOOLSHELF' in os.environ and os.environ['TOOLSHELF']:
    sys.path.insert(0, os.path.join(os.environ['TOOLSHELF'], '.toolshelf', 'src'))
    import toolshelf
else:
    toolshelf = None


# helper function
def bitbucket_repos(space):
    """Generator which yields information about every Mercurial repository
    on Bitbucket referenced by some distribution in Chrysoberyl.

    Information is a triple of the distribution key, the Bitbucket username,
    and the repository name.

    """
    for key, node in space.iteritems():
        if node['type'] != 'Distribution':
            continue
        if 'bitbucket' not in node:
            continue
        (user, repo) = node['bitbucket'].split('/')
        yield (key, user, repo)


def filterdocs(universe, options, config):
    """Kind of a stopgap measure for now..."""
    filename = os.path.join(config['node']['docs_dir'], 'docs.yaml')
    docs = load_docs(filename)
    new_docs = {}
    space = universe['node']  # FIXME hardcoded
    for (key, user, repo) in bitbucket_repos(space):
        doc_key = "bitbucket.org/%s/%s" % (user, repo)
        if doc_key in docs:
            new_docs[key] = sorted(docs[doc_key])
    save_docs(filename, new_docs)


def render(universe, options, config):
    """Render all nodes to a set of HTML5 files.

    """
    for space in universe.spaces:
        space.convert_chrysoberyl_data()
        r = Renderer(universe, space,
            config[space.name]['template_dirs'],
            config[space.name]['output_dir'],
            options.clone_dir,
            options.sleek_node_links,
        )
        r.render_chrysoberyl_data()


def jsonify(universe, options, config):
    """Render all nodes to a JSON blob.

    """
    json_data = {}
    space = universe['node']  # FIXME hardcoded
    for (key, node) in space.iteritems():
        if not node.get('hidden', False):
            json_data[key] = node
    filename = os.path.join(config['node']['output_dir'], 'chrysoberyl.json')
    with codecs.open(filename, 'w', 'utf-8') as file:
        json.dump(transform_dates(json_data), file, encoding='utf-8',
                  default=unicode)


def announce(universe, options, config):
    """Create news feeds from news item nodes in Chrysoberyl.

    """
    space = universe['node']  # FIXME hardcoded
    space.convert_chrysoberyl_data()
    feed_dir = config['node']['feed_dir']
    make_news_feed(universe, space, feed_dir, 'atom_15_news.xml', limit=15)
    make_news_feed(universe, space, feed_dir, 'atom_30_news.xml', limit=30)
    make_news_feed(universe, space, feed_dir, 'atom_all_news.xml')


def catalog(universe, data, options, config):
    """Create a toolshelf catalog from distribution nodes.

    """
    for (key, user, repo) in bitbucket_repos(data):
        print 'bb:%s/%s' % (user, repo)


### driver ###

COMMANDS = {
    'render': render,
    'jsonify': jsonify,
    'announce': announce,
    'filterdocs': filterdocs,
    'catalog': catalog,
}


def usage():
    message = "chrysoberyl {option} {<command>}\n\n"
    message += "where each <command> is one of the following.  All commands\n"
    message += "will be executed in the sequence in which they were given,\n"
    message += "after the Chrysoberyl data has been loaded and statically checked.\n"
    for command in sorted(COMMANDS.keys()):
        message += "\n  %s - " % command
        message += COMMANDS[command].__doc__.rstrip()
    return message


def perform(args):
    optparser = OptionParser(usage().rstrip())
    optparser.add_option("-c", "--clone-dir",
                         dest="clone_dir", metavar='DIR', default='..',
                         help="specify location of the hg clones "
                              "of reference distributions "
                              "(default: %default)")
    optparser.add_option("--config",
                         dest="config", metavar='FILE', default='config.yaml',
                         help="specify the config file to use "
                              "(default: %default)")
    optparser.add_option("--host-language",
                         dest="host_language", metavar='LANG',
                         default=None,
                         help="(for lint) lint only those distributions "
                              "containing implementations in this language")
    optparser.add_option("--output-doc-yaml-to",
                         dest="output_filename", metavar='FILENAME',
                         default=None,
                         help="(for troll) write updated documentation yaml here")
    optparser.add_option("--sleek-node-links",
                         dest="sleek_node_links", default=False,
                         action='store_true',
                         help="render links to nodes using Mediawiki-ish "
                              "URLs (requires web server that understands "
                              "what nodes these refer to)")

    options, args = optparser.parse_args(args)

    config = load_config(options.config)

    universe = Universe()

    for key in config.keys():
        try:
            os.makedirs(config[key]['output_dir'])
        except OSError:
            pass
        print "Loading Chrysoberyl '%s' data..." % key
        space = universe.create_namespace(key)
        load_chrysoberyl_dirs(space, config[key]['data_dirs'])
        for filename in config[key].get('overlay_files', []):
            overlay_yaml(filename, space)

    for key in config.keys():
        check_chrysoberyl_data(universe, universe[key])

    for command in args:
        func = COMMANDS.get(command, None)
        if func is None:
            sys.stderr.write("Usage: " + usage() + '\n')
            sys.exit(1)
        print "Executing '%s'..." % command
        # it's expected that func will just raise an exc if it fails
        func(universe, options, config)
