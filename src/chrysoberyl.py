#!/usr/bin/env python

import os
import sys

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_chrysoberyl_dir(dirname):
    data = {}

    for root, dirnames, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.endswith('.yaml'):
                file = open(os.path.join(root, filename))
                data.update(yaml.load(file, Loader=Loader))
                file.close()
        del dirnames[:]  # don't automatically descend

    return data

def check_chrysoberyl_data(data):
    for key in data:
      assert 'type' in data[key], \
          "'%s' does not specify a type" % key
      type_ = data[key]['type']
      assert type_ in data, \
          "'%s' specifies undefined type '%s'" % (key, type_)
      assert 'type' in data[type_] and data[type_]['type'] == 'type', \
          "'%s' has bad type '%s'" % (key, type_)

if __name__ == '__main__':
    data = load_chrysoberyl_dir(sys.argv[1])
    check_chrysoberyl_data(data)
