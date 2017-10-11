Chris Pressey's Lingography
===========================

(What is a "lingography", you ask? Well, if bands have disc-ographies and directors have film-ographies...)

This is a list, given in approximate chronological order, of the languages I've designed and/or implemented.
It is more-or-less unabridged, but not intended to be completely exhaustive. Most of these language are
programming languages; some of them are formal languages, and some of them are automata of some kind.
Many of them are esolangs. Some of them possibly aren't even languages at all; they just seem to fit the
general theme of the list. Most of them have been implemented, and these implementations are available in
downloadable distrbutions. At the bottom there is also a list of languages that I've implemented, but which
were designed by someone else.

You may also be interested in reading about what it was like to design these and/or the ones that got away.

Languages I've Designed
-----------------------


### Maentwrog

*   type: Programming Language
*   inception-date: ca 1993
*   genre: Pedagogical language
*   development-stage: archival
*   computational-class: known not Turing-complete
*   paradigms: Stack-based

Maentwrog is an RPN-calculator-turned-FORTH-interpreter which
probably counts as [Chris Pressey][]'s first *proper* programming language.
It was implemented on his Amiga 500 in 1993, then lost and unearthed
multiple times.  It is hardly remarkable, save that it spawned [Befunge-93][].

Sample program:

    *a *b *c
    0 =a 1 =b
    : fib a b + =c c . b =a c =b c 100000 < @fib ;
    1 . fib

#### Reference Implementation: maentw.c

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: ANSI C

### Full Moon Fever

*   type: Programming Language
*   inception-date: ca 1993
*   genre: DSL
*   development-stage: archived
*   computational-class: known not Turing-complete
*   paradigms: Imperative

Full Moon Fever is a language for describing ASCII animations.
It was used to deliver animated screens on Chris Pressey's BBS
(when it was operational in the early 90's) via [ANSI terminal](ANSI Terminal) control codes.
This probably counts as his first proper language, even though
it wasn't a full programming language, because it had
the usual machinery (syntax, parser, interpreter...)
Lives on, in a somewhat distended form, as a sub-language of
[ILLGOL][].

Sample program:

    GO 1 2 CLREOL CENTRE "Enter... the Stupid Guard." 2
    GO 1 3 CLREOL
    PAUSE 70
    GO 76 19
    PRINT "0"
    PAUSE 20
    DO 20
        LF PRINT " " LF LF PRINT "0" PAUSE 5;


### Befunge-93

*   type: Programming Language
*   inception-date: Sep 1993
*   genre: Esolang
*   development-stage: mature
*   computational-class: can simulate some push-down automata
*   influences: Maentwrog, brainfuck, FALSE
*   paradigms: Stack-based, 2-dimensional, Self-modifying

Befunge-93 is an esoteric programming language where the program exists
in a two-dimensional grid of cells, where each cell contains a single
instruction, and execution can proceed in any cardinal direction across this
grid — not just left-to-right, but also right-to-left, top-to-bottom, and
bottom-to-top.

Sample program:

     v    <
    >?"/",^
     >"\",^
    

#### Reference Implementation: bef

*   license: BSD license
*   implementation-type: interpreter
*   host-language: ANSI C
#### Implementation: tc.catseye.yoob.befunge93

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Java

### Cyclobots

*   type: Automaton
*   inception-date: ca 1994
*   genre: Toy
*   development-stage: mature
*   computational-class: ???
*   paradigms: Angular, Particle automaton

Cyclobots is an automaton that consists of a number of little virtual
"turtle robots" called "cyclobots".  Each cyclobot moves with a constant
velocity, and tries to follow exactly one other cyclobot, adjusting
its heading to point towards the cyclobot it is following.
No cylobot is followed by more than one cyclobot.

A group of cyclobots tends to fall into one of several semi-stable
patterns.  The simplest of these is just a rotating circle, but
more complex, [trefoil](http://en.wikipedia.org/wiki/Trefoil_knot)-like
patterns are more common.

#### Implementation: cyclobots.js

*   license: Freely Redistributable
*   implementation-type: ???
*   host-language: Javascript
#### Implementation: Cyclobots (Visual Basic)

*   license: Freely Redistributable
*   implementation-type: ???
*   host-language: Visual Basic

### SMETANA

*   type: Automaton
*   inception-date: ca 1994
*   genre: Esolang
*   development-stage: archival
*   computational-class: known not Turing-complete
*   paradigms: Self-modifying

SMETANA is a pathological little self-modifying language with only two
possible operations: Go to step *n*, and Swap steps *n* and *m*.
It has inspired a few variants and developments, notably a proof that
despite its minimalism, it is finite-automata-complete; it is also the
(great-?)grandfather of [SMITH][].

Sample program:

    Step 1. Swap step 1 with step 2.
    Step 2. Go to step 2.
    Step 3. Go to step 1.

#### Reference Implementation: smetana.pl

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Perl
#### Implementation: SMETANA (Visual Basic)

*   license: Freely Redistributable
*   implementation-type: interpreter
*   host-language: Visual Basic
#### Implementation: tc.catseye.yoob.smetana

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Java

### Wierd

*   type: Programming Language
*   inception-date: 1997
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   influences: brainfuck, Befunge-93
*   paradigms: Stack-based, 2-dimensional, Angular
*   reference-distribution: [Wierd distribution](/distribution/Wierd distribution)

Wierd is a programming language, inspired somewhat by [Befunge-93][] and
[brainfuck][], where instructions are not determined by the symbols in a
sequence of symbols, but by the *bends* in a sequence of symbols.

The original Wierd, designed during a three-way email conversation, is
probably lost and gone forever, but two dialects have been specified
(sorta) and implemented: [Wierd (John Colagioia)][] and
[Wierd (Milo van Handel)][].

Sample program:

    *
     *
      *
       *
      * *  **
     *   ** *
      **     **
        *      *
        *     *
        *     *
        *      *
        *     **
        *    *
        * ** *
        **  *
    


### RUBE

*   type: Automaton
*   inception-date: 1997
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: Bully automaton, 2-dimensional

RUBE is an esoteric programming language in tribute to [Rube Goldberg][],
with bulldozers pushing around numbered crates, knocking them together to
perform computations.  It is based on a variant of a cellular automaton called
a *[bully automaton](Bully automaton)*, where certain state changes can
force other state changes to occur elsewhere in the playfield.

Sample program:

      0a21646c726f77202c6f6c6c6548
    , :::::::::::::::::::::::::::: ,
     )
     ==============================
    F
                                   O F
                                   c
                                   =
    

#### Reference Implementation: rube.c

*   license: BSD license
*   implementation-type: interpreter
*   host-language: ANSI C

### Befunge-97

*   type: Programming Language
*   inception-date: Dec 25, 1997
*   genre: Esolang
*   development-stage: lost
*   computational-class: ???
*   influences: Befunge-93
*   paradigms: Stack-based, 2-dimensional, Self-modifying

Befunge-97 was an unimplemented attempt to design a successor to [Befunge-93][].
The design, however, was not successful — it has been described as
"brain-damaged" — primarily due to the fact that separate processes were specified
as sharing a single stack.


### ETHEL

*   type: Programming Language
*   inception-date: 1998
*   genre: DSL
*   development-stage: lost
*   computational-class: believed Turing-complete
*   paradigms: Functional

ETHEL was a programming language specifically for expressing
quantity surveying (materials estimating) formula and procedures,
designed for Star Building Materials.

#### Implementation: ethel.pl

*   license: Proprietary
*   implementation-type: interpreter
*   host-language: Perl

### REDGREEN

*   type: Automaton
*   inception-date: 1998
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: RUBE
*   paradigms: Cellular automaton

REDGREEN is a cellular automaton that simulates a little
"physical world", much like [RUBE][].

Sample program:

                                       # #
                     ......            # #
                                       #  ~                      #
                                       #######################   #
                                      %#                         #
                           . . .      T #####                    #
                                      ###   #  :                 #
                                            #                    #
                                            #  .                 #
                                            #                    #
                                            #                    #
                                            #  .                 #
                                            #                    #
                                            #                    #
    >>>>>>>>>>>>>>>##<<<<<<<<<<<<<<<<<############################
                                                    %
                                                    T
    

#### Reference Implementation: redgreen.alp

*   license: BSD license
*   implementation-type: formal description
*   host-language: ALPACA

### ALPACA

*   type: Programming Language
*   inception-date: 1998
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: Metalanguage, Object-oriented

ALPACA is a meta-language for describing cellular automata.

Sample program:

    /* John Conway's Game of Life, expressed in ALPACA. */
    state Dead  " " to Alive when 3 Alive and 5 Dead;
    state Alive "*" to Dead when 4 Alive or 7 Dead.
    

#### Reference Implementation: alpaca.pl

*   license: BSD license
*   implementation-type: compiler
*   host-language: Perl
*   target-language: Perl
#### Reference Implementation: alpaca (Python)

*   license: BSD license
*   implementation-type: compiler
*   host-language: Python
*   target-language: Javascript

### Funge-98

*   type: Programming Language Family
*   inception-date: Sep 11, 1998
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: Befunge-93, Befunge-97
*   paradigms: Stack-based, Self-modifying
*   reference-distribution: [Funge-98 distribution](/distribution/Funge-98 distribution)

Funge-98 is a family of programming languages designed as the successor
to [Befunge-93][].  It generalizes Befunge-93's two-dimensional nature
somewhat, defining languages in one dimension ([Unefunge-98][]),
two dimensions ([Befunge-98][]), and three dimensions ([Trefunge-98][]),
and suggests possibilities for other dimensions and topologies (but does
not specify exactly how they look or would behave.)
It also makes the playfield unbounded, allowing the language to be
[Turing-complete][], and tries to define mechanisms for interacting with the
operating system and engaging extensions to the language.

Sample program:

    >>#v?v
    ^,A' <
     ^ C'
        T
     ^ <<
        G
        '
    


### MDPN

*   type: Programming Language
*   inception-date: 1999
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: ???
*   paradigms: Metalanguage
*   reference-distribution: [Specs on Spec distribution](/distribution/Specs on Spec distribution)

MDPN is a meta-language for describing multi-directional and
multi-dimensional languages.

Sample program:

      Box ::= "+" {"-"}^(w) r(-90) "+" "||" {"|"}^(h) r(-90)
              "+" {"-"}^(w) r(-90) "+" "||" {"|"}^(h) r(-90)
    


### Shelta

*   type: Programming Language
*   inception-date: ca Jul 1999
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: Stack-based

Shelta is an extremely minimal Forth-like language with barely
any semantics; it relies on inline machine code to write anything resembling
an actual program in it. In the spirit of compilers for languages such as [FALSE][]
and [brainfuck][], a Shelta-to-8086 compiler was implemented (with help from
[Ben Olmstead][]) in less than 512 bytes of [80286 machine code](x86 machine code). What's more,
it's also been bootstrapped — that is to say, a Shelta compiler was
written in Shelta, which was compiled with the original compiler, and then
compiled again with the resulting compiler, producing a wholly self-hosted
executable!

Sample program:

    [ `Hello, _32 `world! _13 _10 ] \15 outs \0 halt
    

#### Reference Implementation: shelta

*   license: Freely Redistributable
*   implementation-type: compiler
*   host-language: NASM Assembler
*   target-language: x86 machine code
#### Implementation: sheltas

*   license: Freely Redistributable
*   implementation-type: compiler
*   host-language: Shelta
*   target-language: x86 machine code

### Bear Food

*   type: Programming Language
*   inception-date: ca Dec 1999
*   genre: Esolang
*   development-stage: lost
*   computational-class: ???
*   paradigms: Stack-based

Bear Food was a horrible language defined by an interpreter that
evolved (no... let's be honest, it *devolved*) from a small piece of example
code showing how to parse and intepret a simple reverse-polish notation language.
This same example code also took a very divergent line of evolution, eventually
becoming the programming language [Var'aq][].

#### Reference Implementation: bearfood.pl

*   license: Unknown license
*   implementation-type: interpreter
*   host-language: Perl

### Sally

*   type: Programming Language
*   inception-date: 2000
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: Functional

Sally is a cute but naive little functional language with a minimal syntax,
a strict type system, and some unusual rules for parameters and return values.

Sample program:

    stdlib
    int factorial int if $1 mul $1 factorial sub $1 1 1
    int main int factorial $1
    

#### Reference Implementation: sally2c

*   license: BSD license
*   implementation-type: compiler
*   host-language: ANSI C
*   target-language: ANSI C

### ILLGOL

*   type: Programming Language
*   inception-date: ca Apr 2000
*   genre: Joke language
*   development-stage: mature
*   computational-class: ???
*   paradigms: Imperative

ILLGOL is a joke language which parodies the sort of language designed by the
sheer fact that a compiler for it has been hacked together.

Sample program:

    NB eh.ill
    10 *f = { print str(#0), EoL };
    20 do f(1);
    30 don't f;
    40 do f(2);
    50 reinstate f;
    60 do f(3);
    FIN
    

#### Reference Implementation: illgol.exe

*   license: Unknown license
*   implementation-type: compiler
*   host-language: ANSI C
*   target-language: x86 machine code

### SMITH

*   type: Programming Language
*   inception-date: ca Jul 2000
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: SMETANA
*   paradigms: Imperative, Self-modifying

SMITH is a self-modifying assembly-like language which completely lacks
any kind of jump instructions *whatsoever*.  Despite this handicap, it
has been shown to be [Turing-complete][].

Sample program:

    MOV R0, 10
    MOV R2, 0
    SUB R2, 1
    MOV R[R0], "Hello, world!"
    MOV TTY, R[R0]
    SUB R0, R2
    MOV R1, R0
    SUB R1, 23
    NOT R1
    NOT R1
    MUL R1, 8
    COR +1, -7, R1

#### Reference Implementation: smith.pl

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Perl

### Tamerlane

*   type: Programming Language
*   inception-date: Aug 2000
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: Graph-rewriting, Imperative
*   reference-distribution: [Specs on Spec distribution](/distribution/Specs on Spec distribution)

Tamerlane is a multi-paradigmatic programming language, unimplemented
and possibly unimplementable. One of its core execution mechanisms is the
traversing of a graph (representing the program) while rewriting that same
graph.

Sample program:

    Point-A: 1 Point-B,
    Point-B: 1 Point-C,
    Point-C: 1 Point-A.
    ?- 1 Point-A -> 0 Point-A @ Point-A
    


### Squishy2K

*   type: Programming Language
*   inception-date: Sep 2000
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: String-rewriting, State machine

Squishy2K is a language which is a hybrid of string rewriting
and finite state automata; as an added twist, it also lets program states serve
as functions.  It was based largely on an earlier grammar-based language
called SQUISHY, taking also some ideas from the language [Thue][].  The
original SQUISHY was conceived sometime around 1998, but is now lost.  Because
it was based largely on EBNF, the author wanted to name it Wirth, but the
name SQUISHY was proposed and (somewhat unfortunately) stuck.

Sample program:

    * main { start many finish? "Hello, world!"! }
    

#### Reference Implementation: squishy2k.pl

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Perl

### noit o' mnain worb

*   type: Automaton
*   inception-date: Sep 15, 2000
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: Particle automaton, Probabilistic

noit o' mnain worb is a probabilistic particle automaton that
uses pressure between randomly moving particles to approximate the behaviour
of circuits.  It can approximate computation with these circuits, too, but
it's so lossy that it has more value as just a neat toy to watch.

(The name of this language contains a *secret message*! Can *you* find it?)

Sample program:

    #####         #####
    #   ###########   #
    # . >         < . #
    #   #####v#####   #
    #####   #  ########
            #       >!#
            #v#########
            # #
            ###
    

#### Reference Implementation: worb.pl

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Perl
#### Implementation: worb.js

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Javascript
#### Implementation: tc.catseye.yoob.worb

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Java

### HUNTER

*   type: Programming Language
*   inception-date: ca Sep 20, 2000
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: 2-dimensional, Maze-space-rewriting

HUNTER is a language I designed for the Esoteric Awards ("Essies")
Its abstract starts out like this:

> It is perceived that one of the biggest problems in maintaining
> interest in programming is the above linear growth of boredom
> compared to the usefulness of the program, resulting in an
> acute loss of enthusiasm on the part of the programmers and
> ultimately the abandonment of the software...

Sample program:

    ##################
    #   1#2#         #
    # #### #         #
    #      #         #
    # ######    M    #
    #     M#         #
    #+######         #
    #     !#         #
    ##################
    *12+>3
    *21+>3
    

#### Reference Implementation: hunter.pl

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Perl

### 'N-DCNC

*   type: Programming Language
*   inception-date: Oct 2000
*   genre: Joke language
*   development-stage: not fully complete
*   computational-class: ???
*   paradigms: Functional

'N-DCNC was [Chris Pressey][]'s entry for the 2000 [Esoteric Awards][].
It is based on a conspiracy theory involving UFOs and a 5-member
boy band, or something.

Sample program:

    4*5+2/2,(9*`c)+1
    

#### Reference Implementation: ndcnc.pl

*   license: Unknown license
*   implementation-type: compiler
*   host-language: Perl
*   target-language: FALSE
#### Implementation: ndcnc.bf

*   license: Unknown license
*   implementation-type: compiler
*   host-language: Befunge-93
*   target-language: FALSE

### Strelnokoff

*   type: Programming Language
*   inception-date: Apr 2001
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   paradigms: Imperative, Non-deterministic

Strelnokoff is a non-deterministic imperative programming language.
Despite this apparent handicap, it appears to be [Turing-complete][] —
thanks to a short-circuiting multiplication operator — but a critical
feature, namely arrays, has yet to be implemented.

Sample program:

    REM HELLO WORLD IN STRELNOKOFF
    REM CHRIS PRESSEY MARCH 24 2001
    X = (X / X) * X + (X = 0) * (T =  0) * (PRINT CHAR 'H' - 'H' +  1)
    X = (X / X) * X + (X = 0) * (T =  1) * (PRINT CHAR 'e' - 'e' +  2)
    X = (X / X) * X + (X = 0) * (T =  2) * (PRINT CHAR 'l' - 'l' +  3)
    X = (X / X) * X + (X = 0) * (T =  3) * (PRINT CHAR 'l' - 'l' +  4)
    X = (X / X) * X + (X = 0) * (T =  4) * (PRINT CHAR 'o' - 'o' +  5)
    X = (X / X) * X + (X = 0) * (T =  5) * (PRINT CHAR ',' - ',' +  6)
    X = (X / X) * X + (X = 0) * (T =  6) * (PRINT CHAR ' ' - ' ' +  7)
    X = (X / X) * X + (X = 0) * (T =  7) * (PRINT CHAR 'w' - 'w' +  8)
    X = (X / X) * X + (X = 0) * (T =  8) * (PRINT CHAR 'o' - 'o' +  9)
    X = (X / X) * X + (X = 0) * (T =  9) * (PRINT CHAR 'r' - 'r' + 10)
    X = (X / X) * X + (X = 0) * (T = 10) * (PRINT CHAR 'l' - 'l' + 11)
    X = (X / X) * X + (X = 0) * (T = 11) * (PRINT CHAR 'd' - 'd' + 12)
    X = (X / X) * X + (X = 0) * (T = 12) * (PRINT CHAR '!' - '!' + 13)
    X = (T = X) * 0 + (X > T) * X REM RESET FLAG
    T = (X / X) * X + (X = 0) * T REM INCREMENT TICK
    

#### Reference Implementation: strelnokoff.pl

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Perl

### Opus-2

*   type: Conlang
*   inception-date: Jul 2001
*   genre: Abstract Artlang
*   development-stage: not fully complete
*   computational-class: ???
*   reference-distribution: [Specs on Spec distribution](/distribution/Specs on Spec distribution)

Opus-2 is not a programming language, but rather, an abstract artlang
(i.e., a conlang designed independently from any conception of society.)
The sole design principle was to entirely eliminate word order.

Sample program:

    + pale green
    + Eb, trombone, forte
    + leaning 40 degrees left (sudden)
    + C, tubular bells, piano
    + mothballs (gentle whiff)
    


### Ypsilax

*   type: Programming Language
*   inception-date: Aug 2001
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Grid-rewriting, Reflective

Ypsilax is a non-deterministic, reflective, two-dimensional grid-rewriting
language.  Rewriting rules look for patterns in the grid and replace them
with other patterns.  These rules are themselves represented by patterns
in the grid, and therefore rules can match and rewrite other rules.

Sample program:

    (      )  (      )
      #            #
      # ###    ### #
      #            #
    
        ###   ###
    
        #      #
        #      #
        #    ###
    

#### Reference Implementation: ypsilax.pl

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Perl
#### Implementation: tc.catseye.yoob.ypsilax

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Java

### Version

*   type: Programming Language
*   inception-date: Sep 2001
*   genre: Esolang
*   development-stage: mature
*   computational-class: unknown computational class
*   paradigms: Imperative, Regular-expression-based

Version is an imperative programming language that uses _ignorance-spaces_
for flow control; all  instructions which match the current ignorance pattern
are ignored during execution.

Sample program:

    START: ROOM = "VALLEY|BROOK|GLADE"
    CONT: IGNORE = ROOM
    VALLEY: OUTPUT = "You are standing in a valley."
    HILL: OUTPUT = "You are on top of a hill."
    BROOK: OUTPUT = "You are by a brook."
    GLADE: OUTPUT = "You are standing in a sun-dappled glade."
    ROOM: OUTPUT = EOL
    ROOM: DIR = CHOP INPUT
    ROOM: IGNORE = DIR
    ROOM: MASK = "VAPOURS"
    N: CAT = "|N"
    S: CAT = "|S"
    E: CAT = "|E"
    W: CAT = "|W"
    ROOM: IGNORE = MASK
    N: ROOM = "VALLEY|BROOK|GLADE"
    S: ROOM = "HILL|BROOK|GLADE"
    E: ROOM = "VALLEY|HILL|BROOK"
    W: ROOM = "VALLEY|HILL|GLADE"
    LASTLY: IGNORE = "START"
    

#### Reference Implementation: version.pl

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Perl

### beta-Juliet

*   type: Programming Language
*   inception-date: ca 2002
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Event-oriented

beta-Juliet is a minimal event-based language.  Each event is caused by some other event.
Event causation is conditional based on which of two given events occurred more recently.

Portia is a preprocessor for beta-Juliet which allows large, regular, finite sets of events
to be described succinctly.

Version 2.0 of beta-Juliet (formerly known as "2iota") allows infinite sets of events to be
specified, allowing the language to be [Turing-complete][].

Sample program:

    event WindowSwitchBroken;
    event MotionDetectorTriggered;
    
    event SystemArmed;
    event SystemDisarmed;
    
    event Alarm,
     caused after WindowSwitchBroken      when SystemArmed > SystemDisarmed,
     caused after MotionDetectorTriggered when SystemArmed > SystemDisarmed,
     causes Alarm.
     
    alphabet Domino,
            One, Two, Three, Four, Five, Six, Seven;
    event Begin,
            causes Domino One Falls;
    event Domino (N = Domino+) Falls,
            causes Domino (succ N) Falls.
    

#### Reference Implementation: 2iota

*   license: BSD license
*   implementation-type: interpreter
*   host-language: C99
#### Implementation: b_juliet.pl

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Perl

### Sbeezg

*   type: Programming Language
*   inception-date: 2002
*   genre: Esolang
*   development-stage: archival
*   computational-class: ???
*   paradigms: Functional

Sbeezg is a syntactically very simple language that attempts to
take the single-assignment concept to a logical extreme.

Sample program:

    f={a,b|i=*is;s=*pred;p=*print;g=p(*beer);h=s(a);
       ln={x,m|z=x|x};lg={y,n|q=n(y,n)|y};j=i(h,0,ln,lg);
       k=j(h,b)|a};l=f(99,f)
    

#### Reference Implementation: sbeezg.erl

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Erlang

### GraNoLa/M

*   type: Programming Language
*   inception-date: Jul 2002
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   influences: Tamerlane
*   paradigms: Graph-rewriting, Imperative

GraNoLa/M is a Graph-Node-based Language (possibly for Machines.) 
It was one of my submissions for the Esoteric Awards. Not unlike [Tamerlane][],
its execution model involves both traversing and rewriting a graph at the
same time.

Sample program:

    a=^sajalom(b=^#d(c=^bimodang(^a))d(e=^#cthulhu(f=^uwaming(g=^ubewic()))))
    

#### Reference Implementation: granolam.erl

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Erlang

### Kangaroo Iceberg

*   type: Programming Language
*   inception-date: Jul 2004
*   genre: Esolang
*   development-stage: unfinished
*   computational-class: ???
*   influences: Tamerlane
*   paradigms: Graph-rewriting

Kangaroo Iceberg was a short-lived attempt to pare down [Tamerlane][]
to something implementable, and implement it.  Although it got a fair ways
along (e.g. the parser for graphs seems to be complete, I lost interest
in it at the time, and put off finishing it indefinitely.

Now, the challenge will be reconstructing the language from the partial
implementation and notes that I left behind...

Sample program:

    A { ^A:0 / ^A:0 -> ^A:1 }
    B { / ^B:0 -> ^B:1, ^B:1 -> ^B:2 }
    C { {}:0 / ^K:0 -> ^K:1, ^K:1 -> ^K:2; ^A:1 -> ^A:0 }
    

#### Reference Implementation: kiceberg

*   license: BSD license
*   implementation-type: interpreter
*   host-language: ANSI C

### Circute

*   type: Automaton
*   inception-date: 2005
*   genre: Esolang
*   development-stage: mature
*   computational-class: known not Turing-complete
*   influences: Wireworld
*   paradigms: Cellular automaton

Circute is a cellular automaton that simulates conduits that
carry digital signals and NAND gates that manipulate those signals.

Sample program:

                      =
                      =
       #######==   ===N===   =========
       #       =   =     =   =       =
     ==N==     = ==N== ==N== =     ==N==
     =   =     = =   = =   = =     =   =
     =====     = ===== ===== =     =====
       =       =   =     =   =       =
       =============     =============
    

#### Reference Implementation: circute.alp

*   license: BSD license
*   implementation-type: formal description
*   host-language: ALPACA
#### Implementation: tc.catseye.yoob.circute

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Java

### Braktif

*   type: Automaton
*   inception-date: 2005
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   influences: brainfuck
*   paradigms: Cellular automaton

Braktif is a cellular automaton modelled closely after the [brainfuck][]
programming language.

Sample program:

                                *
                           <<*[--]*
    000000000000000000  *[-----  --]
    -----------------d-i--         --------
    

#### Reference Implementation: braktif.alp

*   license: BSD license
*   implementation-type: formal description
*   host-language: ALPACA

### Beturing

*   type: Programming Language
*   inception-date: Oct 20, 2005
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: Befunge-93
*   paradigms: Imperative, State machine

Beturing is a "[Befunge](Befunge-93)-flavoured" language for describing Turing
machines; both the tape and the finite control are laid out two-dimensionally.
In addition, the finite control must be expressed as a planar graph (no
edge representing a transition may cross any other edge.) It was devised
this way as a test of the so-called "wire-crossing problem". It turns out
that there are universal Turing machines with finite controls that are planar
graphs, so Beturing is [Turing-complete][].

Sample program:

    # D(40, 4)
    # @(40, 4)
    $bbab$
    # C(0, 0)
    # @(0, 0)
     . . . . . .
    *v*<*<*<*>*v
    aa .ab . .aa .
    >/*>./*^*^</*v
    bb .ba . .bb .
    >/*^./*^*^</*v
    $$ .$$ . .$$ .
    >/*^</*>*^.@*v
             . . .
    *@      *^*<*<
    

#### Reference Implementation: beturing.lua

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Lua

### Bhuna

*   type: Programming Language
*   inception-date: Oct 21, 2005
*   genre: Production language
*   development-stage: archival
*   computational-class: believed Turing-complete
*   influences: Lua
*   paradigms: Imperative, Functional

Bhuna is a small, garbage-collected language with a simple syntax,
[closures](Closure), inferred types, lightweight processes, and support for UTF-8 source
code.  It was implemented partly to see how closely I could match the performance
of [Lua][]'s interpreter.  It was meant more more as an experimental starting
point for branching new languages, than as a useful language in and of itself.

Sample program:

    Fib = ^ X {
      if X < 2 return 1 else
      return Fib(X - 1) + Fib(X - 2)
    }
    Print Fib(32), EoL
    

#### Reference Implementation: bhuna

*   license: BSD license
*   implementation-type: interpreter
*   host-language: C99

### Burro

*   type: Programming Language
*   inception-date: 2007
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: Turing-complete
*   influences: brainfuck
*   paradigms: Imperative, Algebraic

Burro is a [brainfuck][]-like programming language whose programs
form an algebraical _group_ (modulo the equivalence relation of "computes the
same function") under the operation of concatenation. The upshot of this
is that, for every Burro program, we can find an _antiprogram_ which, when
appended to the program, forms a "no-op" program which has no effect.
 This is a form of reversible computing, but unlike most reversible languages
where it is the execution of the program that is "undone", in Burro, it is
the program itself which is annihiliated by its antiprogram.  Burro 1.0
was released in fall of 2007, but proved not to form a proper group. This
shortcoming was rectified in summer of 2010.

Sample program:

    !--(--(--(!>/
      >>--(+<<+++++++>/+++>+++++>)<
    >)/
      >>--(+++>+++++>/+++<<<<<+++>)<
    >)/
      >>--(+++>+>/+<<+++>)<
    >)<
    

#### Reference Implementation: Burro.lhs

*   license: Unknown license
*   implementation-type: interpreter
*   host-language: Haskell

### Xigxag

*   type: Automaton
*   inception-date: Apr 23, 2007
*   genre: Esolang
*   development-stage: mature
*   computational-class: unknown computational class
*   paradigms: String-rewriting

Xigxag is a simple string-copying automaton that has exponential
growth almost everywhere (i.e. there are only a finite number of initial
configurations that don't blow up.)

Sample program:

    ><<
    

#### Reference Implementation: xigxag.pl

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Perl

### Hev

*   type: Programming Language
*   inception-date: May 23, 2007
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Term-rewriting

Hev is a programming language that attempts to solve the "central
problem of infix notation": how do you allow it without requiring the programmer
to either memorize precedence tables or litter parentheses everywhere?  Hev
has a way! In Hev, *all* operators are infix, yet no tiresome memorization
of any dreadful precedence table is required!

Sample program:

    71+8*27,19,29*99,6,37,7,61,47
    

#### Reference Implementation: Hev.hs

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Haskell

### Cabra

*   type: Programming Language
*   inception-date: Oct 30, 2007
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: known not Turing-complete
*   influences: Burro
*   paradigms: Imperative, Algebraic

Cabra is a (somewhat) formal programming language whose programs
form an algebraical _dioid_ (an idempotent semiring), modulo the equivalence
relation of "computes the same function", under the operations of parallel
execution (as the additive operator) and sequential composition (as the multiplicative
operator).

Sample program:

    (SET 1 + SET 2) * IFSET 1 THEN (IFSET 2 THEN SET 3 ELSE SKIP) ELSE SKIP
    

#### Reference Implementation: cabra.hs

*   license: Unknown license
*   implementation-type: interpreter
*   host-language: Haskell

### You are Reading the Name of this Esolang

*   type: Programming Language
*   inception-date: Nov 2007
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: Spoon
*   paradigms: Imperative
*   reference-distribution: [Specs on Spec distribution](/distribution/Specs on Spec distribution)

You are Reading the Name of this Esolang is an exploration in
the design space of programming languages with undecidable elements. Its syntax
is only recursively enumerable: the problem of determining whether or not
a given string of symbols is a well-formed You are Reading the Name of this
Esolang program is undecidable.

Sample program:

    001000000[0010000000111001000011]11100100001[0]
    


### Emmental

*   type: Programming Language
*   inception-date: Nov 11, 2007
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Meta-circular, Reflective

Emmental is a self-modifying programming language.  It is defined
in terms of a meta-circular interpreter, and this meta-circular interpreter
provides an operation that redefines operations of the meta-circular interpreter.
In fact, this mechanism is required for Emmental to be [Turing-complete][].

Sample program:

    ;#58#126#63#36!;#46#36#!;#0#1!;#0#2!;#0#3!;#0#4!;#0#5!;#0#6!;#0#7!#0#33#111#108#108#101#72$
    

#### Reference Implementation: emmental.hs

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Haskell

### Didigm

*   type: Automaton
*   inception-date: Nov 20, 2007
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: ???
*   paradigms: Cellular automaton, Reflective
*   reference-distribution: [Specs on Spec distribution](/distribution/Specs on Spec distribution)

Didigm is a reflective cellular automaton: the transition rules
for the automaton are defined by forms in the very playfield governed by
those transition rules.

Sample program:

    3333333333333
    3002300230073
    3111311132113
    3311321131573
    3111311131333
    3333333333333
    =F3
    ,
    =F1
    111111111111111
    111111131111111
    111111111111574
    111111111111333
    311111111111023
    111111111111113
    


### Iphigeneia

*   type: Programming Language
*   inception-date: Nov 25, 2007
*   genre: Pedagogical language
*   development-stage: mature
*   computational-class: ???
*   paradigms: Imperative, Functional

Iphigeneia is a toy programming language which contains features
from both imperative programming (assignments to mutable variables, `while`
loops,) and functional programming (immutable name bindings, Scheme-style
"named `let`" loops.) It was originally intended as a testbed for algorithms
that convert programs between the two forms.

Sample program:

    var a in a :=
        let c = 5 in let d = 1 in
            loop
                if c = 0 then
                    d
                else
                    let d = d * c in
                        let c = c - 1 in
                            repeat

#### Reference Implementation: iphi

*   license: Unknown license
*   implementation-type: interpreter
*   host-language: Haskell

### Mascarpone

*   type: Programming Language
*   inception-date: Dec 10, 2007
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   influences: Emmental
*   paradigms: Meta-circular, Reflective

Mascarpone is a self-modifying language able to alter the meta-circular
interpreter which defines it, like its predecessor [Emmental][].  Unlike Emmental
however, in Mascarpone interpreters are first-class objects, making the
job of reflective interpreter-modification quite a bit cleaner and richer.

Sample program:

    v['[/''/']v*]v*'?<^v[/?/<]v*'S<[>!]v*'F<^[]v*1'p'kS'kF.
    

#### Reference Implementation: mascarpone.hs

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Haskell

### Larabee

*   type: Programming Language
*   inception-date: Jan 10, 2008
*   genre: Esolang
*   development-stage: mature
*   computational-class: known not Turing-complete
*   paradigms: Imperative

Larabee is an assembly-like programming language, with [Scheme][]-like
syntax, that borrows the notion of branch prediction from computer architecture
and abuses it, creating a path that leads only to existential angst and self-destruction.

Sample program:

    (store (input) (input)
      (store (input) (input)
        (label loop
          (store (input) (op * (fetch (input)) (fetch (input)))
            (store (input) (op - (fetch (input)) (input))
              (test (op > (fetch (input)) (input))
                (goto loop) (print (fetch (input)))))))))

#### Reference Implementation: larabee.scm

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Scheme

### Arboretuum

*   type: Programming Language
*   inception-date: Mar 2008
*   genre: Experimental language
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Forest-rewriting

Arboretuum is an experimental language based on _forest-rewriting_,
a variant of tree-rewriting in which multiple trees are rewritten simultaneously.
The language was intended for specifying compilers, with each tree representing
a major compiler data structure (AST, symbol table, output buffer, etc.,)
however, this idea was not entirely successful.  Regardless, Arboretuum is
[Turing-complete][], as tree-rewriting is simply a special case of forest-rewriting.

Sample program:

    (
      (
        (ast:   (let a 4 (+ 3 (* a 3))) )
        (stab:  eot)
        (out:   halt)
      )
      (
        ((ast:  (let #(n sym) #(v) #(expr)) => #(expr)            )
         (stab: eot                         => (#(n) #(v) EOT)    ))
        ((ast:  #(n sym)                    => #(v)               )
         (stab: (#(n) #(v) #(tab))          => (#(n) #(v) #(tab)) ))
        ((ast: #(a num)                     => _                  )
         (out: halt                         => (push #(a) halt)   ))
        ((ast: (+ _ _)                      => _                  )
         (out: halt                         => (add halt)         ))
        ((ast: (* _ _)                      => _                  )
         (out: halt                         => (mul halt)         ))
      )
    )

#### Reference Implementation: forest-rewriter.scm

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Scheme

### Treacle

*   type: Programming Language
*   inception-date: Apr 12, 2008
*   genre: Experimental language
*   development-stage: mature
*   computational-class: believed Turing-complete
*   influences: Arboretuum
*   paradigms: Term-rewriting

Treacle is an experimental compiler-definition language based on
_context rewriting_, an expressive variant of term rewriting that generalizes
the forest-rewriting used by its predecessor [Arboretuum][].  In context rewriting,
a separation is made between _names_ and _variables_, and patterns may contain
_holes_ inside which subpatterns may match at any depth.

Sample program:

    (
      (:i (? t (x (? i *) (? j *)))) -> (t : (xx (? j *) (? i *)))))
      (:i (? p right))               -> (p : left)
    )
    

#### Reference Implementation: treacle.scm

*   license: Unknown license
*   implementation-type: interpreter
*   host-language: Scheme

### Quylthulg

*   type: Programming Language
*   inception-date: Dec 6, 2008
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Functional

Quylthulg is a programming language with but a single control-flow
construct: `foreach`.  In fact, it does also have a `goto`, but that can
only appear inside data structures.

Sample program:

    foreach $n$=:L:[1,2,3|goto$L$] with $a$=1 be +$a$+$n$+ else be abort

#### Reference Implementation: Qlzqqlzuup, the Lord of Flesh

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Haskell

### Unlikely

*   type: Programming Language
*   inception-date: Mar 15, 2009
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   paradigms: Continuation-passing, Object-oriented, Dependency injection

Unlikely is a programming language that conflates objects with
continuations, and methods with labels.  It exposes program structures as
objects with commensurate inheritance relationships.  It also takes dependency
injection to the logical extreme: if some class is used by an object, that
class *must* be specified when the object is instantiated.

Sample program:

    class Count(Count,Chain,Print,Add) extends Continuation
    
    class CountForever(Count,Chain,Print,Add) extends Program {
      Count c;
      method continue(Passive accumulator) {
        c = new Count(Passive,Count,Chain,Print,Add);
        goto c.continue(new 1(Passive));
      }
    }
    
    class Count() extends Continuation {
      Count c;
      Print p;
      Add a;
      method continue(Passive accumulator) {
        c = new Count(Passive,Count,Chain,Print,Add);
        a = new Add(Passive,Chain);
        a.value = new 1(Passive);
        a.next = c;
        p = new Print(Passive,Chain);
        p.next = a;
        goto p.continue(accumulator);
      }
    }

#### Reference Implementation: Coldwater

*   license: BSD license
*   implementation-type: static analyzer
*   host-language: Python

### Jaccia

*   type: Automaton
*   inception-date: Apr 11, 2009
*   genre: Esolang
*   development-stage: mature
*   computational-class: known not Turing-complete
*   paradigms: Cellular automaton, 2-dimensional

Jaccia and Jacciata are cellular automata inspired by the [Announcement
of Scientific Proof that Slime Molds are Intelligent Maze Solvers](http://web.archive.org/web/20020220163303/http://www.riken.go.jp/lab-www/frontier-div/NEWSLETTER/feb2001/ameboid_e.htm).
Jaccia can solve mazes too, by a similar mechanism (shrinking). Jacciata builds
upon this to find the shortest path through a maze, if one exists and is unique.

Sample program:

    #######S###
    #:::::::::#
    #:###:###:#
    #:#:#:::#:#
    #:#:#:#:###
    #:::#:#:#:#
    #####:#:#:#
    #:#:::#:::#
    #:#:###:###
    #:::#:::::#
    #########F#
    

#### Reference Implementation: jaccia.alp

*   license: BSD license
*   implementation-type: formal description
*   host-language: ALPACA

### Pixley

*   type: Programming Language
*   inception-date: May 2009
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Functional

Pixley is a very small subset of R5RS Scheme (or, if you prefer, R4RS
Scheme), supporting only four datatypes (boolean, cons cell, function, and
symbol) and only a dozen built-in symbols.  The reference implementation of
Pixley is written in 124 lines of Pixley (or, if you prefer, 124 lines of
Scheme; and if you prefer more Scheme-ly metrics, it consists of 413
instances of 54 unique symbols in 684 cons cells.)

Sample program:

    (let* ((a (lambda (x y) (cons x y)))) (a (quote foo) (quote ())))
    

#### Reference Implementation: pixley.pifx

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Pifxley
#### Reference Implementation: mignon

*   license: BSD license
*   implementation-type: interpreter
*   host-language: ANSI C
#### Reference Implementation: pixley.pix

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Pixley
#### Reference Implementation: p-normal.pix

*   license: BSD license
*   implementation-type: compiler
*   host-language: Pixley
*   target-language: P-Normal Pixley
#### Reference Implementation: haney

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Haskell
#### Reference Implementation: pixley.js

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Javascript

### Dieter

*   type: Programming Language
*   inception-date: ca Oct 3, 2009
*   genre: Experimental language
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   paradigms: Object-oriented

Dieter (as in the German masculine given name Dieter, not dieter as in
"one who diets") is a little experimental programming language that
conflates *type qualifiers* with *modules* to produce something
reminiscent of object-orientation.  It demonstrates another way of
thinking about objects, or rather, classes: not so much as
*aggregates of data* as *associations of predicates*.

Dieter was intended as a way to make Hungarian notation part of the type
system, and thus automatically checkable.  However, it also suggests
possible ways of dealing with the problems of aliasing — that is,
determining if two pointers cannot possibly point to the same data, for
safety and optimization considerations.

Sample program:

    module beefy
      procedure beef_up(x: ♥t): beefy ♥t
      begin
        return (bestow beefy x)
      end
    end.

#### Reference Implementation: dieter.py

*   license: BSD license
*   implementation-type: typechecker
*   host-language: Python

### Etcha

*   type: Programming Language
*   inception-date: Oct 4, 2009
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   influences: BitChanger
*   paradigms: Imperative

Etcha is a two-dimensional descendant of [Jeffry Johnston][]'s [BitChanger][].
Like BitChanger, it has four instructions; unlike BitChanger, its storage
model is based on turtle graphics, which permits it to be immediately used
for an alternative purpose: graphical composition. Unlike the turtle in LOGO
however, the turtle in Etcha is an integral part of the computation, playing
a role similar to the tape head of a Turing machine.

Sample program:

    >+++>+++>+++>+++>[+]>>>>+

#### Reference Implementation: tc.catseye.etcha

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Java
#### Implementation: tc.catseye.yoob.etcha

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Java
#### Implementation: etcha.js

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Javascript

### ZOWIE

*   type: Programming Language
*   inception-date: Dec 29, 2009
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: BitChanger
*   paradigms: Imperative, Memory-mapped

ZOWIE is a machine-like language in which all operations *including
structured control flow* are memory-mapped.  Control flow is structured in
the sense of structured programming — the programmer never deals with
`goto`s, or offsets or labels of any kind.  Instead, the program writes to
a memory location to mark the beginning or end of a loop or conditional.

Sample program:

    MOV R10, 90
    MOV R1, R1
    MOV R0, R10
    MOV R8, R10
    MOV R5, 1
    MOV R10, R8
    MOV R8, R10
    MOV R5, 64
    MOV R3, R8
    

#### Reference Implementation: zowie.py

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Python

### Okapi

*   type: Programming Language
*   inception-date: May 23, 2010
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   paradigms: Imperative

Okapi is a language I designed as an anniversary present for my
wife(!). In it, the only means of control flow is throwing exceptions, and
as if this wasn't enough, there are two restrictions on exceptions that are
thrown — they must be divide-by-zero exceptions, and they must be caught
in a lexically enclosing block.  Nor is there any facility to "retry" after
an exception is caught. The language is nonetheless [Turing-complete][].

#### Reference Implementation: okapi.py

*   license: Proprietary
*   implementation-type: interpreter
*   host-language: Python

### Whothm

*   type: Programming Language
*   inception-date: Jun 28, 2010
*   genre: Esolang
*   development-stage: mature
*   computational-class: known not Turing-complete
*   paradigms: Imperative

Whothm is a simple language for describing infinite two-colour
bitmapped drawings.

Sample program:

    r := (0, 0, 1, 2);
    s := (0, 0, 1, 2);
    XOR := TF/FT;
    
    begin
    r.x += r.w;
    r.x += -1;
    r.w += 1;
    r.h += 1;
    draw r, XOR;
    s.x += s.w;
    s.x += -1;
    s.w += 1;
    s.h += 2;
    draw s, XOR;
    end
    

#### Reference Implementation: tc.catseye.whothm

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Java

### Eightebed

*   type: Programming Language
*   inception-date: ca Sep 1, 2010
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Imperative

Eightebed is a small language with explicit `malloc` and `free`.
Through a modicum of static analysis
and runtime support, Eightebed is "safe": it is not possible to dereference a dangling
pointer or otherwise incorrectly-populated memory.

Eightebed was designed as a counter-example to [Gregor Richards][]' claim that such
a language would either need a garbage collector, or not actually implement `free`.
Eightebed has a real `free` and has no garbage collector.

Sample program:

    type node struct {
        int value;
        ptr to node next;
    };
    var ptr to node jim;
    var ptr to node george;
    {    
        jim = malloc node;
        if valid jim {
            [@jim].value = (1 + 4);
            george = jim;
        }
        if valid george {
            print [@george].value;
        }
        free george;
        free jim;
    }

#### Reference Implementation: 8ebed2c.py

*   license: BSD license
*   implementation-type: compiler
*   host-language: Python
*   target-language: ANSI C

### Oozlybub and Murphy

*   type: Programming Language
*   inception-date: Dec 2010
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: ???
*   paradigms: Imperative
*   reference-distribution: [Specs on Spec distribution](/distribution/Specs on Spec distribution)

The name of this language is Oozlybub and Murphy. Despite appearances,
this name refers to a single language. The majority of the language is named
Oozlybub. The fact that the language is not entirely named Oozlybub is named
Murphy. Deal with it.  For the sake of providing an "olde tyme esoterickal
de-sign", the language combines several unusual features, including multiple
interleaved parse streams, infinitely long variable names, gratuitously strong
typing, and only-conjectural Turing completeness.

Sample program:

    VARIABLES ARE p /p*/, p /q*/.
    dynast(3) <->
      (. do (. if? not? exists/dynast 5 ,then
           create/countably/many/dynasts #myself#, 5 .) .) ,then
      (. for each prime /p*|p/ below #myself#+2 do
           for each prime /q*|q/ below /p*|pp/+1 do
             if? not? exists/dynast /p*|p|p/+/q*|q|q/ ,then
               copy/dynast #myself#, /p*|ppp/, /q*|qqq/ .)
    


### Gemooy

*   type: Programming Language
*   inception-date: Dec 2, 2010
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: 2-ill, Etcha
*   paradigms: Imperative

Gemooy is a 2-dimensional esolang with 3 instructions (5 initial symbols)
which combines features from [2-ill][] and [Etcha][], and adds
self-modification.  It came about when the author noticed the tape-related
semantics of 2-ill were essentially the same as those of [BitChanger][].

Sample program:

    %### # ###   # #   ### # ###   # #   ### # ###@
    
       @    @#         @
      @      @          @
     @@
    @                   @
        $         @# # @
                 #      @
                #
           @   @
                        @
             
           @
          #
         #
        @
        @    @
         @# @
    @        @
             @
      @     @#@

#### Implementation: tc.catseye.yoob.gemooy

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Java
#### Implementation: gemooy.js

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Javascript

### Nhohnhehr

*   type: Programming Language
*   inception-date: Dec 8, 2010
*   genre: Esolang
*   development-stage: mature
*   computational-class: can simulate some push-down automata
*   paradigms: 2-dimensional

Nhohnhehr is a remotely fungeoid language which explores the design
space between having a fixed playfield versus an expandable one.  When the
instruction pointer reaches the edge of the playfield (the "room"), whether
it wraps around or creates a new room and adjoins it to that edge, depends
on the current _edge mode_ of the program.  New copies of rooms may be rotated
before being adjoined to existing rooms, but rooms are otherwise immutable.

Sample program:

    +------+
    |    /}|
    |&#/$?@|
    |  / \&|
    |      |
    | {    |
    |\\    |
    +------+
    

#### Reference Implementation: nhohnhehr.py

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Python

### Kelxquoia

*   type: Programming Language
*   inception-date: Dec 23, 2010
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   paradigms: 2-dimensional, Grid-rewriting, Self-modifying
*   reference-distribution: [Kelxquoia distribution](/distribution/Kelxquoia distribution)

Kelxquoia is another remotely fungeoid language, this one self-modifying
— in fact, self-destroying.  As instructions are executed, they are
erased.  In order to execute indefinitely, new instructions of some sort
must be created. Luckily the language provides as its main data-manipulation
facility, grid-rewriting, which can be used to restore instructions that
were previously erased after execution.

Sample program:

     >+-0 0*+-1*/+-?*-R*- *+-?*-R*-?*/v
     RRRRRRRRRRRRRRRRRRRR RRRRRRRRRRRRR
    $>+-0 0*+-1*/+-?*-R*- *+-?*-R*-?*/v
        ' '   '       '  '      '   
                 '         '  '     
     ^      /*?-*P-*?-+*?-*P-* -+     <
     P      PPPPPPPPPPPPPPPPPP PP     P
     ^      /*?-*P-*?-+*?-*P-* -+     <
    
     00 00 00 00
    


### Wunnel

*   type: Programming Language
*   inception-date: Feb 13, 2011
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   influences: 1L, reMorse
*   paradigms: Turning tarpit

Wunnel is a two-dimensional language which draws from the [1L][]
family of languages and incorporates features from [reMorse][]. The name
is both a play on the pronunciation of "1L", and a recursive portmanteau
of the words _Wunnel_ and _tunnel_ which is used to describe the long sequences
of identical instructions (often nops) used in Wunnel programs to sync up
remote parts of the program.

Sample program:

              o   ooo  o
    
    
    o
    o
    o
    o         o
    o         o
    o         o
    o         o
    o
    o        o     o
    o         o
    o
    o        o
    o              o
    o        o     o
    o              o
    
             o
    o oooooooo     o
             o
             o
             o
    
             o    oooo o
    

#### Reference Implementation: tc.catseye.yoob.wunnel

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Java
#### Implementation: wunnel.js

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Javascript

### Pail

*   type: Programming Language
*   inception-date: May 25, 2011
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   influences: Pixley
*   paradigms: Functional

Pail is a programming language based on pairs; just as Lisp stands
for LISt Processing, Pail stands for PAIr Language. Its original working
title was "Bizaaro[sic]-Pixley", as it attempts to resemble [Pixley][]
while turning several concepts on their heads: use pairs instead of lists,
quote by default instead of eval by default, and allow not just values but also
names of bindings to be expressed.

Sample program:

    **[*let [
         [cadrg *[#fst ##*[#snd #g]]]
         **[*let [
              [g [x [y z]]]
              ***cadrg
           ]]
      ]]
    

#### Reference Implementation: Pail.lhs

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Haskell

### Xoomonk

*   type: Programming Language
*   inception-date: Aug 7, 2011
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Imperative, Lazy

Xoomonk is a programming language in which _malingering updatable
stores_ are first-class objects.  Malingering updatable stores unify several
language constructs, including procedure activations, named parameters, and
object-like data structures.

The Xoomonk project was also an experiment in _test-driven language design_.
The specification is largely composed of a number of example programs in
the format of [Falderal][] tests, which were written while the language was
being designed.  These were used to compare the reference implementation,
while it was being developed, against the spec.

Sample program:

    l := $loop*
    counter := 5
    l.do := {
      y := x
      print ^.counter
      o := $sub*
      o.x := ^.counter
      o.y := 1
      ^.counter := o.result
      continue := o.result
    }
    

#### Reference Implementation: xoomonk.py

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Python

### Flobnar

*   type: Programming Language
*   inception-date: Oct 28, 2011
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   influences: Befunge-93
*   paradigms: Functional, 2-dimensional

One day in September of 2011 — though I'm not sure precisely
which one — marked [Befunge-93][]'s 18th birthday.  That means that
Befunge is now old enough to drink in its native land of Canada.  To celebrate
this, I thought I'd get Befunge-93 drunk to see what would happen.  What
happened was Flobnar, an esolang which is in many respects a functional dual
of Befunge-93; most of the symbols have analogous meanings, but execution
proceeds in a much more dataflow-like fashion.

Sample program:

    >     v
    ^\ <   
           
    :v    v   \<@
    -<      : 6
    1 :   > *
      -|    <
      11

#### Reference Implementation: Flobnar.hs

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Haskell

### Madison

*   type: Programming Language
*   inception-date: Dec 2, 2011
*   genre: DSL
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   paradigms: Proof checking, Term-rewriting
*   reference-distribution: [Specs on Spec distribution](/distribution/Specs on Spec distribution)

Madison is a language in which one can state proofs of properties
of term-rewriting systems.  Classical methods of automated reasoning,
such as resolution, are not used; indeed, term-rewriting itself is
used to check the proofs.  Both direct proof and proof by induction
are supported.  Induction in a proof must be across a structure which
has a well-founded inductive definition.  Such structures can be thought
of as types, although this is largely nominal; the traditional typelessness
of term-rewiting systems is largely retained.

Sample program:

    type tree is
      tree(leaf)        -> true
      tree(branch(X,Y)) -> and(tree(X),tree(Y))
    in let
      reflect(leaf)        -> leaf
      reflect(branch(A,B)) -> branch(reflect(B),reflect(A))
    in theorem
      forall X where tree(X)
        reflect(reflect(X)) ~> X
    proof
      case X = leaf
        reflect(reflect(leaf))
        -> reflect(leaf)        [by reflect.1]
        -> leaf                 [by reflect.1]
      case X = branch(S, T)
        reflect(reflect(branch(S, T)))
        -> reflect(branch(reflect(T),reflect(S)))          [by reflect.2]
        -> branch(reflect(reflect(S)),reflect(reflect(T))) [by reflect.2]
        -> branch(S,reflect(reflect(T)))                   [by IH]
        -> branch(S,T)                                     [by IH]
    qed
    


### Troupe

*   type: Programming Language
*   inception-date: Jun 25, 2012
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   paradigms: Imperative, State machine
*   reference-distribution: [Troupe distribution](/distribution/Troupe distribution)

Troupe is an esolang based on hedgehogs, faery rings, and hills.  It maps
fairly neatly to the definition of a Turing machine, so it is almost certainly
[Turing-complete][].


### Exanoke

*   type: Programming Language
*   inception-date: ca Jul 2012
*   genre: Experimental language
*   development-stage: mature
*   computational-class: Primitive recursive
*   paradigms: Functional

Exanoke is a functional language which is syntactically restricted to
expressing the primitive recursive functions.

Sample program:

    def inc(#)
      cons(:one, #)
    def add(#, other)
      if eq?(#, :nil) then other else self(<tail #, inc(other))
    def mul(#, other)
      if eq?(#, :nil) then :nil else
        add(other, self(<tail #, other))
    def fact(#)
      if eq?(#, :nil) then cons(:one, :nil) else
        mul(#, self(<tail #))
    def four(#)
      cons(:one, cons(:one, cons(:one, cons(:one, #))))
    fact(four(:nil))
    

#### Reference Implementation: exanoke.py

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Python

### Velo

*   type: Programming Language
*   inception-date: Jul 2012
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   influences: Ruby
*   paradigms: Object-oriented

Velo is a vaguely [Ruby][]-inspired "scripting" language which unifies
strings with code blocks, and scripts with object classes.  Curly braces
delimit string literals, and there is no difference between a string literal
and a block of code given to, say, an `if` statement.  Any given script is
an object, which inherits from the root object in delegation-OO style.

Sample program:

    yes = {IO.print {Yes}}
    no = {IO.print {No}}
    if ({X}.equals {Y}), yes, no

#### Reference Implementation: velo.rb

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Ruby
#### Implementation: velo.lua

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Lua

### Cfluviurrh

*   type: Programming Language
*   inception-date: Aug 26, 2012
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Imperative

Cfluviurrh is, as far as I am aware, the first programming language designed
for writing programs that can *feel*. Cfluviurrh defines a mechanism by which a
program can be instructed to experience particular emotions.

You might, thus, on first blush, consider Cfluviurrh to be unimplementable,
as modern-day computers are not capable of experiencing emotions (you guess.)
However, this is demonstrably untrue.  The reference interpreter demonstrates it.

Sample program:

    (print ASCII table while experiencing a bewildering array of emotions)
    a=8
    a*=8
    b=a
    b+=a
    b-=2
    :X
    a+=1
    a>
    z@=X
    z?a<b
    

#### Reference Implementation: cfluviurrh

*   license: BSD license
*   implementation-type: interpreter
*   host-language: ANSI C

### Jolverine

*   type: Programming Language
*   inception-date: Sep 10, 2012
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: Wunnel, Half-Broken Car in Heavy Traffic
*   paradigms: Turning tarpit, 2-dimensional

The Jolverine language was devised as a conscious attempt to expand the
genre of turning tarpit by adding the feature of modifying the instruction
wheel during execution.

Sample program:

    --*-*
         \
          \
           \           *
            \         /
             \       /
              \     /
               *   /
                \ /
                 *-*---*
    

#### Reference Implementation: jolverine.py

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Python

### SICKBAY

*   type: Programming Language
*   inception-date: Sep 22, 2012
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   paradigms: Imperative

SICKBAY is an esoteric dialect of [BASIC][] with a call ring buffer instead of
a call stack, and computed line number definitions (and no `IF` because
of that.)

Sample program:

    10 LET B% = 99
    (100+B%) END
    100 GOTO 200:REM BEGIN LOOP
    200 PRINT B%;:PRINT " BOTTLES OF BEER ON THE WALL,"
    205 PRINT B%;:PRINT " BOTTLES OF BEER,"
    210 PRINT "TAKE ONE DOWN, PASS IT AROUND,"
    215 LET B% = (B% - 1)
    220 PRINT B%;:PRINT " BOTTLES OF BEER ON THE WALL.":PRINT ""
    230 GOTO 100

#### Reference Implementation: SAWBONES

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Python

### Carriage

*   type: Programming Language
*   inception-date: Nov 2012
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: unknown computational class
*   influences: 
*   paradigms: Concatenative

Carriage is the result of various, not-entirely-successful attempts to
design a "pure" concatenative language — one in which the program
texts are monoids and nothing but monoids (no quoting operators or
the like.)  The result was midly unusual — subroutines are specified
by indices into an area of the stack which contains program symbols,
thus may overlap — and was released as an esolang.

Sample program:

    111-@11-~!$11111++++11-~@11-~!
    

#### Reference Implementation: Carriage.hs

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Haskell

### Chzrxl

*   type: Automaton
*   inception-date: 2013
*   genre: Toy
*   development-stage: mature
*   computational-class: ???
*   paradigms: Angular, Particle automaton
*   reference-distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)

"Chzrxl, the Living Inkblot."  Or is it a sort of self-attracting
lava lamp?

#### Implementation: chzrxl.js

*   license: Public Domain
*   implementation-type: ???
*   host-language: Javascript

### Yolk

*   type: Programming Language
*   inception-date: Aug 24, 2014
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   paradigms: Functional

Yolk is a tiny S-expression-based programming language (or computational
calculus) with a tiny meta-circular interpreter.

Sample program:

    (ifeq (head arg) (quote arg)
        (head (tail (tail arg)))
        (ifeq (head (head arg)) (quote head)
            (head (self (cons (head (tail (head arg))) (tail arg))))
            (ifeq (head (head arg)) (quote tail)
                (tail (self (cons (head (tail (head arg))) (tail arg))))
                (ifeq (head (head arg)) (quote cons)
                    (cons (self (cons (head (tail (head arg))) (tail arg))) (self (cons (head (tail (tail (head arg)))) (tail arg))))
                    (ifeq (head (head arg)) (quote quote)
                        (head (tail (head arg)))
                        (ifeq (head (head arg)) (quote ifeq)
                            (ifeq (self (cons (head (tail (head arg))) (tail arg)))
                                  (self (cons (head (tail (tail (head arg)))) (tail arg)))
                                  (self (cons (head (tail (tail (tail (head arg))))) (tail arg)))
                                  (self (cons (head (tail (tail (tail (tail (head arg)))))) (tail arg))))
                            (ifeq (head (head arg)) (quote self)
                                (self (cons (head (tail arg))
                                        (cons (head (tail arg))
                                          (cons (self (cons (head (tail (head arg))) (tail arg))) (tail (quote (tail)))))))
                                (ifeq))))))))
    

#### Reference Implementation: yolk.py

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Python
#### Reference Implementation: yolk.yolk

*   license: BSD license
*   implementation-type: interpreter
*   host-language: Yolk

### Matchbox

*   type: Programming Language
*   inception-date: Feb 2015
*   genre: Pedagogical language
*   development-stage: mature
*   computational-class: ???
*   paradigms: Imperative
*   reference-distribution: [Matchbox distribution](/distribution/Matchbox distribution)

A toy language for a toy race-condition finder.

#### Implementation: matchbox.js

*   license: Public Domain
*   implementation-type: static analyzer
*   host-language: Javascript

### Backtracking Wang Tiler

*   type: Automaton
*   inception-date: Feb 2015
*   genre: Experimental language
*   development-stage: mature
*   computational-class: ???
*   paradigms: 2-dimensional
*   reference-distribution: [Wang Tilers distribution](/distribution/Wang Tilers distribution)

This backtracking Wang tiler is an automaton which naïvely tiles the
plane with [Wang tiles](http://en.wikipedia.org/wiki/Wang_tile).

It operates like a backtracking algorithm, backing up whenever it finds
it cannot place a tile, but it may be inaccurate to describe it as an
algorithm, since it never terminates.

#### Implementation: backtracking-wang-tiler.js

*   license: Public Domain
*   implementation-type: ???
*   host-language: Javascript

### Schrödinger's Game of Life

*   type: Automaton
*   inception-date: Feb 7, 2015
*   genre: Experimental language
*   development-stage: mature
*   computational-class: ???
*   paradigms: 2-dimensional, Cellular automaton, Non-deterministic
*   reference-distribution: [Schrödinger's Game of Life distribution](/distribution/Schrödinger's Game of Life distribution)

Schrödinger's Game of Life is what happens when [Conway's Game of Life][]
meets [Schrödinger's Cat][]: each individual cell may be **Alive**,
or **Dead**, or **Possibly-Alive-Possibly-Dead** (which we call **Cat**.)

This is, in essence, the result of applying
[non-determinism](Non-deterministic) to an existing
[cellular automaton](Cellular automaton), and this operation could
probably be applied to any cellular automaton with similar results.

For a full account of its development, see
[its README document](https://github.com/catseye/Schroedingers-Game-of-Life/blob/master/README.md).

#### Reference Implementation: slife

*   license: Public Domain
*   implementation-type: ???
*   host-language: Python
#### Implementation: slife.js

*   license: Public Domain
*   implementation-type: ???
*   host-language: Javascript

### SITU-SOL

*   type: Programming Language
*   inception-date: Jul 2015
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: Turing-complete
*   paradigms: Imperative, Stack-based

SITU-SOL is a vaguely Forth-like language which was designed and
implemented (by hand!) during RetroChallenge 2015/07, and entered
into an emulated [Commodore 64][] using [SITU-MON][].

#### Reference Implementation: SITU-SOL (Commodore 64)

*   license: Unknown license
*   implementation-type: compiler
*   host-language: 6502 machine code
*   target-language: 6502 machine code

### Samovar

*   type: Programming Language
*   inception-date: 2016
*   genre: DSL
*   development-stage: not fully complete
*   computational-class: unknown computational class
*   influences: Madison
*   paradigms: Probabilistic, Logic programming, State machine
*   reference-distribution: [Samovar distribution](/distribution/Samovar distribution)

Samovar is a DSL for world-modeling using predicates rather than explicit objects.
It could be thought of as an "assertion-retraction engine", which itself could be
thought of as a very stilted style of Prolog programming plus some syntactic
sugar.

Sample program:

    rules
      [actor(α),item(β),~holding(α,β)]  α picks up the β.   [holding(α,β)]
      [actor(α),item(β),holding(α,β)]   α puts down the β.  [~holding(α,β)]
    end
    situations
      [actor(Ignatz),item(brick)]
    end
    


### Maxixe

*   type: Programming Language
*   inception-date: 2016
*   genre: DSL
*   development-stage: not fully complete
*   computational-class: believed Turing-complete
*   influences: Madison
*   paradigms: Proof checking
*   reference-distribution: [Maxixe distribution](/distribution/Maxixe distribution)

Maxixe is a simple proof-checking language.  Given a proof written out fully and
explicitly (including all rules of inference), a computer can check if it is valid
or not.

Sample program:

    given
        Modus_Ponens                 = impl(P, Q) ; P |- Q
        Simplification               = and(P, Q)      |- Q
        Commutativity_of_Conjunction = and(P, Q)      |- and(Q, P)
        Premise                      =                |- and(p, impl(p, q))
    show
        q
    proof
        Step_1 = and(p, impl(p, q))    by Premise
        Step_2 = and(impl(p, q), p)    by Commutativity_of_Conjunction with Step_1
        Step_3 = impl(p, q)            by Simplification with Step_1
        Step_4 = p                     by Simplification with Step_2
        Step_5 = q                     by Modus_Ponens with Step_3, Step_4
    qed
    


- - - -

[1L]: TBD
[2-ill]: TBD
[Arboretuum]: http://catseye.tc/article/Lingography.md#arboretuum
[BASIC]: TBD
[Befunge-93]: http://catseye.tc/article/Lingography.md#befunge-93
[Befunge-98]: TBD
[Ben Olmstead]: TBD
[BitChanger]: http://esolangs.org/wiki/BitChanger
[Chris Pressey]: TBD
[Commodore 64]: http://catseye.tc/article/Retrocomputing.md#commodore-64
[Conway's Game of Life]: TBD
[Emmental]: http://catseye.tc/article/Lingography.md#emmental
[Esoteric Awards]: TBD
[Etcha]: http://catseye.tc/article/Lingography.md#etcha
[FALSE]: http://esolangs.org/wiki/FALSE
[Falderal]: http://catseye.tc/article/Formats.md#falderal
[Gregor Richards]: TBD
[ILLGOL]: http://catseye.tc/article/Lingography.md#illgol
[Jeffry Johnston]: http://esolangs.org/wiki/Jeffry%20Johnston
[Lua]: TBD
[Pixley]: http://catseye.tc/article/Lingography.md#pixley
[RUBE]: http://catseye.tc/article/Lingography.md#rube
[Rube Goldberg]: https://en.wikipedia.org/wiki/Rube_Goldberg
[Ruby]: http://www.ruby-lang.org/
[SITU-MON]: http://catseye.tc/article/Tools.md#situ-mon
[SMITH]: http://catseye.tc/article/Lingography.md#smith
[Scheme]: TBD
[Schrödinger's Cat]: https://en.wikipedia.org/wiki/Schr%C3%B6dinger's_cat
[Tamerlane]: http://catseye.tc/article/Lingography.md#tamerlane
[Thue]: TBD
[Trefunge-98]: TBD
[Turing-complete]: TBD
[Unefunge-98]: TBD
[Var'aq]: http://esolangs.org/wiki/Var'aq
[Wierd (John Colagioia)]: TBD
[Wierd (Milo van Handel)]: TBD
[brainfuck]: TBD
[reMorse]: http://esolangs.org/wiki/reMorse
