Chrysoberyl TODO
================

higher priority
---------------

News template, with news items inline, sorted by date, and
with anchors, that the links in the feed match up with.

News archive.  (Could be the News Item index, sorted by date.)

News dates should be real date objects, so we can sort by them.

Render images.  (LED-386, Mildred, games...)

Render documentation to a separate directory and link to it.

Some replacement for project page.  (Featured?)

For (in theory) any item, show all lists that it is present in.

styling
-------

use black background for nav header:

    Cat's Eye Technologies       Home News About Featured Search

use white background for all else.

use two-column layout for (thing, thing distribution)

Don't have separate distribution nodes for ref dists.

tool
----

Function to check broken links.

Function to test local repos.

metanodes
---------

Improve query.

Use chosen in the query page.

structure
---------

`in-distributions`, a list.

templates
---------

Don't show discontinued distributions inline.

Nodes with blank article cause footer to be pushed down below viewable area.

"It is distributed in the Flobnar distribution and it is distributed
under the BSD license" sounds awful.
 
In implementable, Implementations should be next to reference distribution
+ should show which implementations are reference (in lingography too)

Actually, in lingography, be more terse.  "Implementations include
the reference interpreter blah.c and the compiler blah.boo" should be fine.

When it does not need building (dist has executables), still, tell
how you would build it if you want to.

Render sample-output and sample-credit.

### obviousity ###

Call out works in progress and ideas in some more obvious way.

When listing things, list ones by Cat's Eye Technologies first, and
put a heading or something.

Show status of / don't prominently link to discontinued distributions.

content
-------

Link Chrysoberyl to Chrysoberyl distribution somehow.

perhaps...
----------

Don't necessarily even make nodes for reference distributions.

Cited in Jargon File --> like esowiki and wikipedia.

online-implementations should really be a list of implementations,
and implementations should have a list of where they can be found
online.

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
