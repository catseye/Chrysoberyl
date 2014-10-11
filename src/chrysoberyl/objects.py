# encoding: UTF-8

"""Data structures used throughout Chrysoberyl.

"""

import re


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


class NameSpace(object):
    def __init__(self, name):
        self.name = name
        self._has_been_converted = False
        self._dict = {}

    def update(self, dict_):
        for key in dict_:
            self._dict[key] = dict_[key]

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        raise NotImplementedError
        print "SET: {0}={1}".format(key, value)
        self._dict[key] = value

    def __delitem__(self, key):
        raise NotImplementedError

    def __contains__(self, key):
        return key in self._dict

    def __iter__(self):
        return self._dict.iterkeys()

    def keys(self):
        return self._dict.keys()

    def items(self):
        return self._dict.items()

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
        data = self._dict
        for key in data:
            count += 1
            node = data[key]
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

    @property
    def spaces(self):
        for (name, space) in self._spaces.iteritems():
            yield space

    def get_namespace_of(self, key):
        for (name, space) in self._spaces.iteritems():
            if key in space:
                return space
        return None

    def get_node(self, key):
        for (name, space) in self._spaces.iteritems():
            if key in space:
                return space[key]
        return None


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
