# encoding: UTF-8

import re


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

class ApproximateDate(object):
    def __init__(self, s):
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
        return self.year * 10000 + (self.month or 0) * 100 + (self.day or 0)


def warn(message):
    print "*** warning: %s" % message


def check_scalar_ref(data, key, node, property, types=None):
    assert property in node, \
        "'%s' does not specify a %s" % (key, property)
    value = node[property]
    assert value in data, \
        "'%s' has undefined %s '%s'" % (key, property, value)
    if types is None:
        return
    assert data[value]['type'] in types, \
        "'%s' has %s '%s' which is a %s, not a %s" % (
            key, property, value, data[value]['type'], types)


def check_optional_scalar_ref(data, key, node, property, types=None):
    if property in node:
        check_scalar_ref(data, key, node, property, types=types)


def check_list_ref(data, key, node, property, types=None):
    assert property in node, \
        u"'%s' has no %s list" % (key, property)
    assert isinstance(node[property], list), \
        u"'%s' has non-list %s" % (key, property)
    for value in node[property]:
        assert value in data, \
            u"'%s' has undefined %s '%s'" % \
            (key, property, value)
        if types is not None:
            assert data[value]['type'] in types, \
                u"'%s' has %s '%s' which is a %s, not a %s" % (
                    key, property, value, data[value]['type'], types)
          

def check_optional_list_ref(data, key, node, property, types=None):
    if property in node:
        check_list_ref(data, key, node, property, types=types)


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


LEGACY_FIELDS = (
    'abstract',
    'author',
    'implementations',
    'has-reference-distribution',
    'required-libraries',
    'includes-executables',
    'prebuilt-in-distribution',
)


def check_chrysoberyl_data(data):
    count = 0
    for key in data:
      count += 1
      node = data[key]
      
      # Every node must have a valid type.
      assert 'type' in node, \
          "'%s' does not specify a type" % key
      type_ = node['type']
      assert type_ in data, \
          "'%s' specifies undefined type '%s'" % (key, type_)
      assert 'type' in data[type_] and data[type_]['type'] == 'type', \
          "'%s' has bad type '%s'" % (key, type_)

      # Every node may have some of these.
      try:
          if 'inception-date' in node:
              assert node['inception-date'] != 'Unknown'
              node['inception-date'] = ApproximateDate(str(node['inception-date']))
      except Exception:
          print "'%s' has bad date '%s'" % (key, node['inception-date'])
          raise
      check_optional_scalar_ref(data, key, node, 'domain')
      check_optional_list_ref(data, key, node, 'see-also')
      check_optional_scalar_ref(data, key, node, 'genre')
      check_optional_list_ref(data, key, node, 'authors',
          types=['Individual', 'Organization'])
      check_optional_list_ref(data, key, node, 'auspices',
          types=['Organization'])
      check_optional_list_ref(data, key, node, 'influences')
      # These two fields go together.
      if 'auspices' in node:
          assert 'authors' in node, "auspices but no authors in '%s'" % key
      if 'submitted-to' in node:
          for sub in node['submitted-to']:
              check_scalar_ref(data, key, sub, 'competition', types=['Competition'])

      # Every node may have these, and they may have internal links.
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

      # No nodes may have legacy fields.
      for legacy_field in LEGACY_FIELDS:
          assert legacy_field not in node, \
              "legacy field '%s' found in '%s'" % (legacy_field, key)

      check_optional_scalar_ref(data, key, node, 'development-stage',
                                types=['Development Stage'])

      # On to checking fields specific to different types.

      if type_ == 'News Item':
          check_optional_scalar_ref(data, key, node, 'news-node')

      if type_ == 'Distribution':
          assert 'development-stage' not in node, \
            "%s mentions 'development-stage'" % key
          if 'distribution-of' not in node:
              match = re.match(r'^(.*?) distribution$', key)
              if match:
                  distribution_of = [match.group(1)]
                  r = []
                  for d in distribution_of:
                      if data[d]['type'] == 'Implementation':
                          r.extend(data[d]['implementation-of'])
                  if r:
                      distribution_of = r
                  node['distribution-of'] = distribution_of
          check_list_ref(data, key, node, 'distribution-of',
                         types=('Programming Language', 'Programming Language Family',
                                'Game', 'Tool', 'Library', 'Electronics Project',
                                'Demo', 'Conlang', 'Platform', 'Database'))
          check_optional_list_ref(data, key, node, 'test-requirements',
                                  types=('Programming Language', 'Tool'))

      if type_ == 'Implementation':
          check_list_ref(data, key, node, 'implementation-of')
          check_optional_scalar_ref(data, key, node, 'recommended-implementation',
                                    types=['Implementation'])

          # for convenience, bring in the type of the thing being implemented
          # the first thing.  we assume they're all the same type.  but...
          # hey, let's build something that implements both Underload and
          # Zoning Variance #5!
          impl_of_type = data[node['implementation-of'][0]]['type']

          check_scalar_ref(data, key, node, 'license', types=['License'])
          if 'in-distribution' in node:
              assert 'in-distributions' not in node
              node['in-distributions'] = [node['in-distribution']]
              del node['in-distribution']
          check_optional_list_ref(data, key, node, 'in-distributions',
                                    types=['Distribution'])
          check_optional_list_ref(data, key, node, 'prebuilt-for-platforms',
                                    types=['Platform', 'Programming Language'])
          if impl_of_type == 'Musical Composition':
              check_scalar_ref(data, key, node, 'host-language',
                               types=['Musical Notation'])
          else:
              check_scalar_ref(data, key, node, 'host-language',
                               types=['Programming Language'])
          check_optional_scalar_ref(data, key, node, 'host-platform',
                           types=['Platform'])
          # these shouldn't really be needed.  derive, derive!
          # I really don't like that 'Programming Language' is in these
          check_optional_list_ref(data, key, node, 'build-requirements',
                           types=['Library', 'Tool', 'Programming Language'])
          check_optional_list_ref(data, key, node, 'run-requirements',
                           types=['Library', 'Tool', 'Programming Language'])

          if impl_of_type == 'Platform':
              check_scalar_ref(data, key, node, 'implementation-type',
                               types=['Implementation Type'])
              assert node['implementation-type'] == 'emulator', \
                  "Platform has implementation %s not an emulator" % \
                      (key)
          elif impl_of_type == 'Programming Language':
              check_scalar_ref(data, key, node, 'implementation-type',
                               types=['Implementation Type'])
              if node['implementation-type'] == 'compiler':
                  check_scalar_ref(data, key, node, 'target-language',
                                   types=['Programming Language'])
                  check_optional_scalar_ref(data, key, node, 'target-platform',
                                   types=['Platform'])
          else:
              check_optional_scalar_ref(data, key, node, 'implementation-type',
                               types=['Implementation Type'])

          if 'authors' not in node:
              # TODO: assert there's only one
              pl_node = data[node['implementation-of'][0]]
              node['authors'] = pl_node.get('authors', [])
              node['auspices'] = pl_node.get('auspices', [])

      # All "implementables" (except musical compositions) need to pass these checks.
      if type_ in ['Game', 'Programming Language', 'Library', 'Tool', 'Platform', 'Conlang', 'Electronics Project', 'Demo']:
          assert 'build-requirements' not in node
          assert 'run-requirements' not in node
          check_scalar_ref(data, key, node, 'development-stage',
                           types=['Development Stage'])
          check_optional_scalar_ref(data, key, node, 'variant-of', type_)
          if not node.get('no-specification', False):
              if ('specification-link' not in node and
                  'standards-body' not in node and
                  'reference-distribution' not in node):
                  node['reference-distribution'] = '%s distribution' % key
              if ('specification-link' not in node and
                  'standards-body' not in node):
                  check_scalar_ref(data, key, node, 'reference-distribution',
                                   types=['Distribution'])
                  data[node['reference-distribution']]['reference'] = True

      if type_ in ['Game', 'Programming Language', 'Musical Composition']:
          check_scalar_ref(data, key, node, 'genre', types=['Genre'])
          check_list_ref(data, key, node, 'authors')
      
      if type_ == 'Musical Composition':
          check_scalar_ref(data, key, node, 'composed-on')
          check_scalar_ref(data, key, node, 'using-software')

      if type_ == 'Platform':
          check_scalar_ref(data, key, node, 'native-language', types=['Programming Language'])
          check_list_ref(data, key, node, 'other-languages', types=['Programming Language'])

      if type_ == 'Programming Language':
          check_list_ref(data, key, node, 'paradigms',
                         types=['Programming Paradigm'])
          check_optional_scalar_ref(data, key, node, 'computational-class',
                                    types=['Computational Class'])
          check_optional_scalar_ref(data, key, node, 'member-of',
                                    types=['Programming Language Family'])

      if type_ == 'Programming Language Family':
          check_scalar_ref(data, key, node, 'genre', types=['Genre'])
          check_optional_scalar_ref(data, key, node, 'reference-distribution',
                                    types=['Distribution'])

      if type_ == 'Ranking':
          check_list_ref(data, key, node, 'entries')

    print "%d nodes checked." % count
