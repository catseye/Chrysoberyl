Language Implementations
========================

*   common auspices: Cat's Eye Technologies
*   common authors: Chris Pressey
*   image_url: https://static.catseye.tc/images/illustrations/Perpetual_Motion_Machine.jpg

This is a list of languages that Cat's Eye Technologies has built an implementation of,
but which were not designed by Cat's Eye Technologies.  For those, see [Languages](Languages.md).

Note that Cat's Eye Technologies also maintains some [forks](Forks.md) of some language projects.

### aubergine.hs

*   implementation of: [Aubergine][]
*   implementation type: interpreter
*   host language: [Haskell][]
*   inception date: Oct 18, 2012

I implemented Aubergine because the reference interpreter is buggy and
I wanted a version that actually implemented the unbounded integers that
the language description suggests.  After implementing it, I was familiar
enough with it to write a sketch of a proof of its [Turing-complete][]ness.

Here it is: [Aubergine/aubergine.hs](https://esolangs.org/wiki/Aubergine/aubergine.hs).

### Cardboard Prolog

*   implementation of: Prolog
*   implementation type: interpreter
*   host language: [Scheme][]
*   inception date: ca 2018
*   in distribution: [Cardboard Prolog distribution](https://catseye.tc/distribution/Cardboard_Prolog_distribution)

When I was refreshing myself on how a Prolog interpreter works, I found several descriptions and examples
of Prolog interpreters online, but none were quite what I wanted, so I wrote this.  It's a tiny
inference engine (~120 lines) written in purely functional R5RS Scheme.  It lacks all the amenties of
the Prolog language proper, and it uses Scheme literals instead of Prolog syntax, but it does do the
thing that's at the core of Prolog execution: deduction based on Horn clauses.

### muriel.pl

*   implementation of: [Muriel][]
*   implementation type: interpreter
*   host language: [Perl][]
*   inception date: Mar 23, 2001
*   in distribution: [Muriel distribution](https://catseye.tc/distribution/Muriel_distribution)

This is an interpeter, written in Perl, for Matthew Westcott's
quine-based language Muriel.  It was probably
the first full implementation of that language.

### Odd.hs

*   implementation of: [An Odd Rewriting System][]
*   implementation type: interpreter
*   host language: [Haskell][]
*   inception date: ca 2019

I implemented An Odd Rewriting System because it is quite unusual and I
wanted to understand it better and I wanted to leave behind some kind
of artefact that might help others who want to understand it better.

Here it is: [An Odd Rewriting System/Odd.hs](https://esolangs.org/wiki/An_Odd_Rewriting_System/Odd.hs).

### pibfi

*   implementation of: [brainfuck][]
*   implementation type: interpreter
*   host language: [Erlang][]
*   inception date: May 5, 2003
*   in distribution: [pibfi distribution](https://catseye.tc/distribution/pibfi_distribution)

In contrast to all the ultra-minimal Brainfuck interpreters and
compilers out there, I figured I should write a monster: the Platonic Ideal BrainFuck Interpreter.
Written in Erlang, it contains just about every feature under the sun, including the kitchen sink.
I sort of lost interest when I was adding profiling and discovered there were several different
extant reckonings of a "number of instructions executed" metric for Brainfuck.  I guess it was that
point that made me recognize just how silly this project was...

### PL-{GOTO}.NET

*   implementation of: [PL-{GOTO}][]
*   implementation type: compiler
*   host language: [Haskell][]
*   target language: [MSIL][]
*   inception date: May 2011
*   in distribution: [PL-{GOTO}.NET distribution](https://catseye.tc/distribution/PL-{GOTO}.NET_distribution)
*   online @ [catseye.tc](https://catseye.tc/installation/PL-{GOTO})

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

### sf2tab

*   implementation of: [Smallfuck][]
*   implementation type: compiler
*   host language: [ANSI C][]
*   target language: lookup table
*   inception date: Jun 23, 2005
*   in distribution: [The Dipple](https://catseye.tc/distribution/The_Dipple)

Based on the observation that Smallfuck, lacking the (assumed-)infinite tape of Brainfuck,
can only express finite-state automata, I wrote a little program in C to compile Smallfuck programs to
(generally gigantic) lookup-tables.

There is also an old [sf2tab distribution](https://catseye.tc/distribution/sf2tab_distribution).

### stringie

*   implementation of: [Underload][]
*   implementation type: interpreter
*   host language: [ANSI C][]
*   inception date: Sep 2010
*   in distribution: [stringie distribution](https://catseye.tc/distribution/stringie_distribution)

Seeing that there was no *non*-pathological implementation of Alex Smith's
beautiful [Underload][] language in C, I undertook that project one evening.
(In the company of a bottle of really fine wine.  Why, it cost almost twelve dollars.)
The result is one of the most pedantic and boring Underload interpreters known to
man.  Perhaps the most interesting property of it is its name, `stringie`, which was
an accident.

### tc.catseye.yoob.ale

*   implementation of: [Ale][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.backflip

*   implementation of: [BackFlip][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.black

*   implementation of: [Black][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.brainfuck

*   implementation of: [brainfuck][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.lnusp

*   implementation of: [LNUSP][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.onela

*   implementation of: [1L_a][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.onelaoi

*   implementation of: [1L_AOI][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.path

*   implementation of: [PATH][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.qdeql

*   implementation of: [Qdeql][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: Jun 27, 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.sceql

*   implementation of: [Sceql][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: Jun 27, 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.snusp

*   implementation of: [SNUSP][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.twoill

*   implementation of: [2-ill][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### tc.catseye.yoob.twol

*   implementation of: [2L][]
*   implementation type: interpreter
*   host platform: yoob
*   host language: [Java][]
*   inception date: May 2011
*   in distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)
*   jnlp @ [archive.org](https://archive.org/details/yoob-rel_0_3_2018_1128)

Implemented as part of yoob.

### thue.rb

*   implementation of: [Thue][]
*   implementation type: interpreter
*   host language: [Ruby][]
*   inception date: Sep 10, 2012
*   in distribution: [Thue distribution](https://catseye.tc/distribution/Thue_distribution)

Since I've been maintaining a distribution of this language for a while, and
not otherwise involved with it, I decided I should finally implement it.
After knocking my head against the spec and reference implementation
for a few hours (over the course of months, or has it been years?), I finally
did implement it.

### valgol.erl

*   implementation of: [VALGOL][]
*   implementation type: parser
*   host language: [Erlang][]
*   inception date: Oct 11, 2002
*   in distribution: [The Dipple](https://catseye.tc/distribution/The_Dipple)

A parser, in Erlang, for the Lesser-Known Language VALGOL.
It, like, totally demonstrates how a parser can be written so
that a separate scanner is totally not needed.  Bitchen!

Implemented Automata
--------------------

We don't have a dedicated page for implemented automata yet, so they are here.

### life.alp

*   implementation of: [Conway's Game of Life][]
*   implementation type: interpreter
*   host language: [ALPACA][]
*   inception date: 1998
*   in distribution: [ALPACA distribution](https://catseye.tc/distribution/ALPACA_distribution)

Conway's Game of Life, in ALPACA.

### wireworld.alp

*   implementation of: [Wireworld][]
*   implementation type: interpreter
*   host language: [ALPACA][]
*   inception date: 1998
*   in distribution: [ALPACA distribution](https://catseye.tc/distribution/ALPACA_distribution)

Wireworld, in ALPACA.

- - - -

[Turing-complete]: https://esolangs.org/wiki/Turing-complete
[Underload]: https://esolangs.org/wiki/Underload
[1L_AOI]: https://esolangs.org/wiki/1L_AOI
[Aubergine]: https://esolangs.org/wiki/Aubergine
[An Odd Rewriting System]: https://esolangs.org/wiki/An_Odd_Rewriting_System
[Qdeql]: https://esolangs.org/wiki/Qdeql
[2-ill]: https://esolangs.org/wiki/2-ill
[PL-{GOTO}]: http://www.worldcat.org/title/theory-of-computation/oclc/694056
[1L_a]: https://esolangs.org/wiki/1L_a
[Sceql]: https://esolangs.org/wiki/Sceql
[VALGOL]: https://esolangs.org/wiki/VALGOL
[BackFlip]: https://esolangs.org/wiki/BackFlip
[Smallfuck]: https://esolangs.org/wiki/Smallfuck
[LNUSP]: https://esolangs.org/wiki/LNUSP
[Muriel]: https://esolangs.org/wiki/Muriel
[Black]: https://esolangs.org/wiki/Black
[PATH]: https://esolangs.org/wiki/PATH
[2L]: https://esolangs.org/wiki/2L
[brainfuck]: https://esolangs.org/wiki/brainfuck
[Thue]: https://esolangs.org/wiki/Thue
[SNUSP]: https://esolangs.org/wiki/SNUSP
[1L]: https://esolangs.org/wiki/1L
[Ale]: https://esolangs.org/wiki/Ale
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[C99]: ../article/Project%20Dependencies.md#c99
[Perl]: ../article/Project%20Dependencies.md#perl
[Erlang]: ../article/Project%20Dependencies.md#erlang
[Haskell]: ../article/Project%20Dependencies.md#haskell
[Java]: ../article/Project%20Dependencies.md#java
[Conway's Game of Life]: http://en.wikipedia.org/wiki/Conway's_Game_of_Life
[Wireworld]: http://en.wikipedia.org/wiki/Wireworld
[ALPACA]: ../article/Languages.md#alpaca
[Scheme]: ../article/Project%20Dependencies.md#scheme
[AmigaDOS 1.3]: ../article/Project%20Dependencies.md#amiga-500
[Zz]: https://catseye.tc/modules/OpenZz/doc/zzdoc.html
[Zzrk]: ../article/Games.md#zzrk
[Ruby]: ../article/Project%20Dependencies.md#ruby
[MSIL]: http://www.ecma-international.org/publications/standards/Ecma-335.htm

