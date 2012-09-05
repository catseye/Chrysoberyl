Chrysoberyl
===========

TODO
----

### structure ###

Permit sorting by date.

Dump dates sensibly to JSON.

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

(that's an "or")

### templates ###

Add indefart_link().  And indefart_linkedlist.  Or really, maybe a
single function format(value, link=True, indefart=True), which
can handle a scalar or a list and such.  Dunno, maybe.

Display online implementation in lingography.  And elsewhere.

Sort lingography and other collections by date.

Dates on implementable pages.

When it does not need building (dist has executables), still, tell
how you would build it if you want to.

Call out works in progress and ideas in some more obvious way.

When listing things, list ones by Cat's Eye Technologies first, and
put a heading or something.

Use HTML5 sections instead of divs.

Terminology on music pages:
-   "implementation" -> "rendition"
-   "is written in MP3" -> "as an MP3 file"
-   "To run this implementation" -> "To listen to this rendition"
-   "an implementation of MP3" -> "an MP3 player"

Cited in Jargon File --> like esowiki and wikipedia.

For a competition, list all submissions.

bylines for programming language familys and for conlangs

List all programming languages for a computational class.

On a programming language, display its computational class.

### content ###

Allll those variants of Pixley.






### perhaps ###

Minimize the size of the dumped JSON: do not include articles, etc.

`quotations` on anything?

`design-goals` on implementables?

If a distribution is a 'X distribution', compute `distribution-of`.

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
