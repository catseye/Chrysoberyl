# encoding: UTF-8

"""Data structures used throughout Chrysoberyl.

"""

import re


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


class NameSpace(dict):
    def __init__(self, name):
        self.name = name
        self._has_been_converted = False

    def __setitem__(self, key, value):
        raise NotImplementedError

    def fqkeys(self):
        for key in self.iterkeys():
            if key.startswith(self.name + '/'):
                yield key
            else:
                yield self.name + '/' + key

    def related_items(self, relationship, key, filter=None):
        """Return a list of (key, node) pairs in the current namespace whose
        field named by `relationship` contains the given `key`, whether
        the field is a scalar or a list.  Comparable to a database join.
        The filter, if given, is a predicate which takes a key and a node and returns a boolean.
    
        """
        for nkey, node in self.iteritems():
            if node.get('hidden', False):
                continue
            rel = node.get(relationship, None)
            if rel is None:
                continue
            if filter and not filter(nkey, node):
                continue
            if rel == key:
                yield (nkey, node)
            elif isinstance(rel, list) and key in rel:
                yield (nkey, node)

    def reference_implementation_of(self, key):
        """Find the reference implementation for the given node
        (assumed to be an implementable), and return its key.  If there
        is no reference implementation for the given node, return None.

        Once determined, this value is cached in the node.

        """
        node = self[key]
        if '__reference-implementation__' in node:
            return node['__reference-implementation__']
        ref_i = None
        # sigh, special case this for now
        if node['type'] == 'Picture':
            for (i_key, i_node) in self.related_items('implementation-of', key):
                ref_i = i_key
                break
        else:
            for (ikey, inode) in self.related_items('implementation-of', key):
                if inode.get('reference', False):
                    if ref_i is not None:
                        raise ValueError("more than one reference implementation of %s" % key)
                    ref_i = ikey
        node['__reference-implementation__'] = ref_i
        return ref_i

    def convert_chrysoberyl_data(self):
        """Convert all loaded Chrysoberyl data into a form that can be rendered
        in a Jinja2 template.  This includes rendering fields which are known to
        contain Markdown into corresponding HTML fields, and adding equivalent
        fields whose keys contain underscores (which Jinja2 can understand)
        in place of hyphens (which it can't, but which look better in Yaml.)
    
        """
        if self._has_been_converted:
            return
        count = 0
        for (key, node) in self.iteritems():
            count += 1
            new_fields = {}
            for field in node.keys():
                new_fields[field.replace('-', '_')] = node[field]
            node.update(new_fields)
        self._has_been_converted = True

        print "%d nodes converted." % count


class Universe(object):
    """A Universe (despite its fancy name) is nothing more than a set of NameSpaces."""

    def __init__(self):
        self._spaces = {}

    def create_namespace(self, name):
        assert name not in self._spaces
        self._spaces[name] = NameSpace(name)
        return self._spaces[name]

    def __getitem__(self, name):
        return self._spaces[name]

    def get(self, name, *args):
        return self._spaces.get(name, *args)

    @property
    def spaces(self):
        for (name, space) in self._spaces.iteritems():
            yield space

    def get_space_key_node(self, key, default_space=None):
        if default_space is None:
            default_space = self['node']  # FIXME a bit hardcoded
        in_space = None
        # check if space was explicitly given
        for (name, space) in self._spaces.iteritems():
            if key.startswith(space.name + '/'):
                in_space = space
                key = key[len(space.name) + 1:]
                break
        # make a best guess at the space
        if not in_space:
            possible_spaces = []
            for (name, space) in self._spaces.iteritems():
                if key in space:
                    possible_spaces.append(space)
            if len(possible_spaces) == 1:
                in_space = possible_spaces[0]
            else:
                in_space = default_space
        assert in_space, "key '%s' not found in any space" % key
        return (in_space, key, in_space[key])

    def get_node(self, key, default_space=None):
        return self.get_space_key_node(key, default_space=default_space)[2]


class ApproximateDate(object):
    """Object representing a date which is not fully known.
    Useful for curation purposes.

    """
    def __init__(self, s):
        """Given a string describing an approximate date,
        create an ApproximateDate object.  The string must
        contain at least a year.  It may also contain a
        three-letter month abbreviation before the year.
        It may also contain a day of month, after the month.
        Finally, it may in any case be preceded by the
        letters 'ca', abbreviating 'circa', indicating that
        the actual date is only known to be sometime around
        that time.

        """
        self.text = s
        self.approximate = False
        self.month = None
        self.day = None
        self.year = None
        match = re.match(r'^\s*ca\s*(.*?)$', s)
        if match:
            self.approximate = True
            s = match.group(1)

        match = re.match(r'^(.*?)\s*(\d\d\d\d)\s*$', s)
        if match:
            self.year = int(match.group(2))
            s = match.group(1)

        mo = 0
        for month in MONTHS:
            if s.startswith(month):
                self.month = mo
                s = s[3:]
                break
            mo += 1

        match = re.match(r'^\s*(\d+)', s)
        if match:
            self.day = int(match.group(1))

    def __unicode__(self):
        s = u""
        if self.approximate:
            s = u"ca "
        if self.month is not None:
            s += MONTHS[self.month] + u' '
            if self.day is not None:
                s += u'%s, ' % self.day
        assert self.year is not None
        s += u'%s' % self.year
        return s

    def __str__(self):
        return unicode(self)

    def __repr__(self):
        return "ApproximateDate(%r)" % self.text

    def __cmp__(self, other):
        return self.stamp() - other.stamp()

    def stamp(self):
        """Return an integer value suitable for sorting ApproximateDate
        objects, and for including in JSON.

        """
        return self.year * 10000 + (self.month or 0) * 100 + (self.day or 0)
