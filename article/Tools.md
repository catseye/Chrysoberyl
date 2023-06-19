Tools
=====

*   image_url: https://static.catseye.tc/images/illustrations/Allen_wrench_and_screw_(PSF).jpg

Note that the precise distinctions between a Tool, a Platform, and a Library are debatable,
and entries may be categorized somewhat arbitrarily.

Tools for Retrocomputing platforms might be found in the [Retrocomputing][] article instead.

[Formats][] often have tools for processing them, and those are listed along with the format
instead of here.

Note that Cat's Eye Technologies also maintains some [forks](Forks.md) of some tools.

_Note also that there are several novel generators in here, and possibly other kinds of_
_generators, that should probably be in their own "Generators" article rather than here in "Tools"._

### DAM

*   summary: You've tried the Document Object Model, now try the Document *Awesome* Model
*   inception-date: ca 2019
*   development-stage: not fully complete
*   reference-distribution: [DAM distribution](https://catseye.tc/distribution/DAM_distribution)

`DAM` is a little Javascript library for creating trees of [HTML5][] elements
in the DOM.  It supercedes the `element-factory` module from [yoob.js][],
and Cat's Eye Technologies' newer [gewgaws](article/Gewgaws.md) use it
instead of yoob.js for creating their control panels.  It's rather a lot like
[hyperscript](https://github.com/hyperhype/hyperscript) except more minimal
and, of course, awesomer.

#### Implementation: DAM (Javascript)

*   reference: true
*   license: Public Domain
*   host-language: [Javascript][]
*   host-platform: [HTML5][]

### DiskSumo

![DiskSumo main menu](https://static.catseye.tc/images/screenshots/DiskSumo.png)
![DiskSumo during transfer](https://static.catseye.tc/images/screenshots/DiskSumo%20%28transfer%29.png)

*   inception-date: ca 2005
*   reference-distribution: [DiskSumo distribution](https://catseye.tc/distribution/DiskSumo_distribution)

DiskSumo is a program to transfer disk images off a Commodore 64 over
the RS-232 port via the XMODEM protocol at 300 baud.

#### Implementation: DiskSumo (BASIC)

*   reference: true
*   license: Public Domain
*   host-language: [Commodore BASIC 2.0][]
*   host-platform: [Commodore 64][]

### Dissociated Parse

*   inception-date: Nov 2021
*   reference-distribution: [Dissociated Parse distribution](https://catseye.tc/distribution/Dissociated_Parse_distribution)

Dissociated Parse is not really a tool, rather, it is an algorithm;
specifically it is an adaptation of the [Dissociated Press](https://en.wikipedia.org/wiki/Dissociated_press)
algorithm to work on parse trees (rather than the sequential list of
words it conventionally works on).  It was developed during
[NaNoGenMo 2021][] and was used to generate the novel
[The Lion, the Witches, and the Weird Road][].

#### Implementation: Dissociated Parse (Python)

*   reference: true
*   license: Unknown license
*   host-language: [Python][]

### define-opaque

*   inception-date: Jan 2023
*   reference-distribution: [define-opaque distribution](https://catseye.tc/distribution/define-opaque_distribution)

`define-opaque` is a library for R5RS Scheme that adds a facility for
creating opaque data types in a simplistic fashion.  It was written
based on some of the ideas in [Information Hiding in Scheme](https://github.com/cpressey/Information-Hiding-in-Scheme).

It exists partly because I actually wanted to implement some of those
ideas in Scheme, to support building things such as
[LCF-style theorem provers](https://github.com/cpressey/LCF-style-ND)
in Scheme, and abstract data types are otherwise difficult to
implement in Scheme.

#### Implementation: define-opaque.scm

*   reference: true
*   license: Public Domain
*   host-language: [Scheme][]

### ellsync

*   inception-date: 2018
*   development-stage: work in progress
*   reference-distribution: [ellsync distribution](https://catseye.tc/distribution/ellsync_distribution)

**ellsync** is an opinionated [poka-yoke][] for [rsync][].  "Opinionated" because
it was designed for a particular use case for rsync (offline backups).  "Poka-yoke"
because it exposes a restricted interface to rsync, which prevents using it in dangerous ways.

#### Implementation: ellsync (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### Funicular

*   summary: Scripts to set up dev environments on various OS'es on sundry architectures
*   inception-date: Jun 17 2014
*   development-stage: not fully complete
*   reference-distribution: [Funicular distribution](https://catseye.tc/distribution/Funicular_distribution)

**Funicular** is a system that semi-automates the creation of development
environments on eclectic architectures. "Semi-automate" means it automates
what it can, and provides repeatable instructions for you to follow for
what it can't.

"Eclectic architectures" is not terribly-well defined, but it includes
retrocomputing and esoteric architectures.  Basically, if you've got an
emulator for it and install images for it, you might be able
to outfit and run a system for it, using Funicular.

It replaces [Amiga Gondola][].  It can handle such OS/emulator combinations
as [NetBSD][] under [QEMU][], [FreeDOS][] under [QEMU][],
[AmigaDOS 1.3][] on an [Amiga 500][] under [E-UAE][],
[Applesoft BASIC][] on an [Apple II][] under [linapple][],
and [Commodore BASIC 2.0][] on a [Commodore 64][] under [VICE][].

#### Implementation: funicular

*   reference: true
*   license: Public Domain
*   host-language: [Bourne shell][]

### hatoucan

*   summary: Tokenizer for Commodore BASIC 2.0 programs
*   inception-date: 2015
*   development-stage: not fully complete
*   reference-distribution: [hatoucan distribution](https://catseye.tc/distribution/hatoucan_distribution)

`hatoucan` is a tokenizer for [Commodore BASIC 2.0][] programs.
It is compatible with a subset of `petcat`, but is written in
Python and is in the public domain.

#### Implementation: hatoucan (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### kinoje

*   inception-date: 2017
*   development-stage: work in progress
*   reference-distribution: [kinoje distribution](https://catseye.tc/distribution/kinoje_distribution)

**kinoje** is a templating-based animation tool.  A provided template is filled out once for each
frame of the animation; the result of the template expansion is used to create a still image; and
the resulting sequence of images is compiled into the finished movie.

#### Implementation: kinoje (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### Lariat

*   inception-date: 2021
*   development-stage: work in progress
*   reference-distribution: [Lariat distribution](https://catseye.tc/distribution/Lariat_distribution)

Lariat is an abstract data type for proper lambda terms, consisting of four operations:
`app`, `abs`, `var`, and `destruct`.  Each of the operations produces a proper lambda
term as its result, i.e. bound terms are never exposed to the user of the ADT.  Lariat is
a total data type in the sense that all of the operations are defined on all
properly-typed input values.  It is a higher-order data type in the sense that `destruct`
takes function values as parameters.

#### Implementation: Data.Lariat

*   reference: false
*   license: Unknown license
*   host-language: [Haskell][]

### MARYSUE

*   summary: An engine for generating non-interactive fiction
*   inception-date: Nov 2015
*   development-stage: not fully complete
*   reference-distribution: [MARYSUE distribution](https://catseye.tc/distribution/MARYSUE_distribution)

MARYSUE is the story generator used to generate the novel
[A Time for Destiny][] for [NaNoGenMo 2015][].

#### Implementation: MARYSUE (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### Parc

*   summary: The simplest parser combinator library that could possibly work
*   inception-date: Dec 2022
*   development-stage: not fully complete
*   reference-distribution: [Parc distribution](https://catseye.tc/distribution/Parc_distribution)

Parc is a particularly simple parser combinator library, and a series of
experimental variations on this theme, written in Haskell.

#### Implementation: Parc.hs

*   reference: true
*   license: MIT License
*   host-language: [Haskell][]

### Philomath

*   summary: An LCF-style theorem prover written in ANSI C
*   inception-date: Feb 2022
*   development-stage: not fully complete
*   reference-distribution: [Philomath distribution](https://catseye.tc/distribution/Philomath_distribution)

Philomath is an LCF-style theorem prover written in ANSI C.  It supports classical propositional
logic in a Natural Deduction system with labelled assumptions.

#### Implementation: Philomath (ANSI C)

*   reference: true
*   license: Public Domain
*   host-language: [ANSI C][]

### relwrite

*   summary: relates strings to strings via a grammar in the Chomsky hierarchy
*   inception-date: Nov 2022
*   development-stage: not fully complete
*   reference-distribution: [relwrite distribution](https://catseye.tc/distribution/relwrite_distribution)

relwrite relates strings to strings via a grammar in the Chomsky hierarchy.

#### Implementation: relwrite

*   reference: true
*   license: MIT License
*   host-language: [Python][]

### shelf

*   summary: A "package manager" that doesn't actually install anything
*   inception-date: 2016
*   development-stage: work in progress
*   reference-distribution: [shelf distribution](https://catseye.tc/distribution/shelf_distribution)

`shelf` is a "package manager" which doesn't actually install any files.
Instead, it stores the source trees of sundry packages in a single directory,
creates link farms to the interesting files within those trees,
and manages your search paths to include those link farms.
those trees. The source trees are typically the working directories of
local git or Mercurial clones, or they can be source distributions from tarballs.
`shelf`, written in Bourne shell, is a replacement for [toolshelf][], which was
written in Python.

#### Implementation: shelf.sh

*   reference: true
*   license: Public Domain
*   host-language: [Bourne shell][]

### SITU-MON

![SITU-MON](https://git.catseye.tc/SITU-SOL/blob/master/doc/bootstrap-zero/images/tumblr_inline_nrdcglfU4p1tvda25_540.png?raw=true)

*   inception-date: Jul 2015
*   development-stage: mature
*   reference-distribution: [SITU-SOL distribution](https://catseye.tc/distribution/SITU-SOL_distribution)

SITU-MON is a machine language monitor for [6502][]-based
systems, written (by hand!) during RetroChallenge 2015/07 and entered into
an emulated [Commodore 64][] using [SITU-PAN][].

#### Implementation: SITU-MON (Commodore 64)

*   reference: true
*   license: Unknown license
*   host-language: [6502 machine code][]
*   host-platform: [Commodore 64][]

### SITU-PAN

![SITU-PAN](https://git.catseye.tc/SITU-SOL/blob/master/doc/bootstrap-zero/images/tumblr_inline_nr19fai3D41tvda25_540.jpg?raw=true)

*   inception-date: Jul 2015
*   development-stage: mature
*   reference-distribution: [SITU-SOL distribution](https://catseye.tc/distribution/SITU-SOL_distribution)

SITU-PAN is a *front-panel switches simulator* for the [Commodore 64][].
It displays 8 virtual LEDs and 8 virtual dip switches on the screen.
The LEDs display the bit pattern at the current address in memory.
Via the keyboard, the switches may be toggled, a new bit pattern
written into memory, and the address advanced. In this way, machine
code programs may be entered into memory, and then run.
SITU-PAN was written during RetroChallenge 2015/07 for the purposes
of entering [SITU-MON][] into an emulated C64.

#### Implementation: frontpanel.bas

*   reference: true
*   license: Unknown license
*   host-language: [Commodore BASIC 2.0][]
*   host-platform: [Commodore 64][]

### tagfarm

*   inception-date: Apr 2020
*   development-stage: not fully complete
*   reference-distribution: [tagfarm distribution](https://catseye.tc/distribution/tagfarm_distribution)

`tagfarm` is an ultra-lightweight, filesystem-based categorization system for arbitrary
files.  Each tag is implemented as a directory full of symbolic links to files with that tag.

#### Implementation: tagfarm (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### The Swallows Engine

*   summary: An engine for generating non-interactive fiction
*   inception-date: Nov 2013
*   development-stage: not fully complete
*   reference-distribution: [The Swallows distribution](https://catseye.tc/distribution/The_Swallows_distribution)

The Swallows Engine is the engine used to generate _The Swallows_
series of generated novels for [NaNoGenMo 2013][].

#### Implementation: The Swallows Engine (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### tree

*   inception-date: 2014
*   development-stage: mature
*   reference-distribution: [tree distribution](https://catseye.tc/distribution/tree_distribution)

Cat's Eye Technologies' `tree` is a command-line tool that displays an
indented directory tree, similar to "The Tree Command for Linux" except
simpler.

#### Implementation: tree (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### T-Rext

*   summary: Tidier-upper for generated text
*   inception-date: Nov 2014
*   development-stage: mature
*   reference-distribution: [T-Rext distribution](https://catseye.tc/distribution/T-Rext_distribution)

T-Rext is a command-line filter that attempts to clean up spaces and
punctuation in a text file.  Its purpose is so that, when you are writing
a text generator, such as a Markov processor, you need not worry too much
about its output format; just toss its output through T-Rext when you're
done to make it more presentable.

#### Implementation: t-rext (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### yastasoti

*   inception-date: 2018
*   development-stage: work in progress
*   reference-distribution: [yastasoti distribution](https://catseye.tc/distribution/yastasoti_distribution)

**yastasoti** is yet another script for archiving stuff off teh internets.
It supports consulting an _archive router_ to determine where each stuff
is archived to.

#### Implementation: yastasoti (Python)

*   reference: true
*   license: Public Domain
*   host-language: [Python][]

### yucca

*   summary: Static analyzer for 8-bit BASIC programs
*   inception-date: 2012
*   reference-distribution: [yucca distribution](https://catseye.tc/distribution/yucca_distribution)

`yucca` is a dialect-agnostic static analyzer for 8-bit BASIC
programs.  It can find `GOTO`'s and `GOSUB`'s
which refer to non-existent line numbers, or line numbers which contain
only a `REM`, among a few other modest features.

#### Implementation: yucca (Python)

*   reference: true
*   license: MIT license
*   host-language: [Python][]

Not-exactly Tools
-----------------

More like demos?

### Ribos

*   summary: Well-commented C64 raster interrupt example
*   inception-date: April 2007
*   development-stage: mature
*   reference-distribution: [SixtyPical distribution](https://catseye.tc/distribution/SixtyPical_distribution)

A simple Commodore 64 graphics demo that uses the raster interrupt facility
of the VIC-II chip: the colour of the border of the screen is inverted,
but only in the middle part of the screen.  Includes well-commented source
in 6502 assembly language.

Was previously distributed in the [Ribos distribution](https://catseye.tc/distribution/Ribos_distribution)
and the [C64 Demo Depot distribution](https://catseye.tc/distribution/C64_Demo_Depot_distribution),
which have both been discontinued.

### The PETulant Cursor

*   summary: A tiny C64 "display hack"
*   inception-date: ca 1989
*   development-stage: vintage
*   reference-distribution: [SixtyPical distribution](https://catseye.tc/distribution/SixtyPical_distribution)

A tiny (44 byte) "display hack" for the Commodore 64.

Was previously distributed in [The PETulant Cursor distribution](https://catseye.tc/distribution/The_PETulant_Cursor_distribution)
and the [C64 Demo Depot distribution](https://catseye.tc/distribution/C64_Demo_Depot_distribution),
which have both been discontinued.

Archival Tools
--------------

### TPiS

*   subtitle: **Total Procedures in Scheme**
*   summary: Totality-checker for Scheme procedures
*   inception-date: ca 2006
*   development-stage: archival
*   reference-distribution: [TPiS distribution](https://catseye.tc/distribution/TPiS_distribution)

This is a static analyzer, written in Scheme, which can check if
given Scheme procedures are total (always terminate, on any input) by
checking that they are specified primitive-recursively.  What's more, it
is written almost entirely in a primitive-recursive style, so it can
check itself!

#### Implementation: TPiS (Scheme)

*   reference: true
*   license: BSD license
*   host-language: [Scheme][]

### yoob.js

*   summary: A framework for interactive esolang implementation
*   inception-date: Oct 4 2012
*   development-stage: not fully complete
*   reference-distribution: [yoob.js distribution](https://catseye.tc/distribution/yoob.js_distribution)

`yoob.js` is a framework for implementing esoteric programming languages
in Javascript/HTML5.  It has some differences from the earlier [yoob][]
framework, which is in Java.

#### Implementation: yoob.js (Javascript)

*   reference: true
*   implementation-type: framework
*   license: Public Domain
*   host-language: [Javascript][]

[AmigaDOS 1.3]: ../article/Project%20Dependencies.md#amiga-500
[Amiga 500]: ../article/Project%20Dependencies.md#amiga-500
[E-UAE]: ../article/Project%20Dependencies.md#amiga-500
[FreeBSD]: https://www.freebsd.org/
[Amiga Gondola]: ../article/Archived.md#amiga-gondola
[NetBSD]: https://netbsd.org/
[FreeDOS]: ../article/Project%20Dependencies.md#ms-dos
[Commodore BASIC 2.0]: ../article/Project%20Dependencies.md#commodore-basic-20
[Commodore 64]: ../article/Project%20Dependencies.md#commodore-64
[A Time for Destiny]: ../article/Texts.md#a-time-for-destiny
[NaNoGenMo 2013]: ../article/Events.md#nanogenmo-2013
[NaNoGenMo 2015]: ../article/Events.md#nanogenmo-2015
[6502]: ../article/Project%20Dependencies.md#6502
[6502 machine code]: ../article/Project%20Dependencies.md#6502
[SITU-PAN]: ../article/Tools.md#situ-pan
[SITU-MON]: ../article/Tools.md#situ-mon
[Retrocomputing]: https://catseye.tc/article/Retrocomputing
[Formats]: ../article/Formats.md
[The Platform]: ../article/Platforms.md#the-cats-eye-technologies-platform
[yoob]: ../article/Archived.md#yoob
[QEMU]: ../article/Project%20Dependencies.md#ibm-pc-compatible
[VICE]: https://vice-emu.sourceforge.io/
[Bourne shell]: ../article/Project%20Dependencies.md#bourne-shell
[Apple II]: ../article/Project%20Dependencies.md#apple-ii
[Applesoft BASIC]: ../article/Project%20Dependencies.md#applesoft-basic
[toolshelf]: ../article/Archived.md#toolshelf
[Python]: ../article/Project%20Dependencies.md#python
[Javascript]: ../article/Project%20Dependencies.md#javascript
[Lua]: ../article/Project%20Dependencies.md#lua
[Perl]: ../article/Project%20Dependencies.md#perl
[Haskell]: ../article/Project%20Dependencies.md#haskell
[Scheme]: ../article/Project%20Dependencies.md#scheme
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[rsync]: https://rsync.samba.org/
[poka-yoke]: https://en.wikipedia.org/wiki/Poka-yoke
[linapple]: ../article/Forks.md#linapple
[HTML5]: https://www.w3.org/TR/html5/
[yoob.js]: ../article/Tools.md#yoobjs
[NaNoGenMo 2021]: ../article/Events.md#nanogenmo-2021
[The Lion, the Witches, and the Weird Road]: ../article/Texts.md#the-lion-the-witches-and-the-weird-road

