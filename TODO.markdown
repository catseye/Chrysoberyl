Chrysoberyl TODO
================

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

For (in theory) any item, show all lists that it is present in.

Add release-date, as opposed to inception-date. (Infer from first distribution.)

Document what the different dates mean.

documentation nodes
-------------------

Link to github file from documentation nodes.

Breadcrumbs: descend from distribution/implementable in documentation nodes.

templates
---------

For Type and Genre pages, show the pages of that type/genre in a collapsible
(accordion) thing.  If there are a lot (more than, say, 15,) default the accordion
to collapsed.

Longer descriptions and commentary (article-like things) should have a
max-width smaller than the screen size, to help readability.

On implementable pages, show non-reference dists (if any) after reference dist.

Don't show discontinued distributions inline (the same way).

Show status of discontinued distributions.

Nodes with blank article cause footer to be pushed down below viewable area.

"It is distributed in the Flobnar distribution and it is distributed
under the BSD license" sounds awful.
 
"It is distributed in the Flobnar distribution" -- Flobnar distribution should
be a link to the implementable node which contains that distribution inline.
Or possibly we should just bring back distribution nodes now.
 
Actually, in lingography, be more terse.  "Implementations include
the reference interpreter blah.c and the compiler blah.boo" should be fine.

When it does not need building (dist has executables), still, tell
how you would build it if you want to.

### obviousity ###

Embolden entries in lingography, gameography, etc.

Call out works in progress and ideas in some more obvious way.

When listing things, list ones by Cat's Eye Technologies first, and
put a heading or something.

content
-------

Link Chrysoberyl to Chrysoberyl distribution somehow.

perhaps...
----------

Cited in Jargon File --> like esowiki and wikipedia.

Perhaps merge Online Installation with Implementation.  Or perhaps make
Online Installations not in the `node` namespace at all (they're not
informative articles about subjects, they are containers for subject contents.)

Add a single function format(value, link=True, indefart=True), which
can handle a scalar or a list and such.

Version numbers on languages.

Competitions by year?

Minimize the size of the dumped JSON: do not include articles, etc.

`quotations` on anything?

`design-goals` on implementables?

Some documentation in a reference distribution relates to the implementable
and some of it relates to the distribution and some of it relates to
the implementation(s) within the distribution.  Split it up so.
(Note: this is a hard problem.  Ultimate solution is probably to have
Specification type nodes.  These (and implementation) nodes can contain
filenames relative to the root of the distribution.  Actually a specification
is a special kind of implementation.)

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

When the only dependency is IBM PC compatible -- special case that,
don't recommend Bochs like that :/

"Portable" for POSIX and NetBSD.

Petulant Cursor and RIBOS share all their documentation.  And don't
list a distribution.  Maybe they should be seperate or maybe I should
figure out a way to say that a project is in "this part" of a distribution.

Preprocess LHS before markdowning it (indent > blocks)
