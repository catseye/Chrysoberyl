# encoding: UTF-8

"""Functions for loading Chrysoberyl data from a set of Yaml files.

"""

import os

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_chrysoberyl_dirs(dirnames):
    """Given a list of directory names, load Chrysoberyl data from all
    Yaml files in those directories.

    """
    data = {}

    count = 0
    for dirname in dirnames:
        for root, subdirnames, filenames in os.walk(dirname):
            for filename in filenames:
                if filename.endswith('.yaml'):
                    count += 1
                    file = open(os.path.join(root, filename))
                    data.update(yaml.load(file, Loader=Loader))
                    file.close()
            del subdirnames[:]  # don't automatically descend

    print "%d files read." % count
    return data
