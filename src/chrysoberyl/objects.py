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

    def get_namespace_of(self, key):
        spaces = []
        for (name, space) in self._spaces.iteritems():
            if key in space:
                spaces.append(space)
        #assert len(spaces) == 1, \
        #    "key '%s' appears in multiple spaces %r" % (key, [s.name for s in spaces])
        if not spaces:
            return None
        return spaces[0]

    def get_node(self, key):
        in_space = None
        for (name, space) in self._spaces.iteritems():
            if key.startswith(space.name + '/'):
                in_space = space
                key = key[len(space.name) + 1:]
                break
        if not in_space:
            for (name, space) in self._spaces.iteritems():
                if key in space:
                    in_space = space
                    break
        assert in_space, "key '%s' not found in any space" % key
        return in_space[key]


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
