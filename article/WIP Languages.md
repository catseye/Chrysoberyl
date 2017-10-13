WIP Languages
=============

*   common development-stage: work in progress

Languages that are works-in-process at Cat's Eye Technologies.

Some of these will be moved to the [Languages](Languages.md) list someday, with any luck.

Unlike [LoUIE](LoUIE.md), some work has actually been done on these, just not to a "finished" state.

### Deturgenchry

*   type: Programming Language
*   inception-date: 2011
*   genre: Esolang
*   paradigms: Object-oriented, Continuation-passing
*   etymology: neologism

Deturgenchry is an object-oriented language with both `self` and `other`,
and each of these is a continuation (or something.)

#### Reference Implementation: Deturgenchry.hs

*   in-distribution: Deturgenchry distribution
*   license: Unknown license
*   implementation-type: interpreter
*   host-language: Haskell

### Kosheri

*   type: Programming Language
*   inception-date: ca 2007
*   genre: Production Language
*   etymology: Egyptian street food

Kosheri is a virtual machine design that rose from the ashes
of [Bhuna][].

#### Reference Implementation: kosheri (C)

*   in-distribution: Kosheri distribution
*   license: Unknown license
*   implementation-type: interpreter
*   host-language: C99

### Pophery

*   type: Programming Language
*   inception-date: 2010
*   genre: Esolang
*   paradigms: Imperative, String-rewriting
*   etymology: mangling of Porphyry

Pophery is an imperative string-rewriting language.  I know right?

#### Reference Implementation: pophery.py

*    in-distribution: Pophery distribution
*    license: Unknown license
*    implementation-type: interpreter
*    host-language: Python

### Robin

*   type: Programming Language
*   inception-date: 2011
*   genre: Production language
*   paradigms: Functional
*   etymology: bird

Robin is a language drawing from [Pixley][], [Erlang][], and [PicoLisp][].
One distinctive feature of it is that it has an extremely small core semantics,
to the point where even closures are defined in terms of macros.
Another distinctive feature is that it is heavily resource-oriented; almost
everything, including concurrent processes, is (or should be) a virtual device
which must be acquired from a central resource arbiter.  This arbiter may
satisfy the constraints you specify when requesting a device any way it sees
fit; so the operating environment has potentially a lot of influence over
exactly what your program does.

#### Reference Implementation: Robin.lhs

*   in-distribution: Robin distribution
*   license: BSD license
*   implementation-type: interpreter
*   host-language: Haskell

### Castile

*   type: Programming Language
*   inception-date: Nov 21, 2012
*   genre: Experimental language
*   computational-class: believed Turing-complete
*   influences: Eightebed, Rust
*   paradigms: Imperative, Functional
*   etymology: soap
*   sample program: 

        fun foo(a, b: integer|string) {
          r = a;
          typecase b is integer {
            r = r + b;
          };
          typecase b is string {
            r = r + len(b);
          };
          r
        }
        main = fun() {
          a = foo(a, 333 as integer|string);
          a = foo(a, "hiya" as integer|string);
          a /* should output 337 */
        }

Castile is an unremarkable programming language which exists mainly
because an unremarkable evaluator/compiler for it was written.  It is
a bit like [ANSI C][] except with proper union types (and no typecasts.)  Local
variables are mutable, but arguments and globals aren't.  The compiler
supports several backends, including [Javascript][] and [Ruby][].

#### Reference Implementation: castile.py

*   in-distribution: Castile distribution
*   license: Unknown license
*   implementation-type: interpreter
*   host-language: Python

Also it's a compiler to Javascript, Ruby, stackmac, almost C...

### SixtyPical

*   type: Programming Language
*   inception-date: Apr 2014
*   genre: Machine language
*   paradigms: Imperative
*   etymology: portmanteau
*   reference-distribution: SixtyPical distribution
*   sample program: 

        byte table screen @ 1024
        routine main
          trashes a, x, z, n, screen
        {
            ld x, 0
            ld a, 83    // 83 = screen code for heart
            repeat {
                st a, screen + x
                inc x
            } until z
        }

SixtyPical is a very low-level programming language, similar to 6502
assembly, which defines a set of static analyses via type-checking and
abstract interpretation (liveness analysis of variables, i.e. memory
locations.)

#### Reference Implementation: sixtypical (Python)

*   license: BSD license
*   host-language: Python
*   implementation-type: compiler
*   target-language: 6502 machine code

#### Implementation: sixtypical (Haskell)

*   license: BSD license
*   host-language: Haskell
*   implementation-type: compiler
*   target-language: Ophis Assembler

### Tamsin

*   type: Programming Language
*   inception-date: Apr 2014
*   genre: Experimental language
*   paradigms: Functional, Logic programming, Metalanguage
*   etymology: feminine given name
*   reference-distribution: Tamsin distribution
*   sample program: 

        main = expr0 → E & walk(E).
        expr0 = expr1 → E1 & {"+" & expr1 → E2 & E1 ← add(E1,E2)} & E1.
        expr1 = term → E1 & {"*" & term → E2 & E1 ← mul(E1,E2)} & E1.
        term = "x" | "y" | "z" | "(" & expr0 → E & ")" & E.
        walk(add(L,R)) = walk(L) → LS & walk(R) → RS & return LS+RS+' +'.
        walk(mul(L,R)) = walk(L) → LS & walk(R) → RS & return LS+RS+' *'.
        walk(X) = return ' '+X.

Tamsin is an oddball little language that can't decide if it's a
meta-language, a programming language, or a [rubbish lister](/node/Perl).
Its primary goal is to allow the rapid development of parsers,
static analyzers, interpreters, and compilers, and to allow them
to be expressed *compactly*.

#### Reference Implementation: tamsin.py

*   in-distribution: Tamsin distribution
*   license: BSD license
*   host-language: Python
*   implementation-type: interpreter

Kind of compiles, too.

#### Implementation: tamsin.tamsin

*   in-distribution: Tamsin distribution
*   license: BSD license
*   host-language: Tamsin
*   implementation-type: compiler
*   target-language: C99

### Zame

*   type: Programming Language
*   inception-date: Jan 2009
*   genre: Esolang
*   variant-of: Etcha
*   paradigms: Maze-space-rewriting (kind of)
*   sample program: 

        #########
        # #     #
        # # # ###
        #   #   #
        ### # # #
        #   # # #
        #########


Zame is an automaton which uses the solution of a maze to
generate an [Etcha][] program which draws a new maze, then
the process repeats.  An open question is to find a maze for which
this process repeats indefinitely.

Where it stands relative to other models of computation is, therefore,
not well understood.

Information on this language is only available on the Esowiki for now:
[Zame](http://esolangs.org/wiki/Zame).

This is not really a WIP, is it, maybe.

This is actually a language family.

- - - -

[ANSI C]: http://clc-wiki.net/wiki/C89
[Perl]: http://www.perl.org/
[Erlang]: http://www.erlang.org/
[NASM Assembler]: http://nasm.us/
[Java]: http://www.oracle.com/technetwork/java/index.html
[Haskell]: http://www.haskell.org/
[Pixley]: ../article/Languages.md#pixley
[Etcha]: ../article/Languages.md#etcha
[Bhuna]: ../article/Languages.md#bhuna
[Javascript]: http://www.ecma-international.org/publications/standards/Ecma-262.htm
[Ruby]: http://www.ruby-lang.org/
[PicoLisp]: https://picolisp.com/wiki/?home

