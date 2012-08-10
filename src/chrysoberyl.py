#!/usr/bin/env python
# encoding: UTF-8

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

def check_scalar_ref(data, key, node, property, type_=None):
    value = node[property]
    assert value in data, \
        "'%s' has undefined %s '%s'" % (key, property, value)
    if type_ is None:
        return
    assert data[value]['type'] == type_, \
        "'%s' has %s '%s' which is a %s, not a %s" % (
            key, property, value, data[value]['type'], type_)

def check_optional_scalar_ref(data, key, node, property, type_=None):
    if property in node:
        check_scalar_ref(data, key, node, property, type_=type_)

def check_list_ref(data, key, node, property):
    if property in node:
        for value in node[property]:
            assert value in data, \
                "'%s' has undefined %s '%s'" % \
                (key, property, value)

def check_chrysoberyl_data(data):
    for key in data:
      node = data[key]
      assert 'type' in node, \
          "'%s' does not specify a type" % key
      type_ = node['type']
      assert type_ in data, \
          "'%s' specifies undefined type '%s'" % (key, type_)
      assert 'type' in data[type_] and data[type_]['type'] == 'type', \
          "'%s' has bad type '%s'" % (key, type_)

      if type_ == 'Distribution':
          #assert 'distribution-of' in node, \
          #   "Distribution '%s' does not say what it is of" % key
          if 'distribution-of' in node:
              assert node['distribution-of'] in data, \
                  "Distribution '%s' is of non-existant '%s'" % \
                  (key, node['distribution-of'])

      check_list_ref(data, key, node, 'implementations')

      check_optional_scalar_ref(data, key, node, 'license', type_='License')

      check_optional_scalar_ref(data, key, node, 'genre', type_='Genre')

if __name__ == '__main__':
    data = load_chrysoberyl_dir(sys.argv[1])
    check_chrysoberyl_data(data)
