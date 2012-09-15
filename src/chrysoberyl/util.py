"""Handy utilities for manipulating files and other operating system objects.

shamelessly stolen from transmat, which is in the public domain

"""

import os
from os import chdir
from subprocess import check_call, Popen, PIPE, CalledProcessError
import time


# Superset of all options expected by all these functions


class DefaultOptions(object):
    def __init__(self):
        self.delay = None
        self.retry = False
        self.quiet = True
        self.ignored_paths = []
        self.ignored_dirs = []
        self.ignored_files = []


DEFAULT_OPTIONS = DefaultOptions()


### Manipulating the File System ###


def do_it(command, options=DEFAULT_OPTIONS):
    if not options.quiet:
        print ">>> " + command
    if options.delay:
        time.sleep(options.delay)
    try:
        check_call(command, shell=True)
    except (OSError, CalledProcessError):
        if options.retry:
            print "TRYING AGAIN!"
            time.sleep(1)
            do_it(command)


def get_it(command, options=DEFAULT_OPTIONS):
    if not options.quiet:
        print ">>> " + command
    if options.delay:
        time.sleep(options.delay)
    output = Popen(command, shell=True, stdout=PIPE).communicate()[0]
    if not options.quiet:
        print output
    return output


def rm_it(*args, **kwargs):
    options = kwargs.get('options', DEFAULT_OPTIONS)
    if not options.quiet:
        print ">>> (deleting %s)" % ', '.join(args)
    for filename in args:
        try:
            os.remove(filename)
        except OSError:
            print "FAILED to remove %s, skipping" % filename


def mv_it(from_, to_, options=DEFAULT_OPTIONS):
    if not options.quiet:
        print ">>> (moving %s to %s)" % (from_, to_)
    try:
        os.rename(from_, to_)
    except OSError:
        if options.retry:
            print "TRYING AGAIN!"
            mv_it(from_, to_)


def change_dir(dir, options=DEFAULT_OPTIONS):
    if not options.quiet:
        print ">>> cd " + dir
    chdir(dir)


### Directory traversal ###


def traverse_dir(dir, process, options=DEFAULT_OPTIONS):
    for root, dirs, files in os.walk(dir):
        if os.path.normpath(root) in options.ignored_paths:
            del dirs[:]  # don't automatically descend
            continue
        if os.path.basename(root) in options.ignored_dirs:
            del dirs[:]
            continue
        for filename in files:
            if filename in options.ignored_files:
                continue
            unicode_filename = filename.decode('utf-8')
            full = os.path.normpath(os.path.join(root, unicode_filename))
            process(full)
