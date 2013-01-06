# encoding: UTF-8

"""Data structures used throughout Chrysoberyl.

"""

import re


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


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
