Chrysoberyl
===========

*Chrysoberyl* is an attempt to catalogue, and curate, the things produced
by, and related to, Cat's Eye Technologies.

It is something between a wiki and a database and a semantic web and a
pile of goo.

It is supposed to be primarily informative, and only secondarily machine-
processable, and only thirdly structured.  So, the schemas in use are
fuzzy, flexible, incomplete, and subject to change and the drop of a hat.

It does not contain only those things produced by Cat's Eye Technologies;
in theory, anything can be in it.  In these cases, the entry may consist
simply of commentary on the item, or a short explanation of how it relates
to Cat's Eye Technologies.

General Format
--------------

The Chrysoberyl data files are in YAML format, in the `data` directory.

The division into files is artificial; files make no semantic difference;
if they were all concatenated into a single file, the data would be the
same.

Each top-level key in the data is the name of a *node*.  The name should
be both human and machine readable, like the name of a page in a wiki.

To disambiguate nodes which would otherwise have the same name, a
disambiguating phrase may be placed after the name in parentheses.

Each node must have a `type` field, whose value names a node whose `type`
field is `type`.  (This necessitates the presence of a node named `type`
whose `type` is `type`.)

Each node may have any of the following fields:

*   `summary` -- a one-line summary of the node
*   `description` -- a relatively objective description of the node
*   `commentary` -- a subjective opinion, by Chris Pressey, of the node
*   `subtitle` -- expanding on the name of the node
*   `acronym-for` -- expanding the name of the node
*   ...

Each node can have a `domain`, which influences how breadcrumbs are
arranged.  For example, domain of lingography is Chris Pressey.  Domain
of everything which does not specify a domain is Cat's Eye Technologies.
(This scheme is, of course, subject to modifications)

In addition, nodes of particular types may have fields that have meaning
for that type.

Specific Schema
---------------

In the following, an "implementable" (for lack of a better term)
refers to any of the following:

*   a programming language (which includes machine languages)
*   a game
*   a platform (which includes operating systems, architectures, and
    frameworks)
*   a tool
*   a library
*   a musical composition

An implementable may have multiple distributions.  There will typically be
a reference distribution, which contains the spec and/or reference
implementation of the implementable.  If there is no reference distribution,
a link to its specification (even if it's just a page on a wiki) or
standards body (even if it's just "the official website") is needed.
Only one distribution can be the reference distribution for an implementable.

Therefore, every implementable needs at least one of the following:

*   `reference-distribution` (a key)
*   `specification-link` (a URL, or `esowiki`)
*   `standards-body` (a URL)
*   `no-specification: true`

If none of the last three of that list are present, we expect an
implementable to have a `reference-distribution`.  If that key is not present,
we look for a distribution called `FOO distribution` where `FOO` is the name
of the implementable.

An implementable may also have multiple implementations.  Each implementation
may be in zero or more distributions, and a distribution may contain multiple
implementations.  Only one implementation can be the reference implementation
for an implementable.

An implementation may be an implementation of multiple implementables.
(For example, `gcc` is an implementation of ANSI C and C99.)

If an implementation does not give authors, they are assumed to be the
authors of the implementable it implements.  Ditto auspices.

A distribution has releases and, often, can be checked out of some version
control system, and, often, has a place to report bugs.  An implementation,
by itself, has none of those things (at least not in a structured way -- it
might simply be a page on a wiki somewhere.)  The releases of a distribution
should be sorted from earliest to latest.

On the other hand, neither distributions nor implementables have licenses,
but implementations do.  The license of a distribution can be inferred from
the licenses of the implementations contained with it.

Each implementation has an implementation-type.  For a programming language,
this may be interpreter, compiler, etc.  For a platform, this currently must
be "emulator" (even if the platform is a framework...)

An implementation may claim that it is prebuilt in its distribution.  This
assumes it's only in one distribution.  Really, being prebuilt somewhere is
a property of the *distribution*, but this fudging makes some things easier
for now.

Each platform must specify what its native language is.  Implementations
may specify, along with a host language, a host platform.

Every implementable must have a development stage.  The development
stage of an implementation, if not given, is assumed to be on par with the
development stage of the thing it implements.  Distributions never have
development stages, as they are, in a sense, always works in progress.

### side note ###

Any tool which understands a language may be considered an implementation
of that language: an interpreter, a compiler, a parser, a static analyzer, a
pretty-printer, etc., are all implementations.

This is actually kind of weird (e.g. yucca is an implementation of BASIC?
maybe say "partial implementation" in the template if the implementation
type is not interpreter or compiler) but we'll go with it for now.

License
-------

For now, freely redistributable unmodified for non-commercial purposes --
plus you are allowed to fork the repository for the purpose of submitting
corrections to the information.

Script
------

`chrysoberyl` is a Python script included in this distribution which
can process the Chrysberyl database.  It is located in the `bin` directory,
and its source modules are in the `src/chrysoberyl` directory.  Things it
can do include:

*   check the data for consistency (`chrysoberyl check`)
*   render Jinja2 templates with the data (one file per node) and
    dump all nodes to a single JSON file (`chrysoberyl render`)
*   update the Atom news feed (`chrysoberyl announce`)

If mercurial repositories of the distributions are available locally, it
can also:

*   check the distributions for cleanliness (`chrysoberyl survey`)
*   collect documentation from the distributions (`chrysoberyl troll`)
*   create a zipball from the latest tag on a distribution
    (`chrysoberyl release`)

The tool has the following requirements, which can be installed with
`easy_install`:

    atomize
    jinja2
    markdown
    PyYaml

As of this writing, it takes my computer about eight seconds to load,
and check the data and render the templates.

The JSON file is, as of this writing, less than 500K, meaning that, at
broadband speeds it only takes a couple of seconds to download, making
it feasible to implement a client-side query engine for Chrysoberyl
in Javascript.  The size of this file could also be reduced, possibly
substantially.
