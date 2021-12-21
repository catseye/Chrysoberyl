Automata
========

*   image_url: https://static.catseye.tc/images/illustrations/Perpetual_Motion_Machine.jpg

This is a list of Automata designed by Cat's Eye Technologies, listed in chronological
order.  For more information on these Automata, [see below](#about-these-automata).

The distinction between an Automaton and a [Language](Languages.md) or a
[Gewgaw](Gewgaws.md) is not always cut-and-dried, so if you can't find what
you're looking for here, try those lists as well.

### SMETANA

*   type: Automaton
*   inception-date: ca 1994
*   genre: Esolang
*   development-stage: archival
*   computational-class: known not Turing-complete
*   paradigms: Self-modifying
*   reference-distribution: [SMETANA distribution](https://catseye.tc/distribution/SMETANA_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/SMETANA)
*   online @ [catseye.tc](https://catseye.tc/installation/yoob)

Sample configuration:

    Step 1. Swap step 1 with step 2.
    Step 2. Go to step 2.
    Step 3. Go to step 1.

SMETANA is a pathological little self-modifying language with only two
possible operations: Go to step *n*, and Swap steps *n* and *m*.
It has inspired a few variants and developments, notably a proof that
despite its minimalism, it is finite-automata-complete; it is also the
(great-?)grandfather of [SMITH][].

#### Reference Implementation: smetana.pl

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: [Perl][]

#### Implementation: SMETANA (Visual Basic)

*   license: Freely Redistributable
*   implementation-type: interpreter
*   host-language: [Visual Basic][]

#### Implementation: tc.catseye.yoob.smetana

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: [Java][]
*   host-platform: [yoob][]

### Cyclobots

![preview](https://static.catseye.tc/images/screenshots/Cyclobots.jpg)

*   type: Automaton
*   inception-date: ca 1994
*   genre: Desk toy
*   reference-distribution: [Cyclobots distribution](https://catseye.tc/distribution/Cyclobots_distribution)
*   online @ [catseye.tc](https://catseye.tc/installation/Cyclobots)

Cyclobots is an automaton that consists of a number of little virtual
"turtle robots" called "cyclobots".  Each cyclobot moves with a constant
velocity, and tries to follow exactly one other cyclobot, adjusting
its heading to point towards the cyclobot it is following.
No cyclobot is followed by more than one cyclobot.

A group of cyclobots tends to fall into one of several semi-stable
patterns.  The simplest of these is just a rotating circle, but
more complex, [trefoil](http://en.wikipedia.org/wiki/Trefoil_knot)-like
patterns are common.

I originally conceived of this automaton, calling it
an "interactive desktop toy", in 1994, and implemented
it immediately in Visual Basic.  I remember the year because I wrote the
first implementation of [SMETANA][] in Visual Basic at about the same time.

The original implementation had a few features which are not present (yet)
in the HTML5 version: cyclobots could collide with each other, and the user
could use the mouse to attract/repel them from a chosen point.

#### Reference Implementation: cyclobots.js

*   license: Public Domain
*   host-language: Javascript
*   host-platform: HTML5
*   development-stage: mature

#### Implementation: Cyclobots (Visual Basic)

*   license: Freely Redistributable
*   host-language: Visual Basic
*   development-stage: lost

### RUBE

*   type: Automaton
*   inception-date: 1997
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: Bully automaton, 2-dimensional
*   reference-distribution: [RUBE distribution](https://catseye.tc/distribution/RUBE_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/RUBE)

Sample configuration:

      0a21646c726f77202c6f6c6c6548
    , :::::::::::::::::::::::::::: ,
     )
     ==============================
    F
                                   O F
                                   c
                                   =

RUBE is an esoteric programming language in tribute to [Rube Goldberg][],
with bulldozers pushing around numbered crates, knocking them together to
perform computations.  It is based on a variant of a cellular automaton called
a *[bully automaton][]*, where certain state changes can
force other state changes to occur elsewhere in the playfield.

#### Reference Implementation: rube.c

*   license: BSD license
*   implementation-type: interpreter
*   host-language: [ANSI C][]

### REDGREEN

*   type: Automaton
*   inception-date: 1998
*   genre: Esolang
*   development-stage: mature
*   computational-class: Turing-complete
*   influences: RUBE
*   paradigms: Cellular automaton
*   reference-distribution: [REDGREEN distribution](https://catseye.tc/distribution/REDGREEN_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/REDGREEN)
*   online @ [catseye.tc](https://catseye.tc/installation/REDGREEN)

Sample configuration:

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
    #<<<<<<<<<<<<<<<<<############################
                                    %
                                    T

REDGREEN is a cellular automaton that simulates a little
"physical world", much like [RUBE][].

#### Reference Implementation: redgreen.alp

*   license: BSD license
*   implementation-type: formal description
*   host-language: ALPACA

### noit o' mnain worb

![screenshot](https://static.catseye.tc/images/screenshots/noit_o_mnain_worb.jpg)

*   type: Automaton
*   inception-date: Sep 15, 2000
*   genre: Esolang
*   development-stage: mature
*   computational-class: ???
*   paradigms: Particle automaton, Probabilistic
*   reference-distribution: [noit o' mnain worb distribution](https://catseye.tc/distribution/noit_o'_mnain_worb_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/noit_o'_mnain_worb)
*   online @ [catseye.tc](https://catseye.tc/installation/noit_o'_mnain_worb)
*   online @ [catseye.tc](https://catseye.tc/installation/yoob)

Sample configuration:

    #####         #####
    #   ###########   #
    # . >         < . #
    #   #####v#####   #
    #####   #  ########
            #       >!#
            #v#########
            # #
            ###

noit o' mnain worb is a probabilistic particle automaton that
uses pressure between randomly moving particles to approximate the behaviour
of circuits.  It can approximate computation with these circuits, too, but
it's so lossy that it has more value as just a neat toy to watch.

(The name of this language contains a *secret message*! Can *you* find it?)

#### Reference Implementation: worb.pl

*   license: BSD license
*   implementation-type: interpreter
*   host-language: [Perl][]

#### Implementation: worb.js

*   license: BSD license
*   implementation-type: interpreter
*   host-language: [Javascript][]
*   host-platform: [HTML5][]

#### Implementation: tc.catseye.yoob.worb

*   license: BSD license
*   implementation-type: interpreter
*   host-language: [Java][]
*   host-platform: [yoob][]

### Circute

![screenshot](https://static.catseye.tc/images/screenshots/Circute.jpg)

*   type: Automaton
*   inception-date: 2005
*   genre: Esolang
*   development-stage: mature
*   computational-class: known not Turing-complete
*   influences: Wireworld
*   paradigms: Cellular automaton
*   reference-distribution: [Circute distribution](https://catseye.tc/distribution/Circute_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/Circute)
*   online @ [catseye.tc](https://catseye.tc/installation/Circute)
*   online @ [catseye.tc](https://catseye.tc/installation/yoob)

Sample configuration:

                     =
                     =
      #######==   ===N===   =========
      #       =   =     =   =       =
    ==N==     = ==N== ==N== =     ==N==
    =   =     = =   = =   = =     =   =
    =====     = ===== ===== =     =====
      =       =   =     =   =       =
      =============     =============

Circute is a cellular automaton that simulates conduits that
carry digital signals and NAND gates that manipulate those signals.

#### Reference Implementation: circute.alp

*   license: BSD license
*   implementation-type: formal description
*   host-language: ALPACA

#### Implementation: tc.catseye.yoob.circute

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: [Java][]
*   host-platform: [yoob][]

### Braktif

*   type: Automaton
*   inception-date: 2005
*   genre: Esolang
*   development-stage: mature
*   computational-class: believed Turing-complete
*   influences: brainfuck
*   paradigms: Cellular automaton
*   reference-distribution: [Braktif distribution](https://catseye.tc/distribution/Braktif_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/Braktif)
*   online @ [catseye.tc](https://catseye.tc/installation/Braktif)

Sample configuration:

                                *
                           <<*[--]*
    000000000000000000  *[-----  --]
    -----------------d-i--         --------

Braktif is a cellular automaton modelled closely after the [brainfuck][]
programming language.

#### Reference Implementation: braktif.alp

*   license: BSD license
*   implementation-type: formal description
*   host-language: ALPACA

### Xigxag

*   type: Automaton
*   inception-date: Apr 23, 2007
*   genre: Esolang
*   development-stage: mature
*   computational-class: unknown computational class
*   paradigms: String-rewriting
*   reference-distribution: [Xigxag distribution](https://catseye.tc/distribution/Xigxag_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/Xigxag)

Sample configuration:

    ><<

Sample result:

    ><<
    <<>><
    <><<<<>>
    <<<<>><><><<><<<><<<>

Xigxag is a simple string-copying automaton that has exponential
growth almost everywhere (i.e. there are only a finite number of initial
configurations that don't blow up.)

#### Reference Implementation: xigxag.pl

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: [Perl][]

### Didigm

*   type: Automaton
*   inception-date: Nov 20, 2007
*   genre: Esolang
*   development-stage: not fully complete
*   computational-class: ???
*   paradigms: Cellular automaton, Reflective
*   reference-distribution: [Specs on Spec distribution](https://catseye.tc/distribution/Specs_on_Spec_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/Didigm)

Sample configuration:

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

Didigm is a reflective cellular automaton: the transition rules
for the automaton are defined by forms in the very playfield governed by
those transition rules.

### Jaccia

*   type: Automaton
*   inception-date: Apr 11, 2009
*   genre: Esolang
*   development-stage: mature
*   computational-class: known not Turing-complete
*   paradigms: Cellular automaton, 2-dimensional
*   reference-distribution: [Jaccia and Jacciata distribution](https://catseye.tc/distribution/Jaccia_and_Jacciata_distribution)
*   entry @ [esolangs.org](https://esolangs.org/wiki/Jaccia)
*   online @ [catseye.tc](https://catseye.tc/installation/Jaccia)

Sample configuration:

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

Sample result:

    #######S###
    #    :::  #
    # ###:### #
    # # #:::# #
    # # # #:###
    #   # #:# #
    ##### #:# #
    # #   #:  #
    # # ###:###
    #   #  :::#
    #########F#

Jaccia and Jacciata are cellular automata inspired by the [Announcement
of Scientific Proof that Slime Molds are Intelligent Maze Solvers](http://web.archive.org/web/20020220163303/http://www.riken.go.jp/lab-www/frontier-div/NEWSLETTER/feb2001/ameboid_e.htm).
Jaccia can solve mazes too, by a similar mechanism (shrinking). Jacciata builds
upon this to find the shortest path through a maze, if one exists and is unique.

#### Reference Implementation: jaccia.alp

*   license: BSD license
*   implementation-type: formal description
*   host-language: ALPACA

### Jacciata

*   type: Automaton
*   genre: Esolang
*   online @ [catseye.tc](https://catseye.tc/installation/Jacciata)

Jacciata is a variant of [Jaccia][] which finds the shortest path.

### Chzrxl

![preview](https://static.catseye.tc/images/screenshots/Chzrxl.jpg)

*   type: Automaton
*   inception-date: 2013
*   genre: Desk toy
*   reference-distribution: [Chzrxl distribution](https://catseye.tc/distribution/Chzrxl_distribution)
*   online @ [catseye.tc](https://catseye.tc/installation/Chzrxl)

"Chzrxl, the Living Inkblot."  Or is it a sort of self-attracting
lava lamp?

#### Reference Implementation: chzrxl.js

*   type: Implementation
*   license: Public Domain
*   host-language: Javascript
*   host-platform: HTML5

### Backtracking Wang Tiler

![screenshot](https://static.catseye.tc/images/screenshots/Backtracking_Wang_Tiler.jpg)

*   type: Automaton
*   inception-date: Feb 2015
*   genre: Experimental language
*   development-stage: mature
*   computational-class: ???
*   paradigms: 2-dimensional
*   reference-distribution: [Backtracking Wang Tiler distribution](https://catseye.tc/distribution/Backtracking_Wang_Tiler_distribution)
*   online @ [catseye.tc](https://catseye.tc/installation/Backtracking%20Wang%20Tiler)

This backtracking Wang tiler is an automaton which naïvely tiles the
plane with [Wang tiles](http://en.wikipedia.org/wiki/Wang_tile).

It operates like a backtracking algorithm, backing up whenever it finds
it cannot place a tile, but it may be inaccurate to describe it as an
algorithm, since it never terminates.

#### Implementation: backtracking-wang-tiler.js

*   license: Public Domain
*   implementation-type: generator
*   host-language: [Javascript][]
*   host-platform: [HTML5][]

### Schrödinger's Game of Life

![screenshot](https://static.catseye.tc/images/screenshots/Schroedingers_Game_of_Life.jpg)

*   type: Automaton
*   inception-date: Feb 7, 2015
*   genre: Experimental language
*   development-stage: mature
*   computational-class: ???
*   paradigms: 2-dimensional, Cellular automaton, Non-deterministic
*   reference-distribution: [Schrödinger's Game of Life distribution](https://catseye.tc/distribution/Schrödinger's_Game_of_Life_distribution)
*   online @ [catseye.tc](https://catseye.tc/installation/Schrödinger's%20Game%20of%20Life)

Schrödinger's Game of Life is what happens when [Conway's Game of Life][]
meets [Schrödinger's Cat][]: each individual cell may be **Alive**,
or **Dead**, or **Possibly-Alive-Possibly-Dead** (which we call **Cat**.)

This is, in essence, the result of applying
[non-determinism][] to an existing
[cellular automaton][], and this operation could
probably be applied to any cellular automaton with similar results.

For a full account of its development, see
[its README document](https://github.com/catseye/Schroedingers-Game-of-Life/blob/master/README.md).

#### Reference Implementation: slife

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: Python

#### Implementation: slife.js

*   license: Public Domain
*   implementation-type: interpreter
*   host-language: [Javascript][]
*   host-platform: [HTML5][]

## About these Automata

We should say a few words about these automata here.

- - - -

[Javascript]: ../article/Project%20Dependencies.md#javascript
[HTML5]: https://www.w3.org/TR/html5/
[yoob]: ../article/Archived.md#yoob
[Jaccia]: ../article/Automata.md#jaccia
[SMITH]: ../article/Languages.md#smith
[Perl]: ../article/Project%20Dependencies.md#perl
[Visual Basic]: https://en.wikipedia.org/wiki/Visual_Basic
[Java]: ../article/Project%20Dependencies.md#java
[Rube Goldberg]: https://en.wikipedia.org/wiki/Rube_Goldberg
[bully automaton]: https://esolangs.org/wiki/Bully%20automaton
[RUBE]: ../article/Automata.md#rube
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[brainfuck]: https://esolangs.org/wiki/brainfuck
[Conway's Game of Life]: http://en.wikipedia.org/wiki/Conway's_Game_of_Life
[Schrödinger's Cat]: https://en.wikipedia.org/wiki/Schr%C3%B6dinger's_cat
[SMETANA]: ../article/Automata.md#smetana
[non-determinism]: https://esolangs.org/wiki/Category:Nondeterministic
[cellular automaton]: https://en.wikipedia.org/wiki/Cellular_automaton

