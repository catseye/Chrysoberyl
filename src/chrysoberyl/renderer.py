# encoding: UTF-8

"""Functions and classes for rendering Chrysoberyl data as HTML pages.

"""

import codecs
import os
import re

import jinja2

from chrysoberyl.transformer import filekey, pathname2url


class Renderer(object):
    """Object which renders Chrysoberyl data as HTML pages.

    """
    def __init__(self, data, template_dir, output_dir):
        self.data = data
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.loader = jinja2.FileSystemLoader(self.template_dir,
                                              encoding='utf-8')
        self.env = jinja2.Environment(loader=self.loader)

    def render(self, template, output_filename, context):
        """Low-level method to render a given template."""
        with codecs.open(output_filename, 'w', 'utf-8') as html:
            html.write(template.render(context))

    def get_template(self, key):
        """Helper method to retrieve the appropriate template for the given
        key.

        """
        node = self.data[key]
        template_filename = 'base.html'
        filename = filekey(key)
        # Mercurial can't handle filenames containing ':' on Windows, so:
        filename = re.sub(':', '_', filename)
        if node['type'] != 'type' and \
           os.path.exists(os.path.join(self.template_dir, filename)):
            template_filename = filename
        else:
            filename = filekey(node['type'])
            if os.path.exists(os.path.join(self.template_dir, filename)):
                template_filename = filename
        template = self.env.get_template(template_filename)
        return template

    def render_node(self, key, node):
        """Render the given Chrysoberyl node (with the given key) as an HTML
        document.

        """
        context = node.copy()
        context['data'] = self.data
        context['key'] = key
        context['filekey'] = filekey

        # Context functions.  Being nested functions of render_node lets
        # them easily access (close over) the current node and its key.

        def expose(fun):
            context[fun.__name__] = fun
            return fun

        @expose
        def related(relationship, key=key):
            """Return a list of nodes whose attribute named by `relationship`
            contains the given `key`, whether the attribute is a scalar or a
            list.  Comparable to a database join.

            """
            objects = []
            for thing in self.data:
                rel = self.data[thing].get(relationship, None)
                if rel is None:
                    continue
                if rel == key:
                    objects.append(thing)
                    continue
                if isinstance(rel, list) and key in rel:
                    objects.append(thing)
                    continue
            return objects

        @expose
        def ref_dist(key=key):
            """Find the reference distribution for the given node.

            This could be itself, or the dist an implementation is in,
            or the reference distribution of the implementable.

            """
            if self.data[key]['type'] == 'Distribution':
                return key
            if 'in-distribution' in self.data[key]:
                return self.data[key]['in-distribution']
            if 'reference-distribution' in self.data[key]:
                return self.data[key]['reference-distribution']
            raise TypeError(key)

        @expose
        def non_ref_dist_implementations(key=key):
            """Return a list of all the implementations which are not in
            the reference distribution of the given node.

            """
            implementations_of = related('implementation-of', key=key)
            try:
                reference_distribution = ref_dist(key=key)
            except TypeError:
                return implementations_of
            implementations_in_ref_dist = \
                related('in-distributions', key=reference_distribution)
            implementations = []
            for i in implementations_of:
                if i not in implementations_in_ref_dist:
                    implementations.append(i)
            return implementations

        @expose
        def documentation(key=key):
            """Return the documentation node for the given key."""
            doc_node = self.data['Documentation Index']
            return doc_node['entries'].get(key, [])

        @expose
        def related_github(key=key):
            """Return the name of the Github repository (user/repo)
            associated with the given key.

            """
            if 'github' in self.data[key]:
                return self.data[key]['github']
            d = None
            if 'reference-distribution' in self.data[key]:
                d = self.data[key]['reference-distribution']
            elif 'in-distribution' in self.data[key]:
                d = self.data[key]['in-distribution']
            if d is None:
                return None
            return self.data[d].get('github', None)

        @expose
        def github_link(filename):
            """Return an HTML link to a file in a """
            gh = related_github()
            if gh is None:
                return None
            else:
                return "https://github.com/%s/blob/master/%s" % (gh, filename)

        @expose
        def indefart(text):
            """Try to return a reasonable indefinite article to precede the
            given noun phrase.

            """
            # "u" is dicey
            if text.startswith(("a", "e", "i", "o", "u")):
                return "an " + text
            else:
                return "a " + text

        @expose
        def link(key, format="%s"):
            """Return an HTML link to the node with the given key."""
            return '<a href="%s">%s</a>' % (
                pathname2url(filekey(key)), format % key
            )

        @expose
        def link_lower(key, format="%s"):
            """Return a lowercase HTML link to the node with the given key."""
            return '<a href="%s">%s</a>' % (
                pathname2url(filekey(key)), format % key.lower()
            )

        @expose
        def linked_list(keys, format="%s"):
            # not the kind you're probably thinking of
            if len(keys) == 1:
                return link(keys[0], format=format)
            elif len(keys) == 2:
                return "%s and %s" % (link(keys[0], format=format),
                                      link(keys[1], format=format))
            else:
                front = keys[:-1]
                last = keys[-1]
                return "%s and %s" % (
                    ', '.join([link(f, format=format) for f in front]),
                    link(last, format=format)
                )

        @expose
        def breadcrumbs(key=key):
            # ("This function's more like spaghetti than breadcrumbs,"
            # quips Release Notes Girl.  Captain Compiler responds:
            # "Does that mean we're going to make it open-sauce?  HA, HA")
            TOP = "Chrysoberyl"
            if self.data[key]['type'] == 'type':
                bc = ["%ss" % key]
            else:
                bc = [key]
            if key != TOP:
                while 'domain' in self.data[key]:
                    key = self.data[key]['domain']
                    if key == TOP:
                        break
                    bc.append(link(key))
                if key != TOP and self.data[key]['type'] != 'type':
                    bc.append(link(self.data[key]['type'], format="%ss"))
                bc.append(link(TOP))
            bc.append('<a href="http://catseye.tc/">catseye.tc</a>')
            bc.reverse()
            return bc

        @expose
        def recommended_implementation(implementable, key=key):
            if 'recommended-implementation' in self.data[key]:
                return self.data[key]['recommended-implementation']
            impls = related('implementation-of', key=implementable)
            if len(impls) == 0:
                return None
            if len(impls) == 1:
                return impls[0]
            candidates = []
            for impl in impls:
                if 'generally-recommended' in self.data[impl]:
                    candidates.append(impl)
            if len(candidates) == 1:
                return candidates[0]
            raise KeyError("%s/%s: More than one generally recommended "
                           "implementation" % (key, implementable))

        @expose
        def lingography():
            """Return a list of all entries that will be shown on the
            lingography.  This is a bespoke context function, rather than
            a Jinja2 template using related(), because we want to display
            a count of the items in the template.

            """
            languages = []
            types = ('Programming Language', 'Programming Language Family',
                     'Conlang')
            for thing in self.data:
                node = self.data[thing]
                if (node['type'] in types and
                    'Chris Pressey' in node.get('authors', []) and
                    node.get('development-stage', 'idea') not in \
                        ('idea', 'work in progress') and
                    not node.get('variant-of', None) and
                    not node.get('member-of', None)):
                    languages.append(thing)
            return sorted(languages,
                          key=lambda x: self.data[x]['inception-date'])

        @expose
        def news_items():
            """Bespoke function, because we want to sort them by news-date"""
            items = []
            for thing in self.data:
                node = self.data[thing]
                if node['type'] == 'News Item':
                    items.append(thing)
            return reversed(sorted(items,
                                   key=lambda x: self.data[x]['news-date']))

        template = self.get_template(key)
        filename = os.path.join(self.output_dir, filekey(key))
        self.render(template, filename, context)

    def render_chrysoberyl_data(self):
        """Render all nodes in the loaded Chrysoberyl data as HTML
        documents.

        """
        count = 0
        for key in self.data:
            count += 1
            node = self.data[key]
            if node['type'] in ('Exhibit'):
                continue
            self.render_node(key, node)
        print "%d files written." % count
