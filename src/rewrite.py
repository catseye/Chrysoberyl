#!/usr/bin/env python
# encoding: UTF-8

# This isn't very good, as it doesn't retain order within a YAML file.

import os
import sys

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


if __name__ == '__main__':
    file = open(sys.argv[1])
    data = yaml.load(file, Loader=Loader)
    file.close()

    for key in data:
        if 'type' not in data[key]:
            data[key]['type'] = 'Distribution'

    file = open(sys.argv[1] + ".out", 'w')
    file.write(yaml.dump(data, Dumper=Dumper, default_flow_style=False))
    file.close()
