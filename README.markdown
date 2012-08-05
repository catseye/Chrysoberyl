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
simply of commentary on the item.

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

*   `abstract` or `description` (equivalent)
*   ...

In addition, nodes of particular types may have fields that have meaning
for that type.

Specific Schema
---------------

A language may have multiple distributions.  There will typically be
a reference distribution, which contains the spec and/or reference
implementation of the language.  (Although, this "distribution" might
just be a page on a wiki.)  Only one distribution can be the reference
distribution for a language.

A language may also have multiple implementations.  Each implementation
may or may not be in a distribution; a distribution may contain
multiple implementations.  Only one implementation can be the reference
implementation for a language.

Any tool which understands a language may be considered an implementation:
an interpreter, a compiler, a parser, a static analyzer, a pretty-printer,
etc., are all implementations.

License
-------

For now, freely redistributable unmodified -- plus you are allowed
to fork the repository for the purpose of submitting corrections to the
information.
