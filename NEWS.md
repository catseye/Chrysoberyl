# Cat's Eye Technologies: New Developments

*   author: Chris Pressey
*   url: https://catseye.tc/feeds/atom_30_news.xml
*   link-to-anchors-on: https://catseye.tc/article/News
*   link-target-url: https://catseye.tc/article/News

_Note, this feed dates back to 2019.  For older news items, please see the_
**[Archived News Items](http://catseye.tc/article/Archived_News_Items)**
_article._

### Eqthy, a formalized language for proofs in equational logic

*   summary: [Eqthy](https://catseye.tc/node/Eqthy) is a formalized language for proofs in equational logic.
*   date: Wed, 01 Feb 2023 18:29:25 GMT

[Eqthy](https://catseye.tc/node/Eqthy) is a formalized language for proofs
whose design attempts to reconcile _simplicity of implementation on a machine_
with _human usability_.  Each line gives an equation which is derived from
the equation on the previous line, using only the rules of equational logic
along with any previously defined rules of inference or proved theorems.

This, the first release of the Eqthy distribution (Eqthy 0.1),
includes a description of the language, a proof checker called `eqthy`
written in Python 3, and a number of example proofs (including a proof
of the Socks and Shoes theorem in group theory, and a simple proof
in Propositional Algebra).

### relwrite, a tool for relating strings to strings

*   summary: [relwrite](https://catseye.tc/node/relwrite) is a tool for relating strings to strings.
*   date: Fri, 27 Jan 2023 09:29:29 GMT

Last year, like most years since 2013, Cat's Eye Technologies planned to produce something for
[NaNoGenMo](https://catseye.tc/node/NaNoGenMo).
The year 2022 was, actually, the first year I entered and failed to complete anything.
The reasons for this were simple, and probably not uncommon: my plans were too
ambitious, and were difficult to scale back to something modest enough to be
completable in one month.  So it goes.

What I did produce, along the way, is a tool called [`relwrite`](https://catseye.tc/node/relwrite).
Given a grammar and an input string, `relwrite` will find a set of output strings
that relate to the input strings, either by _parsing_ the input to obtain a nonterminal,
or by _generating_ a new string of terminals, at the user's choice.

One thing that makes this interesting is its generality.  The input grammar
doesn't have to be context-free; it can be literally anywhere in the
Chomsky hierarchy.

And this poses complications.  `relwrite` can be instructed to perform a naive
breadth-first search for all the outputs that the input could rewrite to.
But since that is an infeasibly large space to traverse, it supports a
more sophisticated [beam search](https://en.wikipedia.org/wiki/Beam_search)
algorithm, to aggressively trim down the set of possible parses
(or generations), to allow it to find at least one of a desired length.

### Release of Samovar 0.5

*   summary: Version 0.5 of [Samovar](https://catseye.tc/node/Samovar) has been released.
*   date: Thu, 26 Jan 2023 19:27:00 GMT

A new version of the [Samovar](https://catseye.tc/node/Samovar)
distribution has been released.  While there are no changes to the
Samovar language, the reference implementation (`samovar`, written
in Python) has some significant updates.

Notably, alongside the existing stochastic generator (which just
performs random walks through the event-space in the hopes of
connecting the initial state of the scene to a satisfactory final
event of the scene) version 0.5 of `samovar` supports two additional
generation strategies:

*   a breadth-first search-based generator, which is complete, in the
    sense that it will always find the shortest series of events that
    leads to the goal, as long as such a series exists.
*   a depth-first search based generator as well. If the space of
    world-configurations is finite (I'm not sure if Samovar guarantees
    this, but it's often the case), this also is a complete generator,
    and more efficient than the breadth-first one.

Some mildly humorous examples resulting from applying these two strategies to chapters of
[The League of Extraordinarily Dull Gentlemen](https://catseye.tc/article/Texts.md#the-league-of-extraordinarily-dull-gentlemen)
are presented in this gist:
["The League of Efficiently Dull Gentlemen"](https://gist.github.com/cpressey/9450c3b793e81f369a5fa751cc9298cf).

### Lariat: A Total ADT for Proper Lambda Terms

*   summary: [Lariat](https://catseye.tc/node/Lariat) is a total ADT for proper lambda terms.
*   date: Wed, 12 Oct 2022 06:48:57 GMT

Y'know what?  Over the years, I've designed lots of strange small programming
languages, but I never implemented the lambda calculus.  Until now.

And I only did it as a test case for an abstract data type representing
lambda terms.

And I spent quite some time working on said abstract data type, trying to make
something that works, in my opinion, nicely.  The result being something that
is total, in the sense that all operations are always defined, and that
represents only proper lambda terms -- improperly bound variables cannot be
introduced.

And I'm not even entirely sure anymore why I wanted to formulate said
abstract data type for lambda terms.  I believe it may have had something
to do with macros.

Even though I dislike macros, and avoid them like the plague in my own code.

Well, that's how much sense my life makes.

Anyway, [Lariat](https://catseye.tc/node/Lariat).

### Philomath: Write proofs in ANSI C

*   summary: [Philomath](https://catseye.tc/node/Philomath) is an [LCF-style](https://catseye.tc/node/LCF-style-ND) theorem prover in [ANSI C](https://catseye.tc/node/ANSI_C).
*   date: Tue, 06 Sep 2022 16:40:41 GMT

Ever had an urge to write that natural deduction proof you're working on
directly in a classic systems programming language like [ANSI C](https://catseye.tc/node/ANSI_C)?
Well, look no further!  [Philomath](https://catseye.tc/node/Philomath) is an
[LCF-style](https://catseye.tc/node/LCF-style-ND) theorem prover for
propositional logic in a natural deduction system, written in ANSI C.
Values of type `struct theorem` represent proved statements, while
functions that take `struct theorem`s as arguments and return a new
`struct theorem` value, implement rules of inference.  Your proof-program
includes the header file `theorem.h`, which only exposes the
declaration of `struct theorem`, and not its definition; in this way,
you can be confident (in ANSI C) that any `struct theorem` your proof-program
produces indeed represents a theorem with a valid proof, and not just
something you made up.  In ANSI C.  Smashing, no?

### Feedmark 0.13 and Falderal 0.14 released

*   summary: [Feedmark](https://catseye.tc/node/Feedmark) 0.13 and [Falderal](https://catseye.tc/node/Falderal) 0.14 have been released.
*   date: Thu, 01 Sep 2022 19:04:14 GMT

Two releases of two of Cat's Eye Technologies' formats
(and associated tools) have been made.

The latest version of [Feedmark](https://catseye.tc/node/Feedmark), a structured
subset of Feedmark designed to support curation and newsfeeds, is now version 0.13.

The latest version of [Falderal](https://catseye.tc/node/Falderal), a format for
writing literate test suites for programming languages, is now version 0.14
"Jean Baptiste Point DuSable Lake Shore Drive".  (Falderal versions are named
after notable locations in the Chicagoland area.)

Both of these formats have tools written in Python, and these packages
are both available on the Python Package Index, at
[Feedmark](https://pypi.org/project/Feedmark/) and
[Falderal](https://pypi.org/project/Falderal/) respectively.

### Recent updates to the ZOWIE distribution

*   summary: A second implementation of [ZOWIE](https://catseye.tc/node/ZOWIE) has been written.
*   date: Fri, 17 Dec 2021 08:34:11 GMT

This year, a typo was found in the specification of our esoteric programming
language [ZOWIE](https://catseye.tc/node/ZOWIE) -- a language where every instruction,
including the structured "repeat" loop, is memory-mapped.  (Thanks Sgeo!)

From this we decided it would be ideal if there was a second implementation of
the language -- the idea being, with three reference materials
(the spec and two reference implementations) one could use a "majority rules"
approach to divine the canonical behaviour.

(Three cheers for coding theory!  Hip hip, hooray!  Hip hip, hooray!
Hoop hoop, hirray!)

To this end, we wrote a ZOWIE interpreter in Haskell, to go along with the one
written in Python.

We considered using this new Haskell implementation as the basis for
[the online installation of ZOWIE](https://catseye.tc/node/ZOWIE), replacing
the current Skulpt-based installation with it.  That hasn't happened yet, though;
I'm torn between getting rid of the Skulpt one because Skulpt is kind of goony and
non-standard, and keeping the Skulpt one because Skulpt is kind of goony and
non-standard.

### Tandem interpreter installed online

*   summary: An interpreter for [Tandem](https://catseye.tc/node/Tandem) is now [available online](https://catseye.tc/installation/Tandem).
*   date: Thu, 16 Dec 2021 11:43:57 GMT

[Tandem](https://catseye.tc/node/Tandem), our esoteric programming language where
string-rewriting rules form a Kleene algebra, has finally
had an HTML installation for it established on Cat's Eye Technologies' website.
You can [try it in your web browser right here](https://catseye.tc/installation/Tandem).

### The Grammatical Rollercoaster that is Dissociated Parse

*   summary: [Dissociated Parse](https://catseye.tc/node/Dissociated_Parse), an algorithm devised during [NaNoGenMo 2021](https://catseye.tc/node/NaNoGenMo_2021).
*   date: Wed, 08 Dec 2021 22:48:09 GMT

For NaNoGenMo this year, Cat's Eye Technologies developed a variation
on the [Dissociated Press](https://en.wikipedia.org/wiki/Dissociated_press)
algorithm.  Instead of working on a sequential list of words as it
conventionally does, it was adapted to work on parse trees instead.
The result was dubbed [Dissociated Parse](https://catseye.tc/node/Dissociated_Parse),
and the 50K-word novel [The Lion, the Witches, and the Weird Road](https://catseye.tc/node/The_Lion,_the_Witches,_and_the_Weird_Road) was generated using it, which you can
[read online here](https://catseye.tc/view/Dissociated-Parse/generated/The%20Lion,%20the%20Witches,%20and%20the%20Weird%20Road.md).

### Vinegar, a semi-concatenative language

*   summary: [Vinegar](https://catseye.tc/node/Vinegar), a "semi-concatenative" language, has been released.
*   date: Sun, 05 Dec 2021 21:08:51 GMT

[Vinegar](https://catseye.tc/node/Vinegar) is a new esolang from Cat's Eye
Technologies, released in mid-November.  It is a "semi-concatenative" language
where every operation can fail.

"Semi-concatenative" is supposed to mean that there isn't just the usual
implicit "concatenate" program-composing operator, there's also a second
program-composing operator, "alternate" (notated explicitly by `|`).

This second operator is intended to gracefully handle the case where a
program operation has failed -- which any of them can.

### Lanthorn: `letrec` as syntactic sugar

*   summary: [Lanthorn](https://catseye.tc/node/Lanthorn) demonstrates a `letrec`-removing transformation.
*   date: Sat, 17 Jul 2021 12:53:05 GMT

Lovely language [Lanthorn](https://catseye.tc/node/Lanthorn) launches.

Look lucidly at its lexical lycanthropy — a leakproof lifting
of `letrec` to `let` in lieu of lopsided letterbox loads.

A loquacious lucubration in laminar labour for lugubrious laity?
It's likely!

### Release of Castile version 0.4

*   summary: Version 0.4 of the [Castile](https://catseye.tc/node/Castile) programming language has been released.
*   date: Fri, 02 Jul 2021 09:31:42 GMT

After a long time lying fallow, a new version (0.4) of the programming language
[Castile](https://catseye.tc/node/Castile) has been released.

Mainly, I was disappointed that the C-language-generating backend of the
compiler was left incomplete.  So I completed it.  Testing `struct`s for
equality was also unimplemented in several backends.  So I completed that
part of it too.

The language itself has few changes, primarily the tightening of some rules
regarding comparing `struct`s.

But significantly, the language project has been re-focused.  The language
is not quite as unremarkable as its documentation previously made it sound.
Castile is a simple language with union types.  The union types let it do
a number of tricks, like being safe from null pointers, implementing enums,
and taking a "Parse, don't validate" approach when programming.

### A better experience on mobile, and DAM 0.2

*   summary: Improvements to the [online installations](https://catseye.tc/article/HTML5_Installations.md) on mobile.
*   date: Thu, 10 Dec 2020 10:43:22 GMT

The `catseye.tc` website has never exactly been "mobile-first" in its design.
But we've recently taken some steps so that the experience on mobile is less
bad.  In particular, the [gewgaws](https://catseye.tc/article/Gewgaws.md) are
much more mobile-friendly now.  Many of them scale themselves down properly
to the size of your device's screen.  Others, such as
[A Non-Random Walk](https://catseye.tc/installation/A_Non-Random_Walk)
and
[Art Restoration Simulator](https://catseye.tc/installation/Art_Restoration_Simulator),
now function on mobile, when before they did not.

Incidentally, version 0.2 of [DAM](https://catseye.tc/node/DAM), the
Document *Awesome* Model, has been released.  Range controls now expose a method
to set their value programmatically, and the project has a slightly more developed
build system.

### Version 0.3 of ellsync released

*   summary: Version 0.3 of [ellsync](https://catseye.tc/node/ellsync) has been released.
*   date: Tue, 01 Dec 2020 11:27:11 GMT

[`ellsync`](https://catseye.tc/node/ellsync) is an opinionated poka-yoke for rsync,
for the primary purpose of maintaining a backup system.

Version 0.3 has been released, which, along with some cleanup of the internals,
provides two more measures for quality assurance.

First, after `rsync` has completed, the system's `sync` command is run.  So
`ellsync` does not finish until all of the changes have been written to disk.

Second, a `--thorough` option has been added.  This runs `rsync` in a mode
where it thoroughly checks for differences between files, even if the source
file's timestamp has not changed.  This can detect files which have become
corrupted, and also repair the backup file, if the original file has not been
corrupted as well.

### Version 0.8 of Robin released

*   summary: Version 0.8 of [Robin](https://catseye.tc/node/Robin) has been released.
*   date: Thu, 20 Aug 2020 10:13:35 GMT

A new version of Cat's Eye Technologies' excessively principled
Scheme-like programming language [Robin](https://catseye.tc/node/Robin)
has been released.

This is a fairly major release for Robin, as there is a change of
terminology: what were previously called "macros" are now called
by the more obscure, but more accurate term "fexprs".

In Robin, both macros and functions are defined in terms of fexprs.

Fexprs also no longer get passed a `self` argument; instead, to
achieve recursion, a recursive fexpr must be written.  This is
analogous to a recursive function.

The Robin Tutorial has also been significantly fleshed out.  It
aims to be a good overview of the language for programmers who
are already somewhat familiar with Lisp or Scheme.

### Tandem, an experimental rewriting language

*   summary: [Tandem](https://catseye.tc/node/Tandem), an experimental rewriting language, has been released.
*   date: Thu, 09 Jul 2020 15:37:23 GMT

We've designed and released the first version of [Tandem](https://catseye.tc/node/Tandem),
an experimental rewriting language where the rewrite rules form a
[Kleene algebra](https://en.wikipedia.org/wiki/Kleene_algebra).
The object being rewritten by a Tandem program is a collection of labelled stacks — a finite mapping
from strings to strings. The strings are always rewritten at the left edge, so they are effectively stacks.

Writing finite automata, push-down automata, Turing machines, and other automata is quite natural in Tandem,
because transition rules such as "In state 4, if the next character in the input is `g`, consume it and
push `$` onto the stack and go to state 9" translate quite straightforwardly to rewrite rules such as

    Q4 → 9 & Ig… → … & K… → $…

### tagfarm, an ultra-lightweight categorization system for arbitrary files

*   summary: [tagfarm](https://catseye.tc/node/tagfarm), an ultra-lightweight categorization system for arbitrary files, has been released.
*   date: Wed, 29 Apr 2020 14:45:46 GMT

We've designed an ultra-lightweight system for categorizing arbitrary files in
a filesystem and christened it [`tagfarm`](https://catseye.tc/node/tagfarm).

`tagfarm` associates each file in a file tree with zero or more tags. Each tag
is implemented as a directory containing symbolic links to the files that
have that tag. And that, along with a little script to add, remove, and
repair tags after the files themselves may have moved, is basically all it
is - hence "ultra-lightweight".

### Web-based interpreters for Emmental and Mascarpone

*   summary: Web-based interpreters for [Emmental](https://catseye.tc/installation/Emmental) and [Mascarpone](https://catseye.tc/installation/Mascarpone).
*   date: Mon, 06 Apr 2020 13:08:48 GMT

We've made new minor releases of our self-modifying programming languages
[Emmental](https://catseye.tc/node/Emmental) and
[Mascarpone](https://catseye.tc/node/Mascarpone).

We've modernized the build systems in both of these language distributions,
and in the process we've enabled web-based interpreters to be built
for these languages, by compiling their Haskell reference implementations
to JavaScript using the Haste compiler.

And we've put those web-based interpreters online at catseye.tc,
[here (Emmental)](https://catseye.tc/installation/Emmental) and
[here (Mascarpone)](https://catseye.tc/installation/Mascarpone).

We've also placed the contents of the Mascarpone distribution in the
public domain, to match the Emmental distribution.

### Version 0.7 of Robin released

*   summary: Version 0.7 of [Robin](https://catseye.tc/node/Robin) released.
*   date: Wed, 25 Mar 2020 10:22:26 GMT

A new version of Cat's Eye Technologies' "excessively principled"
Scheme-like programming language [Robin](https://catseye.tc/node/Robin)
has been released.

The highlight of this release is that it is now allowed to define a
symbol after it has already been defined, which is understood as providing
multiple semantically equivalent definitions for the symbol.  An
implementation of Robin is allowed to (but not required to) try to disprove
that the given definitions are semantically equivalent, and indeed the
reference implementation has a way to run property tests (written using
QuickCheck) on all such multiple definitions, trying to find cases where
their behaviours differ.

### Version 0.6 of Robin released

*   summary: Version 0.6 of [Robin](https://catseye.tc/node/Robin) released.
*   date: Mon, 02 Mar 2020 09:12:04 GMT

A new version of Cat's Eye Technologies' "excessively principled"
Scheme-like programming language [Robin](https://catseye.tc/node/Robin)
has been released.

The highlight of this release is that exceptions and exception handlers
have been removed from the language.  Conventional exception handlers
are in essence dynamically scoped, and thus break referential transparency,
while lexical exception handlers have limited usefulness.  Exceptions
have therefore been replaced by "abort values", which are the wrong
type for almost all operations, and in this manner bubble up to the top
level of evaluation just as an exception would.  Referential transparency
has thus been restored to the language.

### Falderal, Feedmark, NaNoGenMo 2019, and Cosmos Boulders

*   summary: [Falderal](https://catseye.tc/node/Falderal), [Feedmark](https://catseye.tc/node/Feedmark), [NaNoGenMo 2019](https://catseye.tc/node/NaNoGenMo%202019) and [Cosmos Boulders](https://catseye.tc/node/Cosmos%20Boulders).
*   date: Wed, 08 Jan 2020 23:30:18 GMT

Tying up some loose ends of 2019 before we move on to 2020.

Firstly, our Markdown-based formats [Falderal](https://catseye.tc/node/Falderal)
and [Feedmark](https://catseye.tc/node/Feedmark) had some new minor releases.

But more importantly, their Python implementations are now available
as Python packages: [Falderal on PyPI](https://pypi.org/project/Falderal/) and
[Feedmark on PyPI](https://pypi.org/project/Feedmark/).

But wait, that's not all!  They're also available as Docker images on Docker Hub:
[catseye/falderal](https://hub.docker.com/r/catseye/falderal) and
[catseye/feedmark](https://hub.docker.com/r/catseye/feedmark).

Secondly, at the tail end of 2019 Cat's Eye Technologies participated in [NaNoGenMo 2019](https://catseye.tc/node/NaNoGenMo%202019)
(we just can't seem to stay away from it) resulting in three generated novels:
[Anne of Green Garbles](https://catseye.tc/node/Anne%20of%20Green%20Garbles),
[The Insidiously Rainbow-Wigged Dr. Fu-Manchu](https://catseye.tc/node/The%20Insidiously%20Rainbow-Wigged%20Dr.%20Fu-Manchu), and
[The Epic of Goog-a-MESH](https://catseye.tc/node/The%20Epic%20of%20Goog-a-MESH).

During the first of those novels arose the somewhat surprising (to me) result that
the intersection of a Markov chain and a regular grammar is another
Markov chain — one which obeys the rules of the regular grammar.
You can read all about it in [this write-up](https://catseye.tc/view/NaNoGenMo-Entries-2019/Anne%20of%20Green%20Garbles/README.md),
which includes some snazzy state transition diagrams as well.

Finally, [Cosmos Boulders](https://catseye.tc/node/Cosmos%20Boulders) is an arcade-style
game written in JavaScript using reducers and immutable data structures.  It's not
particularly original, but it's written in a purely function style.  We hope to
write a second version using [Nested Modal Transducers](https://github.com/catseye/Nested-Modal-Transducers)
for comparison.

### Our third esolang of 2019: Oxcart

*   summary: Our third esolang of 2019: [Oxcart](https://catseye.tc/node/Oxcart).
*   date: Tue, 05 Nov 2019 12:32:01 GMT

Back in February, when we announced [Wanda](https://catseye.tc/node/Wanda),
we did say there would be other esolangs this year.
They haven't been the ones I thought they'd be, back then,
but they're pretty squarely esolangs, I think.  And this is the third one!

We present [Oxcart](https://catseye.tc/node/Oxcart), a purely concatenative
language (in the sense of [Equipage](https://catseye.tc/node/Equipage))
which is based on composing functions written in continuation-passing style.
Instead of functions which take states to states, the symbols of the language
represent functions which take an extra argument, a continuation, that
represents the future of the computation.

It's also installed online, so you can
[run Oxcart programs without leaving your web browser](https://catseye.tc/installation/Oxcart).

### Carriage, Erratic Turtle Graphics, and DAM

*   summary: [Carriage](https://catseye.tc/installation/Carriage) finally gets a reference distribution; also [Erratic Turtle Graphics](https://catseye.tc/installation/Erratic_Turtle_Graphics) installed online.
*   date: Thu, 17 Oct 2019 11:44:00 GMT

Since 2012, our first "purely concatenative" language,
[Carriage](https://catseye.tc/node/Carriage), existed only in the form of
[an article on the esowiki](https://esolangs.org/wiki/Carriage).

It now has a real reference distribution, and it's also installed
online, alongside its successors [Equipage](https://catseye.tc/installation/Equipage)
and [Wagon](https://catseye.tc/installation/Wagon), so you can
[run Carriage programs without leaving your web browser](https://catseye.tc/installation/Carriage).

Elsewhere, we've also installed a gewgaw we concocted a little
while ago (though not as long ago as Carriage), which we call
[Erratic Turtle Graphics](https://catseye.tc/installation/Erratic_Turtle_Graphics).

It's possibly also worth mentioning that this gewgaws, and several other of
our recent online installations, use a tiny Javascript library that we released
this year, called [DAM](https://catseye.tc/node/DAM), to build their user interfaces.
It replaces [yoob.js](https://catseye.tc/node/yoob.js)'s "element factory" library,
and it's what we're switching to as we phase out yoob.js.

### PL-{GOTO}, Robin, Equipage, and Wagon installations

*   summary: [PL-{GOTO}](https://catseye.tc/installation/PL-%7BGOTO%7D), [Robin](https://catseye.tc/installation/Robin), [Equipage](https://catseye.tc/installation/Equipage), and [Wagon](https://catseye.tc/installation/Wagon) installed online.
*   date: Mon, 07 Oct 2019 09:09:45 GMT

As we mentioned in a previous news item, the [Haste](https://haste-lang.org/)
compiler allows us to easily create [web-based installations](https://catseye.tc/article/HTML5_Installations)
for things implemented in [Haskell](https://catseye.tc/node/Haskell).

And some things we've had a penchant for implementing in Haskell
are programming languages of all stripes — experimental, esoteric, and
didactic.

So, four more programming languages have come online; you can write
programs in them and run them right in your web browser.  It isn't a fantastic
development environment, of course, but you can get a taste for what the
language is like, without having to download or install anything.

Thus we present online installations for four languages we implemented in Haskell:

*   **[PL-{GOTO}](https://catseye.tc/installation/PL-%7BGOTO%7D)**, a
    pedagogical language from Brainerd and Landweber's textbook
    _Theory of Computation_ (1974; ISBN 0471095850), in which it is possible
    to express only computations which are primitive recursive;
*   **[Robin](https://catseye.tc/installation/Robin)**, an
    "excessively principled" functional programming language influenced
    by Scheme and PicoLisp;
*   **[Equipage](https://catseye.tc/installation/Equipage)**, a
    "purely concatenative" esolang; and
*   **[Wagon](https://catseye.tc/installation/Wagon)**, our latest esolang,
    which is also our latest variation on the theme of "purely concatenative".

### Our second esolang of 2019: Wagon

*   summary: Our second esolang of 2019: [Wagon](https://catseye.tc/node/Wagon).
*   date: Wed, 04 Sep 2019 14:44:11 GMT

Back in February, we did say there would be other esolangs this year,
so here we go with the second one!

We present [Wagon](https://catseye.tc/node/Wagon), a purely concatenative
language (in the sense of [Equipage](https://catseye.tc/node/Equipage))
which is "second-order concatenative": instead of functions which take states to states,
the symbols of the language represent functions which take functions from states
to states, to functions that take states to states.

Also, we have recently made a few updates to our probably-not-esoteric
but-not-exactly-mainstream-either language [Robin](https://catseye.tc/node/Robin),
bringing it up to 0.4.  Mainly this involved cleaning up its specification.

### Quylthulg, Pail, Flobnar, and Maze Clouds installations

*   summary: [Quylthulg](https://catseye.tc/installation/Quylthulg), [Pail](https://catseye.tc/installation/Pail), [Flobnar](https://catseye.tc/installation/Flobnar), and [Maze Clouds](https://catseye.tc/installation/Maze_Clouds) installations updated.
*   date: Wed, 08 May 2019 09:32:19 GMT

Lots more updates to installations.

First, we have discovered that it is possible to use the [Haste](https://haste-lang.org/)
compiler to create [web-based installations](https://catseye.tc/article/HTML5_Installations)
for little things we have implemented in [Haskell](https://catseye.tc/node/Haskell),
by adding only a small module to hook up the internals to some HTML5 controls.

Thus we present online installations for three languages we implemented in Haskell:
**[Quylthulg](https://catseye.tc/installation/Quylthulg)** (where goto's is allowed, but
only inside data structures), **[Pail](https://catseye.tc/installation/Pail)**
(if Lisp stands for LISt Processing, Pail stands for PAIr Language), and
**[Flobnar](https://catseye.tc/installation/Flobnar)** (where
[Befunge](https://catseye.tc/node/Befunge) went drinking on its 18th birthday and
got really quite remarkably drunk).

Since we developed a little system for doing these with Haste, we can expect a few other
of Cat's Eye Technologies Haskell implementations to have online interpreters in
the near future.

Second, we finally put together a distribution for [Maze Clouds](https://catseye.tc/node/Maze_Clouds)
(a simple generative technique to generate mazy, cloudy forms) containing implementations
in both Python and Javascript, and we put the Javascript one online here:
**[Maze Clouds](https://catseye.tc/installation/Maze_Clouds)**

### SixtyPical 0.19 released

*   summary: Version 0.19 of [SixtyPical](https://catseye.tc/node/SixtyPical) has been released.
*   date: Tue, 16 Apr 2019 12:21:59 GMT

Sometimes you go down a rabbit hole because it opens up under your feet.  That's
what it felt like this time, anyway; I hadn't thought about
[SixtyPical](https://catseye.tc/node/SixtyPical) for months, and then suddenly
I find myself rewriting half of the compiler's internals.

The big thing, I guess, is that I realized the language doesn't need separate
`buffer` and `table` types; only let tables have more than 256 entries, but
say only the first 256 can be accessed by index; and let `pointer`s point into
tables, and say that is how you access entries past the 256th.  Then you can
just get rid of `buffer` completely.  Which is what I did.

And then it because fairly obvious that "which table is this pointer pointing
into?" could be tracked in the analysis context just like all the other things
we're tracking, and after some consideration I decided a lexically-scoped
block for it would be nice, and so the language now has `point ... into` blocks.

Doing these introduced or revealed a bug whose root cause seemed to simply be
that hand-rolling immutable objects in Python (or rather, objects that you
would like to consistently pretend are immutable) is a pain in the neck.
Addressing that problem triggered another wave of changes, wherein the internal
representation of type information was refactored into a single context
(the symbol table) shared amongst the phases of the compiler, in which `namedtuple`s
are stored.  It was a lot of refactoring, but the massive test suite helped
keep things together, and it was quite satisfying being able to delete the
`__hash__` methods from objects, knowing they would now be given appropriate
ones under the hood.  And that fixed the bug.

Finally, I thought the `loadngo.sh` script was getting a bit grotty, so I
incorporated the "load-and-go" mechanism into the main `sixtypical` script itself.

### Cyclobots, Chzrxl, Wanda, Velo, and ILLGOL installations

*   summary: [Cyclobots](https://catseye.tc/installation/Cyclobots), [Chzrxl](https://catseye.tc/installation/Chzrxl), [Wanda](https://catseye.tc/installation/Wanda), [Velo](https://catseye.tc/installation/Velo), and [ILLGOL](https://catseye.tc/installation/ILLGOL) installations updated.
*   date: Mon, 11 Mar 2019 11:51:31 GMT

Lots of updates to installations.

First, our little dynamical systems [Cyclobots](https://catseye.tc/node/Cyclobots)
and [Chzrxl](https://catseye.tc/node/Chzrxl) have had their implementations
re-fitted to use [PixiJS](http://pixijs.com/).  PixiJS uses WebGL for display
when it is available, so these installations now have the potential for having much nicer
visuals than the previous versions.  It's only minimally leveraged at this point —
you can select "Blurred" or "Noisy" visuals — but the potential is there, I tell you.

In the process of switching over to PixiJS, these two projects have
been given their own reference distributions instead of residing in the
[HTML5-Gewgaws distribution](https://catseye.tc/distributions/HTML5-Gewgaws%20distribution)
alongside everything else.

You can see these in action here:
**[Cyclobots](https://catseye.tc/installation/Cyclobots)** and
**[Chzrxl](https://catseye.tc/installation/Chzrxl)**.

Second, two of our languages that are implemented in [Lua](http://catseye.tc/node/Lua),
namely [Wanda](https://catseye.tc/node/Wanda) and [Velo](https://catseye.tc/node/Velo),
have been made to run on a web page thanks to
[Fengari](https://fengari.io/), an implementation of the Lua VM in Javascript.

So, you can try these out online here:
**[Wanda](https://catseye.tc/installation/Wanda)** and
**[Velo](https://catseye.tc/installation/Velo)**.

Finally, a distribution of [ILLGOL](https://catseye.tc/node/ILLGOL) running under
[FreeDOS](https://catseye.tc/node/FreeDOS) is now installed online,
under [v86](https://catseye.tc/node/v86), an emulator for IBM-compatible PC architecture
in Javascript.  (We actually built this distribution a while ago, but at the time,
v86 wasn't able to run it correctly.  Now it is.  Kudos to all v86 contributors.)

You can try it out online here:
**[ILLGOL](https://catseye.tc/installation/ILLGOL)**.

### Our first esolang of 2019: Wanda

*   summary: Our first esolang of 2019: [Wanda](https://catseye.tc/node/Wanda).
*   date: Wed, 27 Feb 2019 11:52:33 GMT

We present [Wanda](https://catseye.tc/node/Wanda), a Forth-like, "concatenative"
programming language that's arguably not concatenative at all, nor even "stack-based",
because it's based on a string-rewriting semantics.

Wanda was actually started in 2009, but never really got off the ground.  But it
never really went away, either, so here we are, ten years later.

Ah, also, are you slightly surprised, or even alarmed, to hear that this is only our
*first* esolang of 2019?  It's true, there will be others this year (weather permitting).
But you'll have to wait for those.

### git.catseye.tc and other website improvements

*   summary: [git.catseye.tc](https://git.catseye.tc/) and other website improvements.
*   date: Thu, 31 Jan 2019 12:25:47 GMT

As you might know, Cat's Eye Technologies hosts git repositories of its projects on
[GitHub](https://github.com/).  And as you might also know, several months back,
GitHub was acquired by [Microsoft](https://microsoft.com/).

We do not regard this, in itself, to be a problem.  There's nothing GitHub-specific
about git; it's a distributed protocol, and a git repository can be hosted basically
anywhere.  The GitHub-specific things that GitHub does offer are handy, but we've
intentionally avoided relying too much on them.  For instance, we've tried to describe
planned features in TODO lists in the repo itself, instead of opening issues for
them.  And shall we point out that Microsoft is only one of several 800lb gorillas
in the tech world these days, and perhaps it's not the one you should be the most
worried about anymore?

Ah, but I'm editorializing.  The point is, one *can* lessen one's dependency on GitHub
very easily by hosting one's git repositories elsewhere, and that's just what we've done.
Deploying an instance of [klaus](https://github.com/jonashaag/klaus), we've set up
**[git.catseye.tc](https://git.catseye.tc/)**.  You can browse
repositories from it and clone from it and download zipfiles from it and everything.
(The repositories we have on GitHub will stay on GitHub, too, so if you want to fork
them on there or open issues or pull requests there, you can, still.)

We've also done a fair bit of maintenance on the catseye.tc website in conjunction with this.

First — many would say this is long overdue — it's all `https` now.  Don't worry about
changing any links; it's not required, `http` requests will simply redirect to `https`.

Second, we've released version 0.8 of [Feedmark](https://catseye.tc/node/Feedmark), and
the website is using it in the backend to read Markdown files directly as Feedmark.
This lets us do things like format it more nicely in templates.

Lastly, we've cleaned up the [Retrocomputing](http://catseye.tc/article/Retrocomputing)
article, in particular, moving the things that are dependencies (even if they are
"retro dependencies") rather than projects to the
[Project Dependencies](https://catseye.tc/article/Project_Dependencies) article.

### SixtyPical 0.18 released

*   summary: Version 0.18 of [SixtyPical](https://catseye.tc/node/SixtyPical) has been released.
*   date: Fri, 04 Jan 2019 11:27:41 GMT

We've released the latest version of [SixtyPical](https://catseye.tc/node/SixtyPical),
our low-level 6502-like language with abstract analysis.  In particular, how blocks
are analyzed has been cleaned up.  When two block diverge (such as in an `if` statement),
they no longer need to keep the same values initialized; instead, the two contexts
are merged afterwards — any location that is trashed in one block will continue to be
trashed after both blocks.  (And if that introduces a problem after both blocks, the
analyzer will catch that problem there.)  Also, a `goto` may appear at the end of any
reasonable block, not solely at the end of a routine, so long as the initialization
constraints all work out as declared.  (The context at the `goto` must be compatible
with the context at the end of the routine.)

Our hope is that these changes will pave the way for optimizations such as tail calls
and dead code removal.

- - - -

_Older news items from this feed, dating back to 2007, can be found in the_
**[Archived News Items](http://catseye.tc/article/Archived_News_Items)**
_article._
