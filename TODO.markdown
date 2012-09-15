Chrysoberyl TODO
================

structure
---------

online-implementations should really be a list of implementations,
and implementations should have a list of where they can be found
online.

templates
---------

The root node (at least for breadcrumbs) maybe should be catseye.tc.

News template, with news items inline, sorted by date, and
with anchors, that the links in the feed match up with.

When it does not need building (dist has executables), still, tell
how you would build it if you want to.

Cited in Jargon File --> like esowiki and wikipedia.

Make 'recommended implementation' a snippet, and use it
for test-requirements for distributions.

### obviousity ###

Call out works in progress and ideas in some more obvious way.

When listing things, list ones by Cat's Eye Technologies first, and
put a heading or something.

Show status of / don't prominently link to discontinued distributions.

content
-------

Chrysoberyl has a distribution.

Dipple is a distribution (and implementations are in it.)

Finish cleaning up demos.


perhaps...
----------

screenshots for games.  (again, maybe by implementation)

Something to indicate "specification link forthcoming" instead of
baldly "no specification".

Add indefart_link().  And indefart_linkedlist.  Or really, maybe a
single function format(value, link=True, indefart=True), which
can handle a scalar or a list and such.  Dunno, maybe.

Version numbers on languages.

Competitions by year?

Minimize the size of the dumped JSON: do not include articles, etc.

`quotations` on anything?

`design-goals` on implementables?

If an implementation is the reference implementation, and the
language it's an implementation of has a reference distribution,
assume it's in there, and compute `in-distribution`.

Maybe something other than "emulator" for yoob and BefOS, eh?

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

Even when the language is usually compiled, there might be
a compiler in some dists but not in others (JRE and JDK.)
"An implementation of Java that can build" = JDK.

Account for the fact that some implementations can be
compiled or interpreted under two language (ANSI C and C99
and Borland C++; or in a more involved way, polyglots):
    2iota:
      implementation-of: beta-Juliet
      host-languages:
      - ANSI C
      - C99
    rube.c:
      implementation-of: RUBE
      host-languages:
      - ANSI C
      - C99
      - Borland C

Sort other collections (games, tools, language implementations) by date.
