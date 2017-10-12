Language Implementations
========================

*   common auspices: Cat's Eye Technologies
*   common authors: Chris Pressey

This is a list of languages that Cat's Eye Technologies has built an implementation for,
but which were not designed by Cat's Eye Technologies.

### PL-{GOTO}.NET

*   implementation of: PL-{GOTO}
*   implementation type: compiler
*   host language: Haskell
*   target language: MSIL
*   inception date: ???
*   in distribution: [PL-{GOTO}.NET distribution](/distribution/PL-{GOTO}.NET distribution)

PL-{GOTO}.NET is a compiler for the language PL-{GOTO}
from Brainerd and Landweber's _[Theory of Computation](http://www.worldcat.org/title/theory-of-computation/oclc/694056)_.
PL-{GOTO} can express exactly the
primitive recursive functions, and thus PL-{GOTO} programs
always terminate. PL-{GOTO}.NET generates MSIL code which
can then (using `ilasm`) be turned into a .NET
executable.  It can also execute PL-{GOTO} programs
directly.

I've been idly fascinated by the primitive recursive example programming language
PL-{GOTO} from Brainerd and Landweber's _[Theory of Computation](http://www.worldcat.org/title/theory-of-computation/oclc/694056)_ for some time.
And for some reason I will never be able to explain, I had the craving to implement a compiler
which could produce .NET executables by generating MSIL assembly language.  And putting
those two together — well, that struck me as a respectably absurd match, so that's what I did.
The compiler is written in Haskell and uses Parsec for parsing PL-{GOTO} programs; I tried
to keep the grammar true to what is presented in the book, not refactoring it to be LL(1), and
keeping the `←` symbol for assignment.

### aubergine.hs

*   implementation of: Aubergine
*   implementation type: interpreter
*   host language: Haskell
*   inception date: ???

I implemented Aubergine because the reference interpreter is buggy and
I wanted a version that actually implemented the unbounded integers that
the language description suggests.  After implementing it, I was familiar
enough with it to write a sketch of a proof of its [Turing-complete][]ness.

### muriel.pl

*   implementation of: Muriel
*   implementation type: interpreter
*   host language: Perl
*   inception date: Mar 23, 2001
*   in distribution: [Muriel distribution](/distribution/Muriel distribution)

This is an interpeter, written in Perl, for Matthew Westcott's
quine-based language Muriel.  It was probably
the first full implementation of that language.

### pibfi

*   implementation of: brainfuck
*   implementation type: interpreter
*   host language: Erlang
*   inception date: ???
*   in distribution: [pibfi distribution](/distribution/pibfi distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

In contrast to all the ultra-minimal Brainfuck interpreters and
compilers out there, I figured I should write a monster: the Platonic Ideal BrainFuck Interpreter.
Written in Erlang, it contains just about every feature under the sun, including the kitchen sink.
I sort of lost interest when I was adding profiling and discovered there were several different
extant reckonings of a "number of instructions executed" metric for Brainfuck.  I guess it was that
point that made me recognize just how silly this project was...

### sf2tab

*   implementation of: Smallfuck
*   implementation type: compiler
*   host language: ANSI C
*   target language: lookup table
*   inception date: ???
*   in distribution: [The Dipple](/distribution/The Dipple)

Based on the observation that Smallfuck, lacking the (assumed-)infinite tape of Brainfuck,
can only express finite-state automata, I wrote a little program in C to compile Smallfuck programs to
(generally gigantic) lookup-tables.

There is an old [sf2tab distribution](/distribution/sf2tab distribution).

### stringie

*   implementation of: Underload
*   implementation type: interpreter
*   host language: ANSI C
*   inception date: ???
*   in distribution: [stringie distribution](/distribution/stringie distribution)

Seeing that there was no *non*-pathological implementation of Alex Smith's
beautiful [Underload][] language in C, I undertook that project one evening.
(In the company of a bottle of really fine wine.  Why, it cost almost twelve dollars.)
The result is one of the most pedantic and boring Underload interpreters known to
man.  Perhaps the most interesting property of it is its name, `stringie`, which was
an accident.

### tc.catseye.yoob.ale

*   implementation of: Ale
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.backflip

*   implementation of: BackFlip
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.black

*   implementation of: Black
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.brainfuck

*   implementation of: brainfuck
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.lnusp

*   implementation of: LNUSP
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.onela

*   implementation of: 1L_a
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.onelaoi

*   implementation of: 1L_AOI
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.path

*   implementation of: PATH
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.qdeql

*   implementation of: Qdeql
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.sceql

*   implementation of: Sceql
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.snusp

*   implementation of: SNUSP
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.twoill

*   implementation of: 2-ill
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### tc.catseye.yoob.twol

*   implementation of: 2L
*   implementation type: interpreter
*   host platform: yoob
*   host language: Java
*   inception date: ???
*   in distribution: [yoob distribution](/distribution/yoob distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Implemented as part of yoob.

### thue.rb

*   implementation of: Thue
*   implementation type: interpreter
*   host language: Ruby
*   inception date: Sep 10, 2012
*   in distribution: [Thue distribution](/distribution/Thue distribution)

Since I've been maintaining a distribution of this language for a while, and
not otherwise involved with it, I decided I should finally implement it.
After knocking my head against the spec and reference implementation
for a few hours (over the course of months, or has it been years?), I finally
did implement it.

### valgol.erl

*   implementation of: VALGOL
*   implementation type: parser
*   host language: Erlang
*   inception date: ???
*   in distribution: [The Dipple](/distribution/The Dipple)

A parser, in Erlang, for the Lesser-Known Language VALGOL.
It, like, totally demonstrates how a parser can be written so
that a separate scanner is totally not needed.  Bitchen!

- - - -

[Turing-complete]: TBD
[Underload]: TBD

