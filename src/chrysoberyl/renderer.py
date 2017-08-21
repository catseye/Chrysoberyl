# encoding: UTF-8

"""Functions and classes for rendering Chrysoberyl data as HTML pages.

"""

import codecs
import os
import re

from jinja2 import BaseLoader, Environment
from jinja2.exceptions import TemplateNotFound
import markdown

from chrysoberyl import transformer
from chrysoberyl.objects import get_distname
from chrysoberyl.transformer import (
    filekey, sleek_key, pathname2url, markdown_contents
)


# lifted from toolshelf (and probably to be removed from there)
def find_likely_documents(start_dir):
    DOC_PATTERNS = (
        r'^LICENSE$',
        r'^UNLICENSE$',
        r'^README',
        r'^.*?\.markdown$',
        r'^.*?\.md$',
        r'^.*?\.txt$',
        r'^.*?\.lhs$',
    )
    for root, dirnames, filenames in os.walk(start_dir):
        if root.endswith((".hg", ".git", "bin", "fixture", "distrepos")):
            del dirnames[:]
            continue
        for filename in filenames:
            for pattern in DOC_PATTERNS:
                if re.match(pattern, filename):
                    full_filename = os.path.join(
                        os.path.relpath(root, start_dir), filename
                    )
                    if full_filename[0:2] == './':
                        full_filename = full_filename[2:]
                    yield full_filename
                    break


class Loader(BaseLoader):
    def __init__(self, template_dirs):
        self.template_dirs = template_dirs

    def get_source(self, environment, filename):
        found_path = None
        for template_dir in self.template_dirs:
            path = os.path.join(template_dir, filename)
            if os.path.exists(path):
                found_path = path
                break
        if found_path is None:
            raise TemplateNotFound(filename)
        with open(found_path, 'r') as f:
            source = f.read().decode('utf-8')
        return source, found_path, lambda: True


CACHE = {}   # of related items


class Renderer(object):
    """Object which renders Chrysoberyl data as HTML pages.

    """
    def __init__(self, universe, space, template_dirs, output_dir, checkout_dir,
                 projection_dir, sleek_node_links, render_nodes, link_priority):
        self.universe = universe
        self.space = space
        self.template_dirs = template_dirs
        assert isinstance(template_dirs, list)
        self.output_dir = output_dir
        self.checkout_dir = checkout_dir
        self.projection_dir = projection_dir
        self.sleek_node_links = sleek_node_links
        self.render_nodes = render_nodes
        self.jinja2_env = Environment(loader=Loader(self.template_dirs))
        self.link_priority = link_priority

    def render(self, template, output_filename, context):
        """Low-level method to render a given template."""
        with codecs.open(output_filename, 'w', 'utf-8') as html:
            html.write(template.render(context))

    def get_template(self, key):
        """Helper method to retrieve the appropriate template for the given
        key.

        If the node is a type, look first for a template called
        type_[key].html, in ALL the template directories.  If found, load it
        as the template.  If not found, load type.html as the template.

        Look for a template named [key].html in ALL the template directories.
        If found, use it as the template.

        If no template yet, look for a template named [type].html in ALL the
        template directories.  If found, use it as the template.

        If no template yet, use _node.html as the template.

        Note that this logic is not in the template loader, because it resolves
        keys to filenames, and is not applicable during {% extends foo %}.

        """
        node = self.space[key]
        # Mercurial can't handle filenames containing ':' on Windows, so:
        key_filename = re.sub(':', '_', filekey(key))

        def find_template(filename):
            for template_dir in self.template_dirs:
                full_filename = os.path.join(template_dir, filename)
                if os.path.exists(full_filename):
                    return full_filename
            return None

        if node['type'] == 'type':
            type_filename = 'type_' + key_filename
            if find_template(type_filename):
                return self.jinja2_env.get_template(type_filename)
            else:
                return self.jinja2_env.get_template('type.html')

        if find_template(key_filename):
            return self.jinja2_env.get_template(key_filename)

        type_filename = filekey(node['type'])
        if find_template(type_filename):
            return self.jinja2_env.get_template(type_filename)

        return self.jinja2_env.get_template('_node.html')

    def render_node(self, key, node):
        """Render the given Chrysoberyl node (with the given key) as an HTML
        document.

        """
        context = node.copy()
        context['key'] = key
        context['sleek_key'] = sleek_key
        context['pathname2url'] = pathname2url

        # Context functions.  Being nested functions of render_node lets
        # them easily access (close over) the current node and its key.

        def expose(fun):
            context[fun.__name__] = fun
            return fun

        @expose
        def basename(path):
            return os.path.basename(path)

        @expose
        def get_node(key=key, space=self.space):
            return self.universe.get_node(key, default_space=space)

        @expose
        def get_space(name=None):
            if name is None:
                return self.space
            return self.universe[name]

        @expose
        def md2html(field_contents, prefix='../', fixed=False):
            if fixed:
                md = '\n'.join(
                    ['    ' + l for l in field_contents.split('\n')]
                )
                return markdown.markdown(md)
            else:
                return markdown_contents(
                    self.universe, field_contents, prefix=prefix,
                    sleek=self.sleek_node_links,
                    link_priority=self.link_priority,
                )

        @expose
        def markdown_file_to_html(filename):
            # FIXME makes awful assumptions
            prefix = 'http://catseye.tc/modules/'
            parts = filename.split(prefix)
            if len(parts) == 2:
                filename = os.path.join(self.projection_dir, parts[1])
            with codecs.open(filename, 'r', 'utf-8') as f:
                md = f.read()
            return markdown.markdown(md)

        @expose
        def html_file_to_html(filename):
            # FIXME makes awful assumptions
            prefix = 'http://catseye.tc/modules/'
            parts = filename.split(prefix)
            if len(parts) == 2:
                filename = os.path.join(self.projection_dir, parts[1])
            with codecs.open(filename, 'r', 'utf-8') as f:
                collect = False
                html = []
                for line in f:
                    if line.strip() == '<body>':
                        collect = True
                    elif line.strip() == '</body>':
                        collect = False
                    elif collect:
                        html.append(line)
            return ''.join(html)

        @expose
        def empty(iterable):
            for x in iterable:
                return False
            return True

        @expose
        def count(iterable):
            return len(list(iterable))

        @expose
        def filter_items(predicate):
            """Return a list of (key, node) pairs in the current namespace
            for which the given predicate returns True.

            """
            for nkey, node in self.space.iteritems():
                if predicate(node):
                    yield (nkey, node)

        @expose
        def implementations_by_p(type_, auspice):
            """A predicate for returning the implementations conducted
            under the given auspice.

            """
            def f(node):
                if node.get('hidden', False):
                    return False
                if 'implementation-of' not in node:
                    return False
                cnode = get_node(node['implementation-of'][0])
                if cnode['type'] != type_:
                    return False
                if 'auspices' in cnode and auspice in cnode['auspices']:
                    return False
                if 'auspices' not in node:
                    return False
                if auspice not in node['auspices']:
                    return False
                return True
            return f

        # incomplete and circumstantial.  used on front page only
        @expose
        def ours_p():
            auspices = ("Cat's Eye Technologies", "What is this I don't even",)
            def f(key, node):
                if node.get('hidden', False):
                    return False
                if not is_current(node):
                    return False
                if 'auspices' not in node:
                    return False
                ok = False
                for auspice in auspices:
                    if auspice in node['auspices']:
                        ok = True
                        break
                if not ok:
                    return False
                return True
            return f

        # wow, quite the hack
        @expose
        def include_snippet(filename):
            with open(filename, 'r') as f:
                return f.read()

        @expose
        def has_online_implementation_p():
            def f(key, node):
                return bool(online_implementations(key))
            return f

        @expose
        def related_items(relationship, key=key, filter=None):
            if filter is None:
                cache_key = relationship + ':' + key
                if cache_key not in CACHE:
                    CACHE[cache_key] = list(  self.space.related_items(relationship, key, filter=None)  )
                return CACHE[cache_key]
            else:
                return self.space.related_items(relationship, key, filter=filter)

        # maybe will be deprecated: use related_items instead
        @expose
        def related(*args, **kwargs):
            for (k, n) in related_items(*args, **kwargs):
                yield k

        @expose
        def group_by(iterable, group_by):
            groups = {}
            for (nkey, node) in iterable:
                if node.get('hidden', False):
                    continue
                memberships = node.get(group_by)
                if not isinstance(memberships, list):
                    memberships = [memberships]
                for membership in memberships:
                    groups.setdefault(membership, []).append(nkey)
            return groups

        @expose
        def iteritems_sorted_within(assoc, sorts):
            for key in sorts:
                if key == 'None':
                    key = None
                if key in assoc:
                    yield (key, assoc[key])
            for (key, stuff) in sorted(assoc.iteritems()):
                if key is not None and key not in sorts:
                    #print "Note: '%s' not in sort keys" % key
                    yield (key, stuff)

        @expose
        def keys_sorted_within(keys, sorts):
            for key in sorts:
                if key == 'None':
                    key = None
                if key in keys:
                    yield key
            for key in sorted(keys):
                if key is not None and key not in sorts:
                    #print "Note: '%s' not in sort keys" % key
                    yield key

        @expose
        def is_current(node):
            if 'development-stage' not in node:
                return True
            return node['development-stage'] not in (
                'idea', 'work in progress', 'abandoned', 'unfinished',
                'archived', 'lost',
            )

        @expose
        def collect_auspices(items):
            """Group nodes with the given type by auspices.  Only include nodes
            which are current, and for the "None" auspices, nodes which have not
            been implemented by 'us'."""
            us = [
                "Cat's Eye Technologies",
                "What is this I don't even",
            ]
            collected_auspices = {}
            for auspices, v in group_by(items, 'auspices').iteritems():
                v = [k for k in v if is_current(get_node(k))]
                if auspices == None:
                    v = [k for k in v if not has_implementation_by_one_of(k, us)]
                if v:
                    collected_auspices[auspices] = v
            return collected_auspices

        @expose
        def has_implementation_by_one_of(key, auspices):
            for (ikey, node) in related_items('implementation-of', key=key):
                iauspices = node.get('auspices', [])
                for auspice in auspices:
                    if auspice in iauspices:
                        return True
            return False

        @expose
        def impls_for_platform(plat_key, key=key):
            for (ikey, node) in related_items('implementation-of', key=key):
                if (node.get('platform', None) == plat_key or
                    node.get('host_platform', None) == plat_key or
                    node.get('target_platform', None) == plat_key):
                    yield ikey

        @expose
        def ref_impl(key=key):
            return self.space.reference_implementation_of(key)

        @expose
        def ref_dist(key=key):
            """Find the reference distribution for the given node, which is
            assumed to be an implementable.

            If a `defining-distribution` is given, then that is
            the reference distribution.

            Otherwise, if there is a reference implementation, and the
            reference implementation is in more than zero distributions,
            the first such distribution is the reference distribution.

            Otherwise None.

            """
            node = self.universe.get_node(key)
            if 'defining-distribution' in node:
                return node['defining-distribution']

            ref_i = ref_impl(key=key)
            if ref_i is not None:
                if 'in-distributions' in self.universe.get_node(ref_i):
                    return self.universe.get_node(ref_i)['in-distributions'][0]

            return None

        @expose
        def documentation(key=key):
            """Return a list of documentation file names for the given key."""
            filenames = []
            node = self.universe.get_node(key)
            if 'github' in node:
                path = os.path.join(
                    self.projection_dir, get_distname(node),
                )
                for filename in find_likely_documents(path):
                    filenames.append(filename)

            return sorted(filenames)

        @expose
        def documentation_link(filename, key=key):
            node = self.universe.get_node(key)
            # This is a URL. TODO don't make so many assumptions in URLs.
            path = os.path.join(
                '..', 'view',
                get_distname(node),
                pathname2url(filename)
            )
            # TODO: stat the file, fallback to Github link if not there
            return path

        @expose
        def github_link(filename, key=key):
            """Return an HTML link to a file in the Github repository
            associated with the given key, which is assumed to be a
            distribution.

            """
            # apparently not used anymore!
            raise NotImplementedError
            return "https://github.com/%s/blob/master/%s" % (
                pathname2url(self.universe.get_node(key)['github']),
                pathname2url(filename)
            )

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
        def plural(text):
            """Try to return a reasonable pluralized version of the
            given noun phrase.

            """
            if text[-4:] == 'dium':
                return text[:-4] + 'dia'
            if text[-5:] == 'maton':
                return text[:-5] + 'mata'
            if text[-1:] == 's':
                return text + 'es'
            if text[-1:] == 'y':
                return text[:-1] + 'ies'
            return text + 's'

        _indefart = indefart
        _plural = plural

        @expose
        def link(key, format="%s", indefart=False, lower=False, plural=False,
                 link_text=None, title=None, extra_attr=''):
            """Return an HTML link to the node with the given key.

            indefart causes the link text to be preceded by an indefinite
            article.  lower causes the link text to be lowercase.
            plural causes the link text to be pluralized.

            If the node is of a type that suppresses page generation, this
            will raise an exception.  In the future, it may intelligently
            divert to a different node.

            """
            if key in self.link_priority:
                return u'<a href="{}">{}</a>'.format(self.link_priority[key], key)
            if link_text is None:
                (_, ukey, _) = self.universe.get_space_key_node(key)
                link_text = ukey
                if lower:
                    link_text = link_text.lower()
                if indefart:
                    link_text = _indefart(key)
                if plural:
                    link_text = _plural(link_text)
                link_text = format % link_text
            return transformer.link(
                self.universe, key, link_text, title=title,
                extra_attr=extra_attr, sleek=self.sleek_node_links
            )

        # not the kind you're probably thinking of
        @expose
        def linked_list(keys, format="%s"):
            """Given a list of keys, return a fragment of HTML containing
            links to nodes with those keys.  The list is formatted in a human-
            readable fashion, with commas, and the word "and" before the
            end.

            """
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

        def online_locations(key):
            l = self.space[key].get('online-locations', [])
            if l:
                return l
            if key.endswith(' (mp3)'):
                return ['installation/' + key[:-6]]
            if key.endswith(' (PNG)'):
                return ['installation/' + key[:-6]]
            if key.endswith(' (GIF)'):
                return ['installation/' + key[:-6]]
            if key.endswith(' (JPEG)'):
                return ['installation/' + key[:-7]]
            return []

        def online_implementations(key):
            online_locs = []
            online_locs.extend(online_locations(key))
            for impl in sorted(related('implementation-of', key=key)):
                online_locs.extend(online_locations(impl))
            return online_locs

        @expose
        def online_buttons(key=key, show_verb_phrase=True):
            links = []
            for loc_key in sorted(online_implementations(key)):
                mediums = self.universe.get_node(loc_key)['mediums']
                medium = 'Online'
                if 'Java applet' in mediums:
                    medium = '(Java applet)'
                if 'Java Web Start' in mediums:
                    medium = '(Java Web Start)'
                assert 'HTML5' in mediums, 'No good medium in ' + \
                                           ' on '.join(mediums)
                if show_verb_phrase:
                    node = self.universe.get_node(key)
                    if node['type'] == 'Game':
                        link_text = 'Play'
                    elif node['type'] == 'Musical Composition':
                        link_text = 'Listen'
                    elif node['type'] in ('Text', 'Book'):
                        link_text = 'Read it'
                    elif node['type'] in ('Picture',):
                        link_text = 'See it'
                    else:
                        link_text = 'Try it'
                    link_text += ' ' + medium
                else:
                    link_text = medium
                links.append(
                    link(
                        loc_key, link_text=link_text,
                        extra_attr='class="button" '
                    )
                )
            non_applet_links = [l for l in links if '(Java applet)' not in l]
            if non_applet_links:
                links = non_applet_links
            return ' '.join(links)

        @expose
        def strip_outer_p(text):
            match = re.match(
                r'^\s*\<p\>\s*(.*?)\s*\<\/p\>\s*$', text,
                re.DOTALL
            )
            if match:
                return match.group(1)
            return text

        @expose
        def debug(text):
            print
            print text
            print
            return ''

        @expose
        def error(text):
            raise ValueError("'%s'" % text)

        @expose
        def _assert(cond):
            assert cond
            return ''

        @expose
        def breadcrumbs(key=key):
            """Generate breadcrumbs for the node given by key."""
            # ("This function's more like spaghetti than breadcrumbs,"
            # quips Release Notes Girl.  Captain Compiler responds:
            # "Does that mean we're going to make it open-sauce?  HA, HA")
            TOP = "Chrysoberyl"
            bc = []
            if key != TOP:
                while 'domain' in self.universe.get_node(key):
                    key = self.universe.get_node(key)['domain']
                    if key == TOP:
                        break
                    bc.append(link(key))
                if key != TOP and self.universe.get_node(key)['type'] != 'type':
                    bc.append(link(self.universe.get_node(key)['type'], plural=True))
                bc.append(link(TOP))
            bc.append('<a href="../">catseye.tc</a>')
            bc.reverse()
            return bc

        @expose
        def recommended_implementation(implementable, key=key):
            """Return a node representing the recommended implementation of
            the given key (assumed to be an implementable.)

            """
            node = self.universe.get_node(key)
            if 'recommended-implementation' in node:
                return node['recommended-implementation']
            if empty(related('implementation-of', key=implementable)):
                return None
            impls = [i for i in related('implementation-of', key=implementable)]
            if len(impls) == 1:
                return impls[0]
            candidates = []
            # XXX can we statically check this?
            for impl in impls:
                if 'generally-recommended' in self.universe.get_node(impl):
                    candidates.append(impl)
            if len(candidates) == 1:
                return candidates[0]
            raise KeyError("Implementable %s has more than one generally "
                           "recommended implementation (under key %s)" %
                           (implementable, key))

        @expose
        def lingography():
            """Return a list of all entries that will be shown on the
            lingography.  This is a bespoke context function, rather than
            a Jinja2 template using related(), because we want to display
            a count of the items in the template.

            """
            languages = []
            types = ('Programming Language', 'Programming Language Family',
                     'Conlang', 'Automaton')
            for thing in self.space:
                node = self.space[thing]
                if (node['type'] in types and
                    'Chris Pressey' in node.get('authors', []) and
                    node.get('development-stage', 'idea') not in \
                        ('idea', 'work in progress') and
                    not node.get('variant-of', None) and
                    (node.get('member-of', None) != 'Funge-98')):
                    languages.append(thing)
            return sorted(languages,
                          key=lambda x: self.space[x]['inception-date'])

        @expose
        def articles():
            """Return a list of all article entries to be shown on the articles
            node.  This is a bespoke context function because we want the
            nodes to be sorted by publication date (and this is an easy way
            to do that.  There might be others.)

            """
            items = []
            for thing in self.space:
                node = self.space[thing]
                if node['type'] == 'Article':
                    items.append(thing)
            return reversed(sorted(
                items,
                key=lambda x: self.space[x]['publication-date']
            ))

        @expose
        def latest_news_item():
            return list(articles())[0]

        @expose
        def strftime(date, fmt):
            return date.strftime(fmt)

        template = self.get_template(key)
        basename = filekey(key)
        filename = os.path.join(self.output_dir, basename)
        self.render(template, filename, context)
        # sideways compatibility
        if '_' in basename:
            basename = basename.replace('_', ' ')
            filename = os.path.join(self.output_dir, basename)
            self.render(template, filename, context)

    def render_chrysoberyl_data(self):
        """Render all nodes in the loaded Chrysoberyl data as HTML
        documents.

        """
        render_nodes = self.render_nodes.split(',') if self.render_nodes else []
        render_nodes = [r.replace('_', ' ') for r in render_nodes]
        count = 0
        for (key, node) in self.space.iteritems():
            type_ = node['type']
            if self.universe.get_node(type_).get('suppress-page-generation', False):
                continue
            if render_nodes and key not in render_nodes:
                continue
            self.render_node(key, node)
            count += 1
        print "%d files written." % count
