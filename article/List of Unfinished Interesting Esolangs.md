List of Unfinished Interesting Esolangs
=======================================

*   summary: A list of "open problems" in esoteric programming language design
*   common auspices: Cat's Eye Technologies
*   common authors: Chris Pressey
*   common development-stage: idea
*   common no-specification: true
*   common type: Programming Language
*   image_url: https://static.catseye.tc/images/illustrations/Perpetual_Motion_Machine.jpg

Here are some designs for [esoteric programming languages][]
that I've worked on, but which have turned out to be a bit resistant to
joining the ranks of [the completed][].  You
could describe them as "open problems" in esolang design — but that would
suggest that the completed designs would be "solutions" to something.  (Ha!)

I've disseminated what little I have for these designs here because it looks
unlikely that I'll have the time and resources to complete them in the near
future, and I am a gracious individual who wouldn't want to hoard these
potentially beautiful things.

If you would like to continue the work on any of these designs, feel free.
Of course, if you do manage to complete something based on one of them,
I would appreciate being given some credit (since you are a gracious
individual as well, right?)

### AINSNIA

*   acronym-for: AINSNIA Is Not SETL, Nor Is AINSNIA
*   genre: Esolang
*   paradigms: Functional
*   summary: fundamentally based on sets

When I first heard of [SETL][], the "SET Language",
I was intrigued, but when I looked into it, I found it just wasn't
based on sets fundamentally enough for my taste.

AINSNIA would be the remedy for that.  In AINSNIA,
functions take sets, return sets, and are built up *from* sets.
The key idea to achieve this is encode ordered pairs (_a_,_b_) as
Kuratowski pairs {{_a_}, {_a_,_b_}}.

This could probably be put into a [Scheme][]-like framework. Instead of
(ordered) s-expressions, you have (unordered) set-expressions. So
instead of `(list 1 2 3)` you have `(set 1 2 3)`. But actually this
should be at the lowest level, so that `(quote (1 2 3))` is a set. You would
do the Kuratowski thing to encode order, but you'd have to do it
**everywhere**, which would get, wow.

On the other hand, `map` and friends stay mostly the same, they just
work on sets now.

### Belabour

*   genre: Esolang
*   paradigms: 2-dimensional, Logic programming
*   summary: 'relative entropy meets Prolog: a crossword logic game'
*   inception-date: ca 2006

While in Vancouver, I came across a copy of that classic book on Information
Theory, _The Mathematical Theory of Communication_
(Claude Shannon and Warren Weaver, University of Illinois Press, 1969),
and found this quoted on page 14:

> "...[I]t is interesting to note that a language must have at least 50 per cent of real freedom (or relative entropy)
> in the choice of letters if one is to be able to construct satisfactory crossword puzzles.  If it has complete
> reedom, then every array of letters is a crossword puzzle.  If it has only 20 per cent of freedom, then
> it would be impossible to construct crossword puzzles in such complexity and number as would make the
> game popular.  Shannon has estimated that if the English language had only about 30 per cent redundancy,
> then it would be possible to construct three-dimensional crossword puzzles."
> — Warren Weaver, _Recent Contributions to the Mathematical Theory of Communication_

So let us consider another puzzle game based on another language.  The language is not so strange;
take Prolog's semantics
and cast them in Forth's syntax (Reverse Polish Notation — RPN.)  That includes identifiers —
to construct the atom `cat` you might say `ca.t.`, or equally well, `tca..`.  To express a Horn clause like
`gp(X,Y) :- p(X,Z), p(Z,Y)`, you might say `XY,gp.*ZY,p*XZ,p*&:`, or
any of a number of other valid permutations.

Now, let us say that that clause need not only be read left to right, but, like a crossword puzzle entry,
could be read top to bottom.  And that a set of such clauses shall be cast into a grid, with the rows and
columns *both* being clauses in the logic program, even though they are overlapping.
And, just to keep it feasible, we provide in the language a symbol `#` which does nothing
except waste space.

So, here is the game: I give you a logic puzzle, hopefully of some moderate "interestingness", like that
old chestnut about the farmer with his goose and his fox who's trying to smuggle them onto a boat into Eurozone,
or get them to market, or something.  You give me a _n_×_n_ square
grid of symbols which contains a Belabour program which solves this
puzzle.  You get points for making _n_ small; you have points deducted for using `#`.

What would this game tell us about the percent of relative entropy in logic?  If nothing
so profound could learned about "pure logic", per se, then what about Horn-clause-based
logic programming — and is that not still an interesting question?

### Boo-yah!

*   genre: Esolang
*   paradigms: 2-dimensional
*   summary: overlapping instructions in 2 dimensions
*   inception-date: ca 1998

This thing's terminally undesigned.  I started thinking about
it in the late nineties — possibly as early as 1998 — in Winnipeg.

The challenge is to design a 2-dimensional language similar to [Befunge-93][],
except where each instruction is is composed, not of a single symbol, but of a 2×2 square of
symbols.  As in Befunge, the IP should move at a rate of one cell per tick, and that
means that each executed instruction must in general share two symbols with the
previously executed instruction.  In other words, in *Boo*-yah!,
instructions *overlap*.

Symbols are drawn from the alphabet {`/`, `\`}.  This two-symbol alphabet
gives us 2^4 = 16 possible instructions.  4 of these instructions
would be used to direct the flow of the IP like Befunge's `><^v`:

    \\  //  /\  \/
    //  \\  /\  \/

That leaves 12 instructions to manipulate the state.

One of the reasons that this has gone undesigned for so long is the difficulty in selecting
a sufficiently "sweet" combination of instructions: one which will allow the instructions to be
overlapped, while also having the instructions manipulate the state of the program in
useful and interesting and non-trivial ways.

It would be very tempting to just riff on [brainfuck][] and have a tape,
instructions that increment and decrement the current cell on that tape,
and instructions that move back and forth on the tape.  But I think that's a bit boring.
Ideally, each instruction would affect *several* different bits of state
in the runtime model simultaneously, and it should be possible to come up with
a series of instructions in which most, but not all, of those state changes
have been cancelled out, leaving only the desired change in state.  Since this
cancellation approach would naturally dovetail with overlapping, it would be a
good fit for the language.

### Faradaisical

*   genre: Joke language
*   paradigms: Self-modifying
*   summary: programmagnetic induction
*   inception-date: ca 2009

Execution of instructions in one program creates a "programmagnetic field" which induces the execution of instructions
in another nearby program.

Now, I think that's a pretty good joke language, as is.  But it could maybe even be developed into something usable.
Of course, it would ideally adhere to as many of the rules of electromagnetic induction as possible — cross product of
the flux, and all that jazz.  Being able to
wind a program around into a coil whose inductance can be measured in Turinghenries would be a bonus!  (Would it
add ringing to a computation of the Ackermann function...?)

### GI

*   genre: Esolang
*   paradigms: Graph-rewriting
*   summary: execution entails solving instances of GI
*   inception-date: ca 2010

So we have a set of instructions, say two dozen or so.  So far, so good, right?

Each of the instructions is identified by an undirected, unlabeled graph.  The program is a sequence
of undirected graphs.  Each graph in the program is, in sequence, matched up with the
instruction whose graph is isomorphic, and that instruction is executed.

The result of this is that recognizing each instruction requires solving an instance of the
<a href="http://en.wikipedia.org/wiki/Graph_isomorphism_problem" class="external">graph isomorphism problem</a>.
This is an interesting problem, because (last I checked) no one knows whether this problem
can be solved in polynomial time, nor whether it is NP-complete, so it has been given its own
complexity class, **GI**.  The idea here is that the complexity of programs in the GI
language needs to be expressed in terms of the **GI** complexity class.

But there is a small problem with this design; namely, if all the graphs in the program
are statically defined, an optimizing implementation could statically analyze the program,
find matching instructions for each graph in the program beforehand, and cache them.  This
would diminish the complexity of running the program to a finite number of instances of **GI**,
plus whatever the "usual" complexity of the program is.

To defeat that, we can basically force the graphs in the program to be dynamically
defined: some subset of the instructions allows constructing a new graph (by creating an
empty graph in some kind of "graph accumulator", adding nodes and edges, etc);
newly assembled graphs can be executed via some kind of "eval" instruction; and
newly assembled graphs *must* be executed, in a "quining" fashion,
in order to enact repetition, a la [Muriel][].

Since new graphs would then be continually being generated, perhaps in
chaotic and undecidable ways, the ability of an implementation to recognize and
cache them would be severely limited, meaning that the complexity of a GI program
really would need to be effectively measured in terms of **GI**.  For extra fun, some
instruction could re-define the graphs which identify the instructions; while this
certainly doesn't make it any easier to optimize a GI program, I don't think it's
a strictly necessary step to defeat caching.

(Oh, and each of the undirected, unlabeled graphs which represents an instruction
could be termed a "dogtag".  Get it?  Get it?  **GI**, get it?)

Note, however, that there are some problems with any "quining" language
which requires multiple instructions to quine a single instruction.  That
should be obvious if you think about it, but it didn't occur to me until
now.  I'll think about this a bit more.  See also Expload.

### Kig

*   genre: Esolang
*   paradigms: 2-dimensional
*   summary: five points collapse and expand
*   inception-date: ca 2006

Kig was an idea I had while living in Vancouver
for an automaton based on a 2-dimensional, orthogonal, integral, Cartesian grid
containing only a set of five points.  The set of points would shrink until it could
shrink no more, at which point it would explode, and begin to shrink again.
The execution would be considered terminated once the pattern reached
an obvious fixed point, i.e. when the points would cluster in the exact
same way repeatedly before exploding.

The shrinking occured in the following manner.  On each tick,
pick the northwesternmost midpoint of two of the points, and call it
the target.  (There is a
[cute pigeonhole proof](http://www.cut-the-knot.org/pigeonhole/grid_mid.shtml)
that, for 5 points with integral
coordinates, such a midpoint with integral coordinates will always exist.)
If the target is occupied by one other of the five points, stop — it's time to
explode.  Otherwise, move the furthest, northwesternmost point to
the target, and repeat.  Since there are still 5 points with integral
coordinates, the midpoint property is preserved and the operation can be
repeated as necessary.  We can also prove, fairly straightforwardly,
that this shrinking procedure always terminates, i.e. always reaches
the "it's time to explode" state.  (The "furthest, northwesternmost"
condition is just to disambiguate, in the case that there are more than
two points that have a midpoint.)

Unfortunately, although I'm sure I had something in mind while I was
riding the 99 B-Line home once, I can't for the life of me remember now
how the explode phase was supposed to work.  Whatever it was, it
would need to position the points far apart, based on their last
shrink-phase configuration, in order to be interesting.  Extremely far
apart, like exponentially so, would be best.  Even then, it's
not clear if it would be possible to make this system [Turing-complete][].
With 5 points, you do have 10 unbounded counters at your disposal —
although your only real operation in the shrink-phase is something
akin to division by two...

### Milab

*   genre: Esolang
*   paradigms: Meta-circular
*   summary: memory mapped, but where?
*   inception-date: ca Sep 2009

In the vein of [ZOWIE][], some operation critical to [Turing-complete][]ness,
like control flow, is memory-mapped.  The twist is, you don't know where.  It could be any memory location
(out of an unlimited number), so you have to discover it in order to use it and write an arbitrary program.

The most obvious way to discover this memory location would be through systematic probing,
much like you might probe for bad RAM.
Such probing, however, would seem to necessitate a loop and a test of some kind,
and with such operations available, chances are the language is already Turing-complete,
or at least so darn close as to not be very interesting.

So the trick to making this a good design would be figuring out what to hide, and what to provide to
find it without making it unnecessary.

### Naoko

*   genre: Experimental language
*   paradigms: Meta-circular
*   summary: everything is explicit
*   inception-date: ca Sep 2008

While living in Hyde Park in Chicago, I had the idea to design a
high-level programming language where everything is explicit.
If you are reading that and thinking "how absurd", congratulations, your brain works!
Every string of symbols has multiple possible interpretations, so there will always be some
semantic function  providing the interpretation; that function must either be implicit, or must be
described in terms of some other system — i.e. some other strings of symbols —
which suffers the exact same problem.  So, if you try to make *everything* explicit, the best
you can really do is make it circularly defined.

But still, it could be an interesting line of inquiry, if we tack onto "everything is explicit"
a disclaimer like "insofar as this is possible," and pick a few especially significant things to make
explcit.  It could be interesting because, in programming, explicit phenomena
are manageable phenomena — this is why I picked the name Naoko, which means
"obedient child" in Japanese.  It is also interesting because we are having it be a high-level
language, and one of the hallmarks of being "high-level" is that many things are taken care
of for the programmer, i.e. *not* explicit.

For Naoko, I planned to start with a simple eager functional language, similar to
Scheme or Haskell (except eager), and aimed to make at least the following three things explicit:

*   *Lexical environments for variable binding.*
    
    This was to be done by annotating every variable name with the environment it
    comes from.  Since environment are lexically nested, the variable `foo`
    in the immediate enclosing environment would be referred to by `foo^0`,
    the one from the next level up `foo^1`, and so forth.

*   *Control flow.*
            
    This was to be made explicit by continuations; functions could never return, but would
    be forced to continue a continuation as their final act.  In addition, there could be no
    "call-with-current-continuation"-like construct, as the "current continuation" is naturally
    a somewhat implicit object.  These two things would force the entire program to be
    written in a very verbose continuation-passing style.

*   *Memory management.*
            
    The plan was to add explicit allocation and deallocation operations.
    Explicit allocation does not add much except for, every time you create a list or
    closure you should put `new` in front of it.  It's deallocation
    where it gets interesting.  At the last use of a datum, you would need to mark it
    `free`, and if you make copies of it to pass to functions, you
    would need to explicitly mark them `copy`.  There's kind of
    a simplistic syntactic linear typing thing going on.

As if each of these wasn't bad enough alone, their combination and
interaction brings up a couple of further issues.  I never addressed them fully,
but similar ideas with similar interaction eventually materialized in my
programming language [Unlikely][].

### Orbital

*   genre: Experimental language
*   paradigms: ??
*   summary: message queues are just queues
*   inception-date: ca Dec 2012

[Erlang][]'s message-passing paradigm is a good one, but then sometimes
I look around on Github and I see Erlang libraries for managing process
pooling and stuff and I think, wait, Erlang supposedly so awesome for
distributed computing, why isn't this a solved problem?

And this leads me to try to deconstruct what "message passing" actually
is.  Processes can send messages to other processes.  When a process
receives a message, it goes into its inbox until the process can deal
with it.

The inbox is a message queue.  And a message queue is a queue.

When I send a message, I don't really care who receives it as much as
I care that the right thing happens in response to it.

So why not just have queues?  If a queue is only every dequeued by a
single process, fine, that's Erlang's model.  But a queue could be
dequeued by multiple processes.  If the processes are stateless with
respect to the queue, then there you have worker pooling right out of
the box.

If this sounds similar to capabilities and/or Linda, it may well be.
The problem of knowing "who to send a message to" is replaced by the
problem of knowing "which queue to enqueue a message onto".

Of course, doing concurrency in languages which don't use Erlang's
message-passing model, like say [Java][], requires that you build and
use queues explicitly.  But that's something of a degenerate case.  A
programming language which supports queues natively, like Erlang
supports processes, would provide them as an *abstraction*, and they
might not even be implemented as queues internally.

For example, you might have some functionality where you don't really
care if it's done in-process or in another process.  In that case,
enqueuing a message may really not queue anything; it might cause
a function to be immediately called on the message.  In this way,
message-passing (or more accurately, queue-filling) could be used as
a single, unifying abstraction for modularizing processing, unlike say
Erlang's separate functions and processes.

### Paneer

*   genre: Experimental language
*   paradigms: Meta-circular
*   summary: comprehensive compositional language system
*   inception-date: ca 2008

A self-modifying programming language which is "input-universal".
That is, a programming language which can transform itself
in a way similar to how [Mascarpone][] transforms itself,
but which also makes the guarantee that it can "turn itself
into any other language," meaning that after a finite
number of prefix symbols from the input program have been
interpreted, the remaining symbols can be interpreted as
a program in any other [Turing-complete][] programming language.

(Given a reasonable input alphabet, I suppose, and
ignoring tedious and trivial details of encoding.)

This is a matroiska language, because the input can be
divided into distinct languages.  But it's possibly the
most flexible possible matroiska language.

I'm not 100% certain that Mascarpone doesn't already qualify.

One part of this process — say, turning Mascarpone into
Pascal — would be turning every symbol into a little state
machine that scans and parses itself (when encountered in
keyword context, or adds itself to a string constant if
encountered between quotes.)

### Poerhinekh

*   genre: Esolang
*   paradigms: 2-dimensional
*   summary: rectangles within rectangles
*   inception-date: 2009

Imagine a nominally graphical programming language, where the only
program element is the lowly rectangle.  A program consists of an
arrangement of rectangles; they may not overlap, but they may be nested
inside other rectangles, and in this case they may butt up against the
containing rectangle, so that they share a side.  Size of a rectangle
does not matter, not even relative size, except insofar as to permit
or disallow nesting.

When a rectangle is nested within a larger containing
rectangle, it can share 0, 1, 2, or 3 sides with the containing
rectangle.  (For 3 sides, we consider the larger of the two
inner areas to be the nested rectangle.)  When 0 sides are shared,
there are no variations — position of the nested rectangle is
immaterial.  When 1 side or 3 sides are shared, there are
four variations (top, left, right, bottom).  When 2 sides are shared,
there are four other variations (top-left, top-right, bottom-left,
bottom-right).  All in all there are 4+4+4+1=13 possibilities for
nesting.  This could map to 13 different instructions or program
forms.  In addition, the nesting is a natural hierarchical pattern
for program formation, so could represent block structure or
precedence or such.

### Potro

*   genre: Esolang
*   paradigms: Algebraic
*   summary: programs form a ring
*   inception-date: ca 2007

Since finishing the first design for [Burro][], I've been interested in
languages where the set of all programs in the language forms an abstract algebraic structure (over a semantic
equivalence relation) under some non-contrived binary operations.

So, for instance, Burro programs form a _group_ under concatenation,
which means that, for every Burro program, you can find some other Burro program
that annihilates it (concatenating it to the first program yields a null program.)

A _ring_ is a somewhat stricter algebraic structure: it is a set (of programs,
in this case) with *two* binary operations
(called the additive operation and the multiplicative operation).
The operations could be any transformation that can be applied to any two programs to produce
another program.  They must meet certain constraints, however — algebraic properties
which must hold for all members of the set.  Rings build on groups (Abelian groups, actually)
and extend them with a couple of further properties, including _distributivity_, which
should look familiar from even high school algebra:
(_a_ + _b_) * _c_ = (_a_ * _c_) + (_b_ * _c_).

I set out looking for a language whose programs form a ring under some appropriate operations,
but I have yet to find one.

I tried using sequential composition as the multiplicative
operation and parallel execution as the additive operation in
[Cabra][], but the result
was a slightly different algebraic structure, an _idempotent semiring_
(also called a _dioid_.)
Another, somewhat more experimental (and unpublished) design I toyed with
treats a program as a map from a set of labels to basic blocks,
with Cartesian product of label sets as the multiplicative
operation, and set-union of label sets as the additive operation.
This too is only a dioid.

So what semantics, specifically what choice of operations,
would lead to a proper ring?

Obviously it'd be best if the operations weren't completely
contrived.  It's probably possible to have rather degenerate operations
where the additive operation is based directly on addition of numbers,
while the multiplicative operation is based on numerical multiplication.
It's possible this could be done by extending addition and multiplication to
unbounded arrays of numbers — that is, tapes — and have programs
manipulate the tapes.  But I don't think it's a very interesting route to explore.

The most natural (in some sense) choice for the mulitplicative operator
is sequential composition (which corresponds to concatenation of program
texts in many simple languages.)  The problem is that when
you sequentially compose two programs, the first program might never
halt — so the second program doesn't ever run, and it doesn't matter
what that program is.  In algebraic terms, the first program *absorbs*
the second during sequential composition: _a_ * _b_ = _a_,
for any choice of _b_.  But in ring theory, this implies
_a_ + _a_ = _a_, and there is only
one element for which that fits: _a_ = 0.  Moreover, we need
_x_ + 0 = _x_ for some _x_ that's not zero.
That means we need some way to "ignore" a program which doesn't halt during addition, if it doesn't halt,
but some way to pay attention to it if it does halt
(to evaluate general statements like _x_ + _y_ = _z_.)
The problem is, that means we need some way to tell if programs halt or not,
which is (drum roll please) the Halting Problem.

(So why do dioid languages seem much easier to get than ring languages?
Well, unlike rings, dioids *do* provide idempotency, as a property
of addition — _a_ + _a_ = _a_ for any choice of _a_ —
and that can be exploited here.
It's also worth noting that there are some fundamental theoretical computer science concepts which are
dioid-based; for example, regular expressions can be defined by _Kleene algebras_,
which are dioids with an extra "Kleene star" operation.)

Even if we restrict ourselves to the programs that always halt,
multiplicative sequential composition poses an extremely tricky problem
when we try to address distributivity — in particular, right-distributivity.
We need (_a_ + _b_) * _c_ = (_a_ * _c_) + (_b_ * _c_).
If we think of the left side as combining the results of _a_ and _b_,
and then running _c_ on those results, then the right side means that we ought to
get the same thing if we combine the results of two runs: running _a_ then _c_,
and running _b_ then _c_.  Problem is, _c_ can do all kinds of
crazy things, even when it always halts.  It could check that its input is the result of what you would get by running
_a_ only, or _b_ only, but not anything else.  The right side
is then effectively _c_ + _c_, and how do you in general enforce that combining some result
with itself has the same semantics as combining two different results and possibly post-processing them?

I suspect that the underlying reason that getting a ring language
is hard (at least when you insist on sticking
to "intuitive" operations) is because a ring is starting
to approach a structure (a Euclidean domain) in which you 
can perform the Euclidean algorithm and obtain greatest
common denominators.
Now, if you could perform that algorithm on programs, you'd
be able to decompose every program into "prime subprograms".
This sounds intuitively a little too powerful — you'd
be able to find programs which are in some sense optimal!
I'm not certain this would actually *violate* established
undecidability results like Rice's theorem, but it certainly
sounds like it's edging up against them.

### Praline

*   genre: Experimental language
*   paradigms: Imperative
*   summary: an imperative language with continuations (what a terrible summary)
*   inception-date: ca Sep 2012

Observe that in a typical imperative language you are given keywords
with which you can modify the control flow.  You may have `break` and
`continue` to stop or restart a loop, and you may have `return` to exit
a function, and perhaps `exit` to terminate the entire program.

But these have limitations.  If you have a nested loop, you can't break
out of the outer loop from the inner loop.  And you can't write a little
utility function that exits the function it's called from if some condition
is true.  And, although this is surely a minor point, you're stuck with
whatever keywords the language designer chose.

But the fact is, these don't need to be keywords at all, because they all
represent continuations.  Instead, loops and functions can bind these
continuations lexically to identifiers the programmer chooses at the
top of the structure.  This provides a solution to all of the problems
listed above, and perhaps opens up some possibilities.  Now, your
loops look like this:

    while (a > 5) [continue, break] {
        b := something(a);
        if (b > 10) break;
        if (b > 100) { a := a * 2; continue; }
        a := a - 1;
    }

It should be apparent that this allows breaking out of a nest of loops:

    while (a > 5) [continue, break_outer] {
        while (b > a * 7) [continue, break_inner] {
            ...
            if (something(a, b)) break_outer;
        }
    }

In a similar manner, your functions now look like:

    function mul(a, b) [return] {
        return(a * b);
    }

Assuming you can pass these continuations around, you can now write
that little utility function:

    function check(a, b, exit) [return] {
        if (a > b) exit;
        return(a * b);
    }
    function something() [return] {
        ...
        c := check(17, 22, return);
        d := check(5, 29, return);
        ...
    }

Of course, there are some issues with typing (what's the return
value of the function you're exiting?) but that's the basic idea.

### Psogumma

*   genre: Esolang
*   paradigms: Meta-circular
*   summary: grammar self-modifies to accomodate program
*   inception-date: 2011

The Psogumma language provides a small, fixed grammar to start, possibly:

    Program ::= "+"* | "[" Program "]".

However, when parsing a program, whenever there is a syntax error,
the grammar is modified in a way which is pseudorandom, but always
compatible with the input that caused the syntax error.  New productions
may be introduced, or existing productions may be modified, to accomodate
the input.  The semantics of the grammar modifications are similarly
pseudorandomly generated at the moment they are applied.  The pseudorandom
number generator is deterministic, starting with a fixed seed, but is
continually engaged (being called each time an input symbol is consumed).

The result is that all programs are parsable, and all programs have
a well-defined meaning, although divining that meaning before parsing
the program is at best an arduous task and at worst unpredictable (without
having already parsed the program.)

### Seltzer Spigot

*   genre: Esolang
*   paradigms: []
*   summary: computational ascii art
*   inception-date: ca Dec 2008

Once, quite innocently, I ran a Perl script I was writing to
produce a simple inverted index.  Completely nothing special.
But when I ran it, I was surprised to get the following beautiful
output — it turns out I got a regular expression wrong (I always
think whitespace is `\w` when it's really `\s`...)
So, the challenge is to find a
programming language in which this output is a meaningful program
and, in general, programs look something like this:

    :
     :
      :
      ../../:
      /:
     ../../:
     /:
     \
    :
    ++.:
    -:
    .:
    /:
    : :

### YO_DAWG

*   genre: Esolang
*   paradigms: Meta-circular
*   summary: Yo dawg, I herd you like esolangs, so I put an esolang in your esolang so you can esolang while you esolang
*   inception-date: ca 2012
*   influences: Mascarpone

YO_DAWG is an esolang with first-class esolangs. You can create
new [Befunge-93][] objects, [brainfuck][] objects, [Underload][] objects,
and so forth, and probably stick them onto a stack, or into variables.
Presumably, you can apply these objects to strings of characters, to run
programs in those esolangs; but more interestingly, being first-class objects,
esolangs in YO_DAWG can take esolangs as arguments, and return esolangs...
and you can probably compose esolangs (in truly,
*truly* pointless style) to form new esolangs.

Naturally, you can also create new YO_DAWG objects.

### Deturgenchry

*   etymology: mangling of the words "detergent", "urgency", and "gentry"
*   genre: Esolang
*   paradigms: Object-oriented, Continuation-passing
*   summary: an object-oriented language with both `self` and `other`, and each of these is a continuation
*   inception-date: 2011

Deturgenchry is an object-oriented language with both `self` and `other`,
and each of these is a continuation (or something.)

Unlike most of the other languages on this list, work on a Deturgenchry
reference distribution was actually started: the
[Deturgenchry distribution](https://catseye.tc/distribution/Deturgenchry_distribution),
But it has not gone much of anywhere.  Thus it is more suited for
inclusion in this list than in the list of [the completed][].
Maybe if I finish it one day I'll move it back there.

### Pophery

*   etymology: mangling of the word "porphyry"
*   genre: Esolang
*   paradigms: Imperative, String-rewriting
*   summary: an imperative string-rewriting language.  I know right?
*   inception-date: 2010

Pophery is an imperative string-rewriting language.  I know right?

Unlike most of the other languages on this list, work on a Pophery
reference distribution was actually started: the
[Pophery distribution](https://catseye.tc/distribution/Pophery_distribution).
But it has not gone much of anywhere.  Thus it is more suited for
inclusion in this list than in the list of [the completed][].
Maybe if I finish it one day I'll move it back there.


[Befunge-93]: ../article/Languages.md#befunge-93
[Burro]: ../article/Languages.md#burro
[Cabra]: ../article/Languages.md#cabra
[Erlang]: ../article/Project%20Dependencies.md#erlang
[Java]: ../article/Project%20Dependencies.md#java
[Mascarpone]: ../article/Languages.md#mascarpone
[Muriel]: https://esolangs.org/wiki/Muriel
[SETL]: https://en.wikipedia.org/wiki/SETL
[Scheme]: ../article/Project%20Dependencies.md#scheme
[Turing-complete]: https://esolangs.org/wiki/Turing-complete
[Underload]: https://esolangs.org/wiki/Underload
[Unlikely]: ../article/Languages.md#unlikely
[ZOWIE]: ../article/Languages.md#zowie
[brainfuck]: https://esolangs.org/wiki/brainfuck
[esoteric programming languages]: http://esolangs.org/
[the completed]: https://catseye.tc/node/Chris%20Pressey%27s%20Lingography

