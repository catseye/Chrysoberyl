# encoding: UTF-8

"""Functions to statically check loaded Chrysoberyl data for consistency and
completeness.

"""

from datetime import datetime
import re

from chrysoberyl.objects import ApproximateDate


LEGACY_FIELDS = (
    'reference-distribution',
    'online-implementations',
    'ca-definition-link',
    'bitbucket',
    'issue-tracker',
    'has-makefile',
    'distname',
    # 'commentary',
)


def check_scalar_ref(universe, key, node, property, link_priority, types=None):
    """Check that the given node has the given property (field) and that it
    is a scalar (not a list.)  If types is given, check that the key contained
    in the field refers to a node of one of those types.

    """
    if property not in node:
        raise KeyError("'%s' does not specify a %s" % (key, property))
    value = node[property]
    if value in link_priority:
        return
    value_node = universe.get_node(value)
    assert value_node, \
        "'%s' has undefined %s '%s'" % (key, property, value)
    if types is None:
        return
    if value_node['type'] not in types:
        raise KeyError(
            "'%s' has %s '%s' which is a %s, not a %s" %
            (key, property, value, value_node['type'], types)
        )


def check_optional_scalar_ref(universe, key, node, property, link_priority, types=None):
    """Like check_scalar_ref, but skip if property not present on node."""
    if property in node:
        check_scalar_ref(universe, key, node, property, link_priority, types=types)


def check_list_ref(universe, key, node, property, link_priority, types=None):
    """Check that the given node has the given property (field) and that it
    is a list (not a scalar.)  If types is given, check that all keys
    contained in the list refers to a node of one of those types.

    """
    if property not in node:
        raise KeyError(u"'%s' has no %s list" % (key, property))
    assert isinstance(node[property], list), \
        u"'%s' has non-list %s" % (key, property)
    for value in node[property]:
        if value in link_priority:
            continue
        value_node = universe.get_node(value)
        assert value, \
            u"'%s' has undefined %s '%s'" % \
            (key, property, value)
        if types is not None:
            assert value_node['type'] in types, \
                u"'%s' has %s '%s' which is a %s, not a %s" % (
                    key, property, value, value_node['type'], types)


def check_optional_list_ref(universe, key, node, property, link_priority, types=None):
    """Like check_list_ref, but skip if property not present on node."""
    if property in node:
        check_list_ref(universe, key, node, property, link_priority, types=types)


def resolve_internal_links(universe, data, key, property, text, link_priority):
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
        if thing in link_priority:
            continue
        assert universe.get_node(thing), \
            "'%s' mentions undefined '%s' in '%s'" % \
            (key, thing, property)


def check_chrysoberyl_node(universe, data, key, node, link_priority):
    """Check that the data in the given node is consistent and
    complete.

    Note that this may have side-effects (altering the contents of the
    node.)  `inception-date` fields are converted to ApproximateDate
    objects, and `publication-date` fields are converted to datetime objects.
    The following fields may be set to a default based on the presence of a
    node or field with a similar name:
        `in-distributions`
    Also, `authors` and `auspices` may be inherited from the implementable
    being implemented.

    Based on 'mediums' on an online installation, installation-of and other
    things may be auto-populated.

    """
    # Every node must have a valid type.
    assert 'type' in node, \
        "'%s' does not specify a type" % key
    type_ = node['type']

    try:
        universe.get_space_key_node(type_)
    except KeyError:
        raise KeyError("{} has type {} which has no node".format(key, type_))

    assert universe.get_space_key_node(type_), \
        "'%s' specifies undefined type '%s'" % (key, type_)
    type_node = universe.get_node(type_)
    assert type_node.get('type') == 'type', \
        "'%s' has bad type '%s'" % (key, type_node)

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
        if 'article-date' in node:
            assert node['type'] == 'Article'
            node['article-date'] = \
                ApproximateDate(str(node['article-date']))
    except Exception:
        print "'%s' has bad article-date '%s'" % (
            key, node['article-date']
        )
        raise
    try:
        if 'publication-date' in node:
            # Tue, 17 May 2011 23:43:10 GMT
            node['publication-date'] = datetime.strptime(
                str(node['publication-date']), '%a, %d %b %Y %H:%M:%S GMT'
            )
    except Exception:
        print "'%s' has bad publication-date '%s'" % (
            key, node['publication-date']
        )
        raise
    check_optional_scalar_ref(universe, key, node, 'domain', link_priority)
    check_optional_list_ref(universe, key, node, 'see-also', link_priority)
    check_optional_scalar_ref(universe, key, node, 'genre', link_priority)
    check_optional_list_ref(universe, key, node, 'authors', link_priority,
        types=('Individual', 'Organization'))
    check_optional_list_ref(universe, key, node, 'auspices', link_priority,
        types=('Organization',))
    check_optional_list_ref(universe, key, node, 'influences', link_priority)
    # These two fields go together.
    if 'auspices' in node:
        assert 'authors' in node, "auspices but no authors in '%s'" % key
    if 'submitted-to' in node:
        for sub in node['submitted-to']:
            check_scalar_ref(universe, key, sub, 'competition', link_priority,
                             types=('Competition',))
    if 'images' in node:
        for image in node['images']:
            assert 'url' in image, 'image %r has no url' % image

    # Every node may have these, and they may have internal links.
    description = None
    if 'description' in node:
        description = node['description']
    resolve_internal_links(universe, data, key, 'description', description, link_priority)
    commentary = None
    if 'commentary' in node:
        commentary = node['commentary']
    resolve_internal_links(universe, data, key, 'commentary', commentary, link_priority)
    as_a_prerequisite = None
    if 'as-a-prerequisite' in node:
        as_a_prerequisite = node['as-a-prerequisite']
    resolve_internal_links(universe, data, key, 'commentary', as_a_prerequisite, link_priority)

    # No nodes may have legacy fields.
    for legacy_field in LEGACY_FIELDS:
        assert legacy_field not in node, \
            "legacy field '%s' found in '%s'" % (legacy_field, key)

    check_optional_scalar_ref(universe, key, node, 'development-stage', link_priority,
                              types=('Development Stage',))

    # On to checking fields specific to different types.

    if type_ == 'Disambiguation node':
        check_optional_list_ref(universe, key, node, 'entries', link_priority)

    if type_ == 'Article':
        assert 'publication-date' in node
        assert 'article-type' in node

    if type_ == 'Online Installation':
        node['interactive'] = node.get('interactive', False)
        node['animated'] = node.get('animated', False)
        check_list_ref(
            universe, key, node, 'mediums', link_priority, types=(
                'Platform', 'Programming Language', 'Implementation', 'Image Format', 'Medium'
            )
        )

        if 'javascript-urls' in node:
            assert 'javascript-module' in node, key
            for url in node['javascript-urls']:
                assert not url.startswith('../module'), url

        assert 'mp3' not in node['mediums']

        check_scalar_ref(universe, key, node, 'installation-of', link_priority,
                         types=('Implementation',))

    if type_ == 'Distribution':
        assert 'development-stage' not in node, \
          "%s mentions 'development-stage'" % key
        check_optional_list_ref(universe, key, node, 'test-requirements', link_priority,
                                types=('Programming Language', 'Tool'))

    if type_ == 'Implementation':
        check_list_ref(universe, key, node, 'implementation-of', link_priority)
        check_optional_scalar_ref(universe, key, node,
                                  'recommended-implementation', link_priority,
                                  types=('Implementation',))

        # for convenience, bring in the type of the thing being implemented
        # the first thing.  we assume they're all the same type.  but...
        # hey, let's build something that implements both Underload and
        # Zoning Variance #5!
        implemented_thing = node['implementation-of'][0]
        if implemented_thing in ('Commodore 64',):
            impl_of_type = 'Platform'
        else:
            impl_of_type = data[implemented_thing]['type']

        check_scalar_ref(universe, key, node, 'license', link_priority, types=('License',))
        if 'in-distribution' in node:
            assert 'in-distributions' not in node
            node['in-distributions'] = [node['in-distribution']]
            del node['in-distribution']
        check_optional_list_ref(universe, key, node, 'in-distributions', link_priority,
                                  types=('Distribution',))
        check_optional_list_ref(universe, key, node, 'prebuilt-for-platforms', link_priority,
                                  types=('Platform', 'Programming Language'))
        if impl_of_type == 'Picture':
            check_scalar_ref(universe, key, node, 'host-language', link_priority,
                             types=('Image Format',))
        else:
            assert impl_of_type != 'Musical Composition'
            check_scalar_ref(universe, key, node, 'host-language', link_priority,
                             types=('Programming Language',))
        check_optional_scalar_ref(universe, key, node, 'host-platform', link_priority,
                         types=('Platform',))
        # these shouldn't really be needed.  derive, derive!
        # I really don't like that 'Programming Language' is in these
        check_optional_list_ref(universe, key, node, 'build-requirements', link_priority,
                         types=('Library', 'Tool', 'Programming Language'))
        check_optional_list_ref(universe, key, node, 'run-requirements', link_priority,
                         types=('Library', 'Tool', 'Programming Language'))

        if impl_of_type == 'Platform':
            check_scalar_ref(universe, key, node, 'implementation-type', link_priority,
                             types=('Implementation Type',))
            platimpls = ('emulator', 'framework', 'operating system')
            assert node['implementation-type'] in platimpls, \
                "Platform has implementation %s not in %r" % \
                    (key, platimpls)
        elif impl_of_type == 'Programming Language':
            check_scalar_ref(universe, key, node, 'implementation-type', link_priority,
                             types=('Implementation Type',))
            if node['implementation-type'] == 'compiler':
                check_scalar_ref(universe, key, node, 'target-language', link_priority,
                                 types=('Programming Language',))
                check_optional_scalar_ref(universe, key, node, 'target-platform', link_priority,
                                 types=['Platform'])
        else:
            check_optional_scalar_ref(universe, key, node, 'implementation-type', link_priority,
                             types=('Implementation Type',))

        if 'authors' not in node:
            # TODO: assert there's only one
            if node['implementation-of'][0] == 'Commodore 64':
                pl_node = {}
            else:
                pl_node = data[node['implementation-of'][0]]
            node['authors'] = pl_node.get('authors', [])
            node['auspices'] = pl_node.get('auspices', [])

    # All "implementables" need to pass these checks.
    # Programming Language Family isn't *directly* implementable
    # but it must pass these checks too.  And gets ref-dist linked
    # to it here too.
    if type_ in ['Game', 'Programming Language', 'Library', 'Tool',
                 'Platform', 'Conlang', 'Electronics Project', 'Gewgaw',
                 'Automaton', 'Programming Language Family', 'Text',
                 'Picture']:
        assert 'build-requirements' not in node
        assert 'run-requirements' not in node
        if type_ != 'Picture':
            check_scalar_ref(universe, key, node, 'development-stage', link_priority,
                             types=['Development Stage'])
        check_optional_scalar_ref(universe, key, node, 'sample-credit', link_priority,
                                  'Individual')
        check_optional_scalar_ref(universe, key, node, 'variant-of', type_)
        check_optional_list_ref(universe, key, node, 'online-implementations', link_priority,
                                types=['Online Installation'])

        # to do this properly we'd need to check ref. impls.
        #if not node.get('no-specification', False):
        #    if ('specification-link' not in node and
        #        'standards-body' not in node):
        #        check_scalar_ref(universe, key, node, 'defining-distribution',
        #                         types=['Distribution'])
        check_optional_scalar_ref(universe, key, node, 'defining-distribution', link_priority,
                                  types=['Distribution'])

    # alternate constraints for musical pieces (implementables)
    assert type_ != 'Musical Composition'

    # additional constraints for games (implementables)
    if type_ == 'Game':
        check_scalar_ref(universe, key, node, 'genre', link_priority, types=['Genre'])
        check_optional_scalar_ref(universe, key, node, 'platform', link_priority,
                                  types=['Platform'])
        check_list_ref(universe, key, node, 'authors', link_priority)

    # additional constraints for platforms (implementables)
    if type_ == 'Platform':
        check_scalar_ref(universe, key, node, 'native-language', link_priority,
                         types=['Programming Language'])
        check_list_ref(universe, key, node, 'other-languages', link_priority,
                       types=['Programming Language'])

    # additional constraints for proglangs (implementables)
    if type_ in ('Programming Language', 'Automaton'):
        check_scalar_ref(universe, key, node, 'genre', link_priority, types=['Genre'])
        check_list_ref(universe, key, node, 'authors', link_priority)
        check_list_ref(universe, key, node, 'paradigms', link_priority,
                       types=('Programming Paradigm',))
        check_optional_scalar_ref(universe, key, node, 'computational-class', link_priority,
                                  types=('Computational Class',))
        check_optional_scalar_ref(universe, key, node, 'member-of', link_priority,
                                  types=('Programming Language Family',))

    if type_ == 'Programming Language Family':
        check_scalar_ref(universe, key, node, 'genre', link_priority, types=['Genre'])

    if type_ == 'Ranking':
        check_list_ref(universe, key, node, 'entries', link_priority)


def check_chrysoberyl_data(universe, data, link_priority):
    """Check all nodes in the given dictionary of Chrysoberyl data."""
    count = 0
    for key in data:
        count += 1
        check_chrysoberyl_node(universe, data, key, data[key], link_priority)
    print "%d nodes checked." % count
