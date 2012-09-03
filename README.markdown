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

An implementation may claim that it is prebuilt in its distribution.  This
assumes it's only in one distribution.  Really, being built somewhere is
a property of the distribution, but this fudging makes some things easier
for now.

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

Sort by dates.

Display implementations in lingography.

Display online implementation in lingography.  And elsewhere.

Display sample code in lingography and language node.

Display date in lingography and other nodes.  Sort lingography by date.

Collection: Music by Chris Pressey.

Collection: Works in Progress by Chris Pressey.

Have some way to generally recommend a particular implementation
for this purpose (e.g. generally recommend Perl 5.8.some).
(If there is only one implementation, just pick it.  Or an implementation
can specify.)

Don't say "requires Java for yoob".

Even when the language is usually compiled, there might be
a compiler in some dists but not in others (JRE and JDK.)
"An implementation of Java that can build" = JDK.

Account for the fact that some implementations can be
compiled or interpreted under two language (ANSI C and C99; or
in a more involved way, polyglots.)  `host-languages`?

When it does not need building (dist has executables), still, tell
how you would build it if you want to.

Call out works in progress and ideas in some more obvious way.

When listing things, list ones by Cat's Eye Technologies first, and
put a heading or something.

Use HTML5 (header, content, footer) instead of divs.

Terminology on music pages:
-   "implementation" -> "rendition"
-   "is written in MP3" -> "as an MP3 file"
-   "To run this implementation" -> "To listen to this rendition"
-   "an implementation of MP3" -> "an MP3 player"

### content ###

Add implementations of languages you might need (perl for Perl, gcc for C, ...)

Objective descriptions on all my languages.

### perhaps ###

Maybe something other than "emulator" for yoob and BefOS, eh?

Dump all Chrysoberyl data as a JSON blob, see how big it is, and if
it can be reduced by making post-hoc rules about default values.

Some documentation in a reference distribution relates to the implementable
and some of it relates to the distribution and some of it relates to
the implementation(s) within the distribution.  Split it up so.
(Note: this is a hard problem.  Just list the specifications explicitly in
the distribution node, as filenames relative to the distribution -- the rest
is "other")

Some implementations can both compile and interpret.  Some compilers
can target multiple target languages.  Handle both of these.

Run requirements and build requirements can be optional.

Have some way to indicate, on the implementation, that it needs
building, even if the language is not always compiled (Haskell.)
Actually, it's usually obvious if a Haskell impl needs building, and
usually optional, but anyway.
