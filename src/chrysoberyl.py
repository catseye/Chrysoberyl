#!/usr/bin/env python
# encoding: UTF-8

"""
A script to process the Chrysoberyl database.

If no options are given, the database will simply be loaded and checked
for consistency.\
"""

import codecs
from optparse import OptionParser
import os
import re
import sys

import jinja2
import markdown
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_chrysoberyl_dir(dirname):
    data = {}

    count = 0
    for root, dirnames, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.endswith('.yaml'):
                count += 1
                file = open(os.path.join(root, filename))
                data.update(yaml.load(file, Loader=Loader))
                file.close()
        del dirnames[:]  # don't automatically descend

    print "%d files read." % count
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
        segments = link.split('|')
        thing = segments[0]
        assert thing in data, \
            "'%s' mentions undefined '%s' in '%s'" % \
            (key, thing, property)


def check_chrysoberyl_data(data):
    count = 0
    for key in data:
      count += 1
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

      assert 'abstract' not in node, "legacy field 'abstract' in '%s'" % key

      description = None
      if 'description' in node:
          description = node['description']
      resolve_internal_links(data, key, 'description', description)

      commentary = None
      if 'commentary' in node:
          commentary = node['commentary']
      resolve_internal_links(data, key, 'commentary', commentary)

      as_a_prerequisite = None
      if 'as-a-prerequisite' in node:
          as_a_prerequisite = node['as-a-prerequisite']
      resolve_internal_links(data, key, 'commentary', as_a_prerequisite)

      if 'auspices' in node:
          assert 'authors' in node, "auspices but no authors in '%s'" % key

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
          check_scalar_ref(data, key, node, 'implementation-of',
                           type_='Programming Language')
          check_scalar_ref(data, key, node, 'implementation-type',
                           type_='Implementation Type')
          if node['implementation-type'] == 'compiler':
              check_scalar_ref(data, key, node, 'target-language',
                               type_='Programming Language')
          assert 'source-language' not in node, \
              "in %s use implementation-of instead" % key
          if 'authors' not in node:
              pl_node = data[node['implementation-of']]
              node['authors'] = pl_node.get('authors', None)
              node['auspices'] = pl_node.get('auspices', None)

      if type_ in ['Game', 'Programming Language', 'Library', 'Tool']:
          if node.setdefault('has-reference-distribution', True):
              if 'reference-distribution' not in node:
                  node['reference-distribution'] = '%s distribution' % key
              check_scalar_ref(data, key, node, 'reference-distribution',
                               type_='Distribution')

      if type_ in ['Game', 'Programming Language']:
          check_scalar_ref(data, key, node, 'genre', type_='Genre')
          assert 'implementations' not in node, \
              "'%s' has 'implementations' but shouldn't" % key
          check_optional_list_ref(data, key, node, 'influences')
          check_list_ref(data, key, node, 'authors')

      if type_ == 'Programming Language':
          check_list_ref(data, key, node, 'paradigms',
                         type_='Programming Paradigm')
          check_optional_scalar_ref(data, key, node, 'computational-class',
                                    type_='Computational Class')
          check_optional_scalar_ref(data, key, node, 'member-of',
                                    type_='Programming Language Family')
          check_optional_scalar_ref(data, key, node, 'development-stage',
                                    type_='Development Stage')
          check_optional_list_ref(data, key, node, 'paradigms',
                                  type_='Programming Paradigm')

      if type_ == 'Programming Language Family':
          check_scalar_ref(data, key, node, 'genre', type_='Genre')
          check_optional_scalar_ref(data, key, node, 'reference-distribution',
                                    type_='Distribution')

      if type_ == 'Ranking':
          check_list_ref(data, key, node, 'entries')
      if type_ == 'Collection':
          check_list_ref(data, key, node, 'include-types', 'type')
          check_list_ref(data, key, node, 'include-authors', 'Individual')

    print "%d nodes checked." % count


def convert_chrysoberyl_data(data):
    count = 0
    for key in data:
        count += 1
        node = data[key]
        new_fields = {}
        for field in node.keys():
            new_fields[field.replace('-', '_')] = node[field]
        node.update(new_fields)
        for field in ('description', 'commentary', 'as_a_prerequisite'):
            node[field + '_html'] = markdown_field(data, node, field)
    print "%d nodes converted." % count


def filekey(key):
    return re.sub(r'(\/|\s|\:|\#)', '_', key) + ".html"


def markdown_field(data, node, field):
    def linker(match):
        text = match.group(1)
        segments = text.split('|')
        thing = segments[0]
        link_text = thing
        if len(segments) > 1:
            link_text = segments[1]
        return '<a href="%s">%s</a>' % (filekey(thing), link_text)
    if field in node:
        html = markdown.markdown(node[field])
        html = re.sub(r'\[\[(.*?)\]\]', linker, html)
        return html
    else:
        return None


class Renderer(object):
    def __init__(self, data, template_dir, output_dir):
        self.data = data
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.loader = jinja2.FileSystemLoader(self.template_dir,
                                              encoding='utf-8')
        self.env = jinja2.Environment(loader=self.loader)

    def render(self, template, output_filename, context):
        with codecs.open(output_filename, 'w', 'utf-8') as html:
            html.write(template.render(context))
    
    def get_template(self, node):
        template_filename = 'default.html'
        filename = filekey(node['type'])
        if os.path.exists(os.path.join(self.template_dir, filename)):
            template_filename = filename
        template = self.env.get_template(template_filename)
        return template

    def render_node(self, key, node):
        context = node.copy()
        context['data'] = self.data
        context['key'] = key

        def implementations():
            i = []
            for thing in data:
                if data[thing].get('implementation-of', None) == key:
                    i.append(thing)
            return i

        # functions
        context['filekey'] = filekey
        context['implementations'] = implementations

        template = self.get_template(node)
        self.render(template, os.path.join(self.output_dir, filekey(key)), context)

    def render_chrysoberyl_data(self):
        count = 0
        for key in data:
            count += 1
            node = data[key]
            self.render_node(key, node)
        print "%d files written." % count


def troll_docs(data, clone_dir):
    for key in data:
        if data[key]['type'] != 'Distribution':
            continue
        distribution_of = data[key]['distribution-of']
        if not data[distribution_of].get('has-reference-distribution', True):
            continue
        if 'reference-distribution' not in data[distribution_of]:
            # ah jeez, it might be a distribution of an implementation, we can't expect this
            print "### %s %s has a distribution %s, but no reference distribution" % (data[distribution_of]['type'], distribution_of, key)
            continue
        if data[distribution_of]['reference-distribution'] != key:
            print "#-- Found non-reference distribution of %s: %s" % (distribution_of, key)
            continue

        if 'github' not in data[key]:
            print "#_? %s not on github" % key
            continue

        print "--> %s -> %s" % (distribution_of, data[key]['github'])


if __name__ == '__main__':
    optparser = OptionParser("[python] chrysoberyl.py {options} datadir\n" + \
                             __doc__)
    optparser.add_option("-l", "--check-links",
                         dest="check_links", action='store_true', default=False,
                         help="check all web links for sanity "
                              "(no 404's, etc.)")
    optparser.add_option("-r", "--render-to",
                         dest="render_to", metavar='DIR',
                         help="render all nodes (as HTML5 files) and "
                              "write into given directory")
    optparser.add_option("-t", "--troll-docs-from",
                         dest="troll_docs_from", metavar='DIR',
                         help="assume that clones of reference distributions "
                              "are available in DIR, and look through each "
                              "reference distribution for anything that looks "
                              "like documentation, and update "
                              "documentation.yaml with those filenames.")
    (options, args) = optparser.parse_args(sys.argv[1:])

    print "Loading Chrysoberyl data..."
    data = load_chrysoberyl_dir(args[0])
    check_chrysoberyl_data(data)

    if options.check_links:
        raise NotImplementedError

    if options.troll_docs_from:
        troll_docs(data, options.troll_docs_from)

    if options.render_to:
        convert_chrysoberyl_data(data)
        r = Renderer(data, 'templates', options.render_to)
        r.render_chrysoberyl_data()
