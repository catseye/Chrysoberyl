# encoding: UTF-8

import codecs
import os
import re

import jinja2
import markdown


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
        if 'sample' in node:
            node['sample_html'] = markdown.markdown(
                '\n'.join(['    ' + l for l in node['sample'].split('\n')])
            )
            
    print "%d nodes converted." % count


def pathname2url(s):
    s = re.sub('\%', '%25', s)
    s = re.sub(' ', '%20', s)
    s = re.sub('\"', '%22', s)
    s = re.sub('\#', '%23', s)
    s = re.sub('\:', '%3a', s)
    s = re.sub('\?', '%3f', s)
    return s


def filekey(key):
    key = re.sub(r'(\/|\\)', '_', key)
    return key + ".html"


def markdown_field(data, node, field):
    def linker(match):
        text = match.group(1)
        segments = text.split('|')
        thing = segments[0]
        link_text = thing
        if len(segments) > 1:
            link_text = segments[1]
        return '<a href="%s">%s</a>' % (pathname2url(filekey(thing)), link_text)
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
    
    def get_template(self, key):
        node = self.data[key]
        template_filename = 'base.html'
        filename = filekey(key)
        if node['type'] != 'type' and os.path.exists(os.path.join(self.template_dir, filename)):
            template_filename = filename
        else:
            filename = filekey(node['type'])
            if os.path.exists(os.path.join(self.template_dir, filename)):
                template_filename = filename
        template = self.env.get_template(template_filename)
        return template

    def render_node(self, key, node):
        context = node.copy()
        context['data'] = self.data
        context['key'] = key

        def related(relationship, key=key):
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

        def ref_dist(key=key):
            if self.data[key]['type'] == 'Distribution':
                return key
            if 'in-distribution' in self.data[key]:
                return self.data[key]['in-distribution']
            if 'reference-distribution' in self.data[key]:
                return self.data[key]['reference-distribution']
            raise TypeError(key)

        def documentation(key=key):
            doc_node = self.data['Documentation Index']
            return doc_node['entries'].get(key, [])

        def related_github(key=key):
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

        def github_link(filename):
            gh = related_github()
            if gh is None:
                return None
            else:
                return "https://github.com/%s/blob/master/%s" % (gh, filename)

        def indefart(text):
            # "u" is dicey
            if text.startswith(("a", "e", "i", "o", "u")):
                return "an " + text
            else:
                return "a " + text

        def link(key, format="%s"):
            return '<a href="%s">%s</a>' % (pathname2url(filekey(key)), format % key)

        def link_lower(key, format="%s"):
            return '<a href="%s">%s</a>' % (pathname2url(filekey(key)), format % key.lower())

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
                return "%s and %s" % (', '.join([link(f, format=format) for f in front]),
                                      link(last, format=format))

        def breadcrumbs(key=key):
            # ("This function's more like spaghetti than breadcrumbs,"
            # quips Release Notes Girl.  Captain Compiler responds:
            # "Does that mean we're going to make it open-sauce?  HA, HA")
            TOP = "Chrysoberyl"
            if self.data[key]['type'] == 'type':
                bc = ["%ss" % key]
            else:
                bc = [key]
            if key == TOP:
                return bc
            while 'domain' in self.data[key]:
                key = self.data[key]['domain']
                if key == TOP:
                    break
                bc.append(link(key))
            if key != TOP and self.data[key]['type'] != 'type':
                bc.append(link(self.data[key]['type'], format="%ss"))
            bc.append(link(TOP))
            bc.reverse()
            return bc
        
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
            raise KeyError("%s/%s: More than one generally recommended implementation" % (key, implementable))

        def lingography():
            """Bespoke function, because we want to count them in the template"""
            languages = []
            types = ('Programming Language', 'Programming Language Family', 'Conlang')
            for thing in self.data:
                node = self.data[thing]
                if (node['type'] in types and
                    'Chris Pressey' in node.get('authors', []) and
                    node.get('development-stage', 'idea') not in ('idea', 'work in progress') and
                    not node.get('variant-of', None) and
                    not node.get('member-of', None)):
                    languages.append(thing)
            return languages

        # functions
        context['filekey'] = filekey
        context['related'] = related
        context['documentation'] = documentation
        context['related_github'] = related_github
        context['github_link'] = github_link
        context['recommended_implementation'] = recommended_implementation
        context['ref_dist'] = ref_dist
        context['indefart'] = indefart
        context['breadcrumbs'] = breadcrumbs
        context['link'] = link
        context['link_lower'] = link_lower
        context['linked_list'] = linked_list
        context['lingography'] = lingography

        template = self.get_template(key)
        filename = os.path.join(self.output_dir, filekey(key))
        self.render(template, filename, context)

    def render_chrysoberyl_data(self):
        count = 0
        for key in self.data:
            count += 1
            node = self.data[key]
            if node['type'] == 'Metadata':
                continue
            self.render_node(key, node)
        print "%d files written." % count
