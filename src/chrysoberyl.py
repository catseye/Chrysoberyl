#!/usr/bin/env python
# encoding: UTF-8

import os
import re
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
    assert property in node, \
        "'%s' does not specify a %s" % (key, property)
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


def check_list_ref(data, key, node, property, type_=None):
    assert property in node, \
        "'%s' has no %s list" % (key, property)
    assert isinstance(node[property], list), \
        "'%s' has non-list %s" % (key, property)
    for value in node[property]:
        assert value in data, \
            "'%s' has undefined %s '%s'" % \
            (key, property, value)
        if type_ is not None:
            assert data[value]['type'] == type_, \
                "'%s' has %s '%s' which is a %s, not a %s" % (
                    key, property, value, data[value]['type'], type_)
          

def check_optional_list_ref(data, key, node, property, type_=None):
    if property in node:
        check_list_ref(data, key, node, property, type_)


def resolve_internal_links(data, key, property, text):
    if text is None:
        return True
    for match in re.finditer(r'\[\[(.*?)\]\]', text):
        link = match.group(1)
        assert link in data, \
            "'%s' mentions undefined '%s' in '%s'" % \
            (key, link, property)


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

      check_optional_list_ref(data, key, node, 'see-also')
      check_optional_list_ref(data, key, node, 'authors')
      check_optional_list_ref(data, key, node, 'auspices', type_='Organization')

      if 'abstract' in node and 'description' in node:
          assert False, "'%s' defines both 'abtsract' and 'description'" % key

      description = None
      if 'abstract' in node:
          description = node['abstract']
      if 'description' in node:
          description = node['description']
      resolve_internal_links(data, key, 'description', description)

      commentary = None
      if 'commentary' in node:
          commentary = node['commentary']
      resolve_internal_links(data, key, 'commentary', commentary)

      if type_ == 'Distribution':
          # (this has multiple possible types)
          check_scalar_ref(data, key, node, 'distribution-of')
          check_optional_scalar_ref(data, key, node, 'development-stage',
                                    type_='Development Stage')

      if type_.endswith(' Implementation'):
          check_scalar_ref(data, key, node, 'license', type_='License')
          check_optional_scalar_ref(data, key, node, 'in-distribution',
                                    type_='Distribution')
          check_optional_scalar_ref(data, key, node, 'development-stage',
                                    type_='Development Stage')
          check_scalar_ref(data, key, node, 'host-language',
                           type_='Programming Language')
          check_optional_list_ref(data, key, node, 'build-requirements')
          check_optional_list_ref(data, key, node, 'required-libraries')
          check_optional_list_ref(data, key, node, 'run-requirements')

      if type_ == 'Language Implementation':
          check_scalar_ref(data, key, node, 'implementation-type',
                           type_='Implementation Type')
          if node['implementation-type'] == 'compiler':
              check_scalar_ref(data, key, node, 'source-language',
                               type_='Programming Language')
              check_scalar_ref(data, key, node, 'target-language',
                               type_='Programming Language')

      if type_ in ['Game', 'Programming Language']:
          check_scalar_ref(data, key, node, 'genre', type_='Genre')
          check_optional_scalar_ref(data, key, node, 'reference-distribution',
                                    type_='Distribution')
          check_list_ref(data, key, node, 'implementations')
          check_optional_list_ref(data, key, node, 'influences')
          check_list_ref(data, key, node, 'authors')

      if type_ == 'Programming Language':
          check_optional_scalar_ref(data, key, node, 'computational-class',
                                    type_='Computational Class')
          check_optional_scalar_ref(data, key, node, 'member-of',
                                    type_='Programming Language Family')
          check_optional_scalar_ref(data, key, node, 'development-stage',
                                    type_='Development Stage')
          check_optional_list_ref(data, key, node, 'paradigms',
                                  type_='Programming Paradigm')
          if node.get('has-reference-distribution', True):
              check_scalar_ref(data, key, node, 'reference-distribution',
                               type_='Distribution')

      if type_ == 'Programming Language Family':
          check_scalar_ref(data, key, node, 'genre', type_='Genre')
          check_optional_scalar_ref(data, key, node, 'reference-distribution',
                                    type_='Distribution')

if __name__ == '__main__':
    data = load_chrysoberyl_dir(sys.argv[1])
    check_chrysoberyl_data(data)
