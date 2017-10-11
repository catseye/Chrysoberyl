# encoding: UTF-8

"""Parse command line and execute the command(s) given on it.

"""

import codecs
import json
from optparse import OptionParser
import os
import re
import sys

from chrysoberyl.checker import check_chrysoberyl_data
from chrysoberyl.loader import (
    load_chrysoberyl_dirs, load_config, overlay_yaml
)
from chrysoberyl.objects import Universe, get_distname
from chrysoberyl.renderer import Renderer
from chrysoberyl.transformer import transform_dates


### command functions ###

def mkdistmap(universe, options, config):
    """Create a mapping between nodes and distributions."""
    space = universe['node']  # FIXME hardcoded
    dist = {}
    for (key, user, repo) in space.github_repos():
        dist[key] = (user, repo)

    repo_to_node = {}
    for key, node in space.iteritems():
        distribution = None

        if 'defining-distribution' in node:
            distribution = node['defining-distribution']
        else:
            ref_impl = space.reference_implementation_of(key)
            if ref_impl is not None:
                if 'in-distributions' in space[ref_impl]:
                    distribution = space[ref_impl]['in-distributions'][0]

        if distribution:
            if distribution in dist:
                # special case-ish hack-ish special case
                if dist[distribution][1] != 'html5-gewgaws':
                    repo_to_node[dist[distribution][1]] = key

    with open(config[space.name]['dist_map'], 'w') as f:
        f.write(json.dumps(repo_to_node, indent=4, sort_keys=True))


def mkdistjson(universe, options, config):
    """Create a JSON of the distribution info."""
    space = universe['node']  # FIXME hardcoded
    dist = {}

    for key, node in space.iteritems():
        if node.get('type') == 'Distribution':
            dist[key] = node

    with open(config[space.name]['dist_json'], 'w') as f:
        f.write(json.dumps(dist, indent=4, sort_keys=True))


# NOTES made while browsing the two versions:
#   online @ links (Wierd, Shelta, etc)
# Things to add MANUALLY:
#   "Apple Befunge" is a variant of Befunge-93
#   SMETANA: link to proof that it is FSA-complete
#   remove Cyclobots
#   authors on Wierd (with John Colagioia, Ben Olmstead)
#   - implementations on Wierd
#   - This sample was written by Milo van Handel
#   RUBE bully automaton link
#   Befunge-97 with Befunge Mailing List Working Group
#   Remove ETHEL
#   ALPACA before REDGREEN
#   mention new acronym for ALPACA
#   Funge-98 Sep 11, 1998 with Befunge Mailing List Working Group 
#   make Befunge-98 Trefunge-98 Unefunge-98 all link near it!
#   MDPN is a meta-language
#   Illberon, Illgola-2, Open Sores Illgol## link near ILLGOL
#   Images for ILLGOL
#   Call out languages that have been lost (Bear Food) and never implemented (Tamerlane)
#   note that ndcnc.bf is broken
#   (pausing around Version...)

def export_lingography(universe, options, config):
    """Export the lingography."""
    space = universe['node']  # FIXME hardcoded

    link_priority_refdex = {}
    for filename in config[space.name].get('link_priority_files', []):
        with open(filename, 'r') as f:
            link_priority_refdex.update(json.loads(f.read()))

    def lingography():
        languages = []
        types = ('Programming Language', 'Programming Language Family',
                 'Conlang', 'Automaton')
        for thing in space:
            node = space[thing]
            if (node['type'] in types and
                'Chris Pressey' in node.get('authors', []) and
                node.get('development-stage', 'idea') not in \
                    ('idea', 'work in progress') and
                not node.get('variant-of', None) and
                (node.get('member-of', None) != 'Funge-98')):
                languages.append(thing)
        return sorted(languages,
                      key=lambda x: (space[x]['inception-date'], space[x]['genre']) )

    data = []
    for key in lingography():
        thing = space[key]
        thing['inception-date'] = str(thing['inception-date'])
        if 'auspices' in thing: del thing['auspices']
        del thing['authors']
        thing['title'] = key
        data.append(thing)

    #print(json.dumps(data, indent=4, sort_keys=True))
    #return

    needed_links = set()

    def linker(match):
        text = match.group(1)
        segments = text.split('|')
        if len(segments) == 1:
            needed_links.add(segments[0])
            return u'[{}][]'.format(segments[0])
        else:
            return u'[{}]({})'.format(segments[1], segments[0])

    f = codecs.open('../Chrysoberyl/article/Lingography.md', 'w', 'utf-8')
    def write(s):
        f.write(s + '\n')

    write("""\
Chris Pressey's Lingography
===========================

(What is a "lingography", you ask? Well, if bands have disc-ographies and directors have film-ographies...)

This is a list, given in approximate chronological order, of the languages I've designed and/or implemented.
It is more-or-less unabridged, but not intended to be completely exhaustive. Most of these language are
programming languages; some of them are formal languages, and some of them are automata of some kind.
Many of them are esolangs. Some of them possibly aren't even languages at all; they just seem to fit the
general theme of the list. Most of them have been implemented, and these implementations are available in
downloadable distrbutions. At the bottom there is also a list of languages that I've implemented, but which
were designed by someone else.

You may also be interested in reading about what it was like to design these and/or the ones that got away.

Languages I've Designed
-----------------------

""")

    for thing in data:
        if thing['title'] in ('Cyclobots', 'ETHEL', 'Okapi', 'Chzrxl',):
            continue
        write(u"### {}".format(thing['title']))
        write("")

        for key in ('type', 'inception-date', 'genre', 'development-stage', 'computational-class'):
            write(u"*   {}: {}".format(key, thing.get(key, '???')))
        for key in ('influences', 'paradigms'):
            if key in thing:
                write(u"*   {}: {}".format(key, ', '.join(thing[key])))

        if 'defining-distribution' not in thing:
            ref_i = space.reference_implementation_of(thing['title'])
            if ref_i and 'in-distributions' in space[ref_i]:
                thing['defining-distribution'] = space[ref_i]['in-distributions'][0]

        if thing['title'] not in ('Full Moon Fever', 'Befunge-97', 'Bear Food', 'Carriage',):
            assert 'defining-distribution' in thing, thing['title']

        if 'defining-distribution' in thing:
            d = thing['defining-distribution']
            write(u"*   reference-distribution: [{}](/distribution/{})".format(d, d))

        if 'sample' in thing:
            write("*   sample program:")
            write("    ")
            for line in thing['sample'].split('\n'):
                write(u"        {}".format(line))

        write("")

        description = thing['description']
        description = re.sub(r'\[\[(.*?)\]\]', linker, description, count=0, flags=re.U)
        write(description)

        commentary = thing.get('commentary')
        if commentary:
            commentary = re.sub(r'\[\[(.*?)\]\]', linker, commentary, count=0, flags=re.U)
            write(commentary)

        def write_impl_properties(node):
            if 'in-distribution' in node:
                d = node['in-distribution']
                write(u"*   in-distribution: [{}](/distribution/{})".format(d, d))
            for key in ('license', 'implementation-type', 'host-language',):
                write(u"*   {}: {}".format(key, node.get(key, '???')))
            for key in ('target-language',):
                if key in node:
                    write(u"*   {}: {}".format(key, node[key]))

        for implementation_key, node in space.related_items('implementation-of', key=thing['title']):
            if node.get('reference', None) is not None:
                write("#### Reference Implementation: {}".format(implementation_key))
                write("")
                write_impl_properties(node)

        for implementation_key, node in space.related_items('implementation-of', key=thing['title']):
            if node.get('reference', None) is not None:
                continue
            write("#### Implementation: {}".format(implementation_key))
            write("")
            write_impl_properties(node)
        write("")

    write("- - - -")
    write("")
    for needed_link in sorted(needed_links):
        if needed_link in link_priority_refdex:
            p = link_priority_refdex[needed_link]
            if 'url' in p:
                url = p['url']
            elif 'filename' in p:
                base = 'http://catseye.tc/'
                url = "{}{}#{}".format(
                    base, p['filename'], p['anchor']
                )
            else:
                raise NotImplementedError
            write(u"[{}]: {}".format(needed_link, url))
        else:
            write(u"[{}]: TBD".format(needed_link))

    f.close()


def render(universe, options, config):
    """Render all nodes to a set of HTML5 files.

    """
    for space in universe.spaces:

        link_priority_refdex = {}
        for filename in config[space.name].get('link_priority_files', []):
            with open(filename, 'r') as f:
                link_priority_refdex.update(json.loads(f.read()))

        space.convert_chrysoberyl_data()
        r = Renderer(universe, space,
            config[space.name]['template_dirs'],
            config[space.name]['output_dir'],
            config[space.name]['checkout_dir'],
            config[space.name]['projection_dir'],
            options.sleek_node_links,
            options.render_nodes,
            link_priority_refdex,
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


def catalogue(universe, options, config):
    """Create a shelf catalogue from distribution nodes.

    """

    space = universe['node']  # FIXME hardcoded
    infos = {}
    for (key, user, repo) in space.github_repos():
        node = space.get(key)
        releases = node.get('releases', [])
        new_style = node.get('tag-style', 'old') == 'new'
        tag = 'master'
        fixed_tag = node.get('fixed-tag', None)
        if fixed_tag == 'OMIT':
            continue
        if fixed_tag is not None:
            tag = fixed_tag
        elif releases:
            version = releases[-1]['version']
            revision = releases[-1]['revision']
            if new_style:
                tag = '%s-%s' % (version, revision)
                if revision == '0.0':
                    tag = version
            else:
                version = re.sub(r'\.', r'_', str(version))
                revision = re.sub(r'\.', r'_', str(revision))
                tag = 'rel_%s_%s' % (version, revision)
                if revision == '0_0':
                    tag = 'rel_%s' % version
        key = repo.lower() if os.getenv('LOWERCASE_REPOS') else repo
        infos[key] = (repo, tag)

    lines = []
    for (key, (repo, tag)) in sorted(infos.iteritems()):
        lines.append('%s@%s' % (key, tag))

    filename = os.path.realpath(os.path.join('.', config['node']['catalogue_file']))
    print "Writing catalogue to '%s'..." % filename

    with codecs.open(filename, 'w', 'utf-8') as f:
        for line in sorted(lines):
            f.write(line)
            f.write('\n')


def project(universe, options, config):
    """Project a copy of all the files in each checkout'ed repository
    into a plain, non-version-controlled directory in
    the projection directory, at (TODO) the latest tag specified in data.

    """
    space_key = 'node'  # FIXME hardcoded
    space = universe[space_key]

    checkout_dir = os.path.abspath(config[space_key]['checkout_dir'])
    projection_dir = os.path.abspath(config[space_key]['projection_dir'])
    try:
        os.makedirs(projection_dir)
    except OSError:
        pass

    cwd = os.getcwd()
    for (key, user, repo) in sorted(space.github_repos()):

        node = space.get(key)
        fixed_tag = node.get('fixed-tag', None)
        if fixed_tag == 'OMIT':
            continue

        repo_path = os.path.join(checkout_dir, repo)
        os.chdir(repo_path)
        distname = get_distname(space[key])
        proj_path = os.path.join(projection_dir, distname)
        command = "rm -rf %s && git archive --format=tar --prefix=%s/ HEAD | (cd %s && tar xf -)" % (
            proj_path, distname, projection_dir
        )
        print command
        os.system(command)

    os.chdir(cwd)


def check_releases(universe, options, config):
    """Check for missing Chrysoberyl releases based on hg tags.

    """

    # TODO: use version of this function from toolshelf release command
    def match_tag(tag):
        match = re.match(r'^rel_(\d+)_(\d+)_(\d\d\d\d)_?(\d\d\d\d)$', tag)
        if match:
            v_maj = match.group(1)
            v_min = match.group(2)
            r_maj = match.group(3)
            r_min = match.group(4)
            v_name = '%s.%s-%s.%s' % (
                v_maj, v_min, r_maj, r_min
            )
            return (v_maj, v_min, r_maj, r_min, v_name)
    
        match = re.match(r'^rel_(\d+)_(\d+)$', tag)
        if not match:
            match = re.match(r'^v?(\d+)\.(\d+)$', tag)
        if match:
            v_maj = match.group(1)
            v_min = match.group(2)
            v_name = '%s.%s' % (v_maj, v_min)
            return (v_maj, v_min, "0", "0", v_name)
    
        match = re.match(r'^v?(\d+)\.(\d+)\-(\d+)\.(\d+)$', tag)
        if match:
            v_maj = match.group(1)
            v_min = match.group(2)
            r_maj = match.group(3)
            r_min = match.group(4)
            v_name = '%s.%s-%s.%s' % (
                v_maj, v_min, r_maj, r_min
            )
            return (v_maj, v_min, r_maj, r_min, v_name)

        return None

    def print_release(version):
        print """\
  - version: "%s"
    revision: "%s"
    url: %s""" % (version['version'], version['revision'], version['url'])

    passes = 0
    space = universe['node']  # FIXME hardcoded
    for (key, user, repo) in sorted(space.github_repos()):
        if key in ('The Dipple', 'Illgol: Grand Mal',):
            continue

        releases = space[key]['releases']

        # record releases which are associated with a tag that does exist,
        # so we can filter them out at the discovery phase
        release_tags = set()
        for r in releases:
            tag = r.get('tag', None)
            if tag:
                release_tags.add(tag)

        versions = []
        tags = []
        source = shelf.make_source_from_spec('github.com/%s/%s' % (user, repo))
        for tag, hg_rev in source.each_tag():
            tags.append((tag, hg_rev))
            if tag in ('tip',) or tag in release_tags:
                continue
            result = match_tag(tag)
            if not result:
                print "Weird tag in %s: '%s'.  Skipping." % (key, tag)
                continue
            (v_maj, v_min, r_maj, r_min, v_name) = result
            distname = get_distname(space[key])
            versions.append((hg_rev, {
                'url': 'http://catseye.tc/distfiles/%s-%s.zip' % (distname, v_name),
                'version': "%s.%s" % (v_maj, v_min),
                'revision': "%s.%s" % (r_maj, r_min),
            }))
        versions = [version[1] for version in sorted(versions)]

        def strip_release(r):
            return {
               'version': str(r['version']), 'revision': str(r['revision'])
            }

        stripped_releases = [strip_release(v) for v in releases]

        missing_releases = []
        for version in versions:
            if strip_release(version) not in stripped_releases:
                missing_releases.append(version)

        if not missing_releases:
            passes += 1
        else:
            print '-' * 40
            print key
            print '-' * 40
            print
            for release in releases:
                print_release(release)
            print
            for (tag, hg_rev) in tags:
                print "%20s %5d" % (tag, hg_rev)
            print
            print "** MISSING: **"
            print
            for release in missing_releases:
                print_release(release)
            print

    print
    print "%s passed" % passes


def check_distfiles(universe, options, config):
    """Check for missing distfiles based on Chrysoberyl releases

    """
    # FIXME hardcoded
    depo = '/media/cpressey/Transcend/mine/catseye.tc/distfiles/'
    space = universe['node']  # FIXME hardcoded


    def v_name_to_rel_name(v_name):
        match = re.match(r'^(\d+)\.(\d+)\-(\d\d\d\d)\.(\d\d\d\d)$', v_name)
        if match:
            return 'rel_%s_%s_%s_%s' % match.groups()
        match = re.match(r'^(\d+)\.(\d+)$', v_name)
        if match:
            return 'rel_%s_%s' % match.groups()
        return v_name

    commands = []
    for (key, user, repo) in space.github_repos():
        for release in space[key]['releases']:
            url = release['url']
            match = re.match(r'^http\:\/\/catseye\.tc\/distfiles\/(.*?)$', url)
            if not match:
                raise ValueError(url)
            filename = os.path.join(depo, match.group(1))
            if not os.path.exists(filename):
                print filename
                distname = get_distname(space[key])
                match = re.match(r'^http\:\/\/catseye\.tc\/distfiles\/' + re.escape(distname) + r'\-(.*?)\.zip$', url)
                if not match:
                    raise ValueError(url)
                v_name = match.group(1)
                if not os.getenv('DECIMAL_VERSIONS'):
                    v_name = v_name_to_rel_name(v_name)
                command = "cd `toolshelf.py pwd %s` && toolshelf.py --output-dir=%s release .@%s" % (distname, depo, v_name)
                commands.append(command)

    print
    for command in commands:
        print command


def count(universe, options, config):
    """Show how many nodes of each type there are

    """
    space = universe['node']
    types = {}
    for (key, node) in space.iteritems():
        if not node.get('hidden', False):
            types.setdefault(node['type'], 0)
            types[node['type']] += 1
    pairs = [(value, key) for (key, value) in types.iteritems()]
    total = 0
    for value, key in sorted(pairs):
        print(key, value)
        total += value
    print('Total', total)


### driver ###

COMMANDS = {
    'render': render,
    'jsonify': jsonify,
    'mkdistmap': mkdistmap,
    'mkdistjson': mkdistjson,
    'catalogue': catalogue,
    'check_releases': check_releases,
    'check_distfiles': check_distfiles,
    'project': project,
    'count': count,
    'export_lingography': export_lingography,
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
    optparser.add_option("--config",
                         dest="config", metavar='FILE', default='config.yaml',
                         help="specify the config file to use "
                              "(default: %default)")
    optparser.add_option("--render-nodes",
                         dest="render_nodes", metavar='NODES', default=None,
                         help="comma-separated list of nodes to render "
                              "(default: render all nodes)")
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

        link_priority_refdex = {}
        for filename in config[key].get('link_priority_files', []):
            with open(filename, 'r') as f:
                link_priority_refdex.update(json.loads(f.read()))

        check_chrysoberyl_data(universe, universe[key], link_priority_refdex)

    for command in args:
        func = COMMANDS.get(command, None)
        if func is None:
            sys.stderr.write("Usage: " + usage() + '\n')
            sys.exit(1)
        print "Executing '%s'..." % command
        # it's expected that func will just raise an exc if it fails
        func(universe, options, config)
