# encoding: UTF-8

"""Functions for loading Chrysoberyl data from a set of Yaml files.

"""

import codecs
import os

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

from chrysoberyl.objects import NameSpace


def load_chrysoberyl_dirs(space, dirnames):
    """Given a list of directory names, load Chrysoberyl data from all
    Yaml files in those directories.

    """
    count = 0
    for dirname in dirnames:
        for root, subdirnames, filenames in os.walk(dirname):
            for filename in filenames:
                if filename.endswith('.yaml'):
                    count += 1
                    with open(os.path.join(root, filename)) as file_:
                        space.update(yaml.load(file_, Loader=Loader))
            del subdirnames[:]  # don't automatically descend

    print "%d files read." % count


def load_config(filename):
    with open(filename) as file_:
        config = yaml.load(file_, Loader=Loader)
    return config


def overlay_yaml(filename, data):
    with open(filename) as file_:
        overlay = yaml.load(file_, Loader=Loader)
    for key in overlay:
        assert key in data, "%s: %r not in loaded data" % (filename, key)
        for subkey in overlay[key]:
            assert subkey not in data[key], "%s: '%s.%s' already in loaded data" % (filename, key, subkey)
            data[key][subkey] = overlay[key][subkey]
