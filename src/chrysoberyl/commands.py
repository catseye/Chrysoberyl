# encoding: UTF-8

"""Parse command line and execute the command(s) given on it.

"""

import codecs
import json
from optparse import OptionParser
import os
import re
import sys


### command functions ###


# NOTE:
#   `mkdistjson` has been run 'permanently' and, going forward, this
#   script will load from that JSON.

#   TODO `mkdistmap` will need to be replaced by a script which, using Feedmark,
#   reads the articles and injects into each distribution a link to the
#   appropriate section of the article.  This need only be done once; the
#   link will be saved in the new distribution JSON.

#   project has been replaced by `shelf_cast`.

#   TODO `check_releases` should be replaced by a script which dumps all
#   tags from all git repos and sees if there are any that do not correspond
#   with any distribution in here.

#   TODO `check_distfiles` should be replaced by a script which looks at
#   all the distfile URLs in here and tries to fetch each of them and reports
#   if any can't be.


def catalogue(distributions):
    """Create a shelf catalogue from distribution nodes.

    """

    infos = {}
    for (key, node) in sorted(distributions.iteritems()):
        repo = node.get('github')
        if not repo:
            #print "# skipping {}".format(key)
            continue
        repo = repo.replace('catseye/', '')
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
    
    for line in sorted(lines):
        sys.stdout.write(line.encode('utf-8'))
        sys.stdout.write('\n')


### driver ###

COMMANDS = {
    'catalogue': catalogue,
}


def usage():
    message = "chrysoberyl {option} {<command>}\n\n"
    message += "where each <command> is one of the following.  All commands\n"
    message += "will be executed in the sequence in which they were given.\n"
    for command in sorted(COMMANDS.keys()):
        message += "\n  %s - " % command
        message += COMMANDS[command].__doc__.rstrip()
    return message


def perform(args):
    optparser = OptionParser(usage().rstrip())
    options, args = optparser.parse_args(args)

    with open('distribution/distributions.json', 'r') as f:
        distributions = json.loads(f.read())

    for command in args:
        COMMANDS[command](distributions)
