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

In addition, nodes of particular types may have fields that have meaning
for that type.

Specific Schema
---------------

In the following, an "implementable" (for lack of a better term)
refers to a programming language, or a game, or a platform, or a tool or
a library.

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

If neither of the second two are present, we expect an implementable to
have a `reference-distribution`.  If that key is not present, we look
for a distribution called `FOO distribution` where `FOO` is the name of
the implementable.

An implementable may also have multiple implementations.  Each implementation
may be in zero or more distributions, and a distribution may contain multiple
implementations.  Only one implementation can be the reference implementation
for an implementable.

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
be "emulator".

Each platform must specify what its native language is.  Implementations
may specify, along with a host language, a host platform.

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

TODO
----

### structure ###

Some documentation in a reference distribution relates to the implementable
and some of it relates to the distribution and some of it relates to
the implementation(s) within the distribution.  Split it up so.

Some implementations can both compile and interpret.  Some compilers
can target multiple target languages.  Handle both of these.

Generalize "Family" to be families of anything, perhaps.

Perhaps nodes can "belong to" other nodes: lingography and favourite
video games "belong" to Chris Pressey, etc.  (For now it's `see-also`.)

Compilers should be able to specify a target platform (distinct from target
language.)

Maybe something other than "emulator" for yoob and BefOS, eh?

Run requirements and build requirements can be optional.

### templates ###

**Compute if an implementation requires building, based on what language
it's in (C, yes, Python, no, Java and Erlang, depends on the distribution),
and what tools you need ("as a prerequisite") for building or running.**

Better provision of documentation in templates.

Extrapolate the above two for distributions (do that for each implementation
in the distribution.)

If an implementation allows visual debugging or animation, note that.

List all implementations whose host-language is this language.

List all (compiler) implementations whose target-language is this language.

### content ###

More descriptions on things.  Descriptions objective, commentary subjective.

Add my music.

Add LoUIE.

### other ###

Better collection of documentation.
