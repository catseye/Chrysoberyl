# encoding: UTF-8

"""Functions to statically check loaded Chrysoberyl data for consistency and
completeness.

"""

from datetime import datetime
import re

from chrysoberyl.objects import ApproximateDate


LEGACY_FIELDS = ()


def check_scalar_ref(data, key, node, property, types=None):
    """Check that the given node has the given property (field) and that it
    is a scalar (not a list.)  If types is given, check that the key contained
    in the field refers to a node of one of those types.

    """
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
    """Like check_scalar_ref, but skip if property not present on node."""
    if property in node:
        check_scalar_ref(data, key, node, property, types=types)


def check_list_ref(data, key, node, property, types=None):
    """Check that the given node has the given property (field) and that it
    is a list (not a scalar.)  If types is given, check that all keys
    contained in the list refers to a node of one of those types.

    """
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
    """Like check_list_ref, but skip if property not present on node."""
    if property in node:
        check_list_ref(data, key, node, property, types=types)


def resolve_internal_links(data, key, property, text):
    """Check that all cross-references (in [[double brackets]]) in the
    text contained in the given property are keys of nodes that exist
    elsewhere in the Chrysoberyl data.

    """
    if text is None:
        return True
    for match in re.finditer(r'\[\[(.*?)\]\]', text):
        link = match.group(1)
        segments = link.split('|')
        thing = segments[0]
        assert thing in data, \
            "'%s' mentions undefined '%s' in '%s'" % \
            (key, thing, property)


def check_chrysoberyl_node(data, key, node):
    """Check that the data in the given node is consistent and
    complete.

    Note that this may have side-effects (altering the contents of the
    node.)  `inception-date` fields are converted to ApproximateDate
    objects, and `news-date` fields are converted to datetime objects.
    `distribution-of` and `in-distributions` and `reference-distribution`
    may be set to defaults based on the presence of a node or field with
    a similar name.  `authors` and `auspices` may be inherited from
    the implementable being implemented.

    """
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
            node['inception-date'] = \
                ApproximateDate(str(node['inception-date']))
    except Exception:
        print "'%s' has bad inception-date '%s'" % (
            key, node['inception-date']
        )
        raise
    try:
        if 'news-date' in node:
            assert node['news-date'] != 'Unknown'
            # Tue, 17 May 2011 23:43:10 GMT
            node['news-date'] = datetime.strptime(
                str(node['news-date']), '%a, %d %b %Y %H:%M:%S GMT'
            )
    except Exception:
        print "'%s' has bad news-date '%s'" % (key, node['news-date'])
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
            check_scalar_ref(data, key, sub, 'competition',
                             types=['Competition'])

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

    if type_ == 'Online Installation':
        assert 'exhibit-link' not in node
        node['interactive'] = node.get('interactive', False)
        node['animated'] = node.get('animated', False)
        assert 'medium' in node

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
                       types=('Programming Language',
                              'Programming Language Family',
                              'Game', 'Tool', 'Library',
                              'Electronics Project',
                              'Demo', 'Conlang', 'Platform', 'Database'))
        check_optional_list_ref(data, key, node, 'test-requirements',
                                types=('Programming Language', 'Tool'))

    if type_ == 'Implementation':
        check_list_ref(data, key, node, 'implementation-of')
        check_optional_scalar_ref(data, key, node,
                                  'recommended-implementation',
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
                             types=['Music Format'])
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

    # All "implementables" (except musical compositions)
    # need to pass these checks.
    if type_ in ['Game', 'Programming Language', 'Library', 'Tool',
                 'Platform', 'Conlang', 'Electronics Project', 'Demo']:
        assert 'build-requirements' not in node
        assert 'run-requirements' not in node
        check_scalar_ref(data, key, node, 'development-stage',
                         types=['Development Stage'])
        check_optional_scalar_ref(data, key, node, 'variant-of', type_)
        check_optional_list_ref(data, key, node, 'online-implementations',
                                types=['Online Installation'])

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
        check_optional_scalar_ref(data, key, node, 'composed-on')
        check_optional_scalar_ref(data, key, node, 'using-software')
        check_scalar_ref(data, key, node, 'development-stage',
                         types=['Development Stage'])

    if type_ == 'Platform':
        check_scalar_ref(data, key, node, 'native-language',
                         types=['Programming Language'])
        check_list_ref(data, key, node, 'other-languages',
                       types=['Programming Language'])

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


def check_chrysoberyl_data(data):
    """Check all nodes in the given dictionary of Chrysoberyl data."""
    count = 0
    for key in data:
        count += 1
        check_chrysoberyl_node(data, key, data[key])
    print "%d nodes checked." % count
