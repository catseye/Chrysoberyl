Tools
=====

Note that the precise distinctions between a Tool, a Platform, and a Library are debatable,
and entries may be categorized somewhat arbitrarily.

Tools for Retrocomputing platforms might be found in the Retrocomputing article instead.

### Console::Virtual

*   summary: Package for simulating a virtual console
*   inception-date: ca 2003

`Console::Virtual` is a simple, lightweight abstraction layer which
allows a program to interact with the user through a console, which
is emulated on whatever user interface is really available.
  
#### Implementation: Console::Virtual (Perl module)

*   reference: true
*   in-distributions:
*   - 'Console::Virtual distribution'
*   - 'Corona: Realm of Magic distribution'
*   - Ypsilax distribution
*   - noit o' mnain worb distribution
*   - HUNTER distribution
*   license: BSD license
*   host-language: Perl

### DiskSumo

*   inception-date: ca 2005

DiskSumo is a program to transfer disk images off a Commodore 64 over
the RS-232 port via the XMODEM protocol at 300 baud.

#### Implementation: DiskSumo (BASIC)

*   reference: true
*   in-distribution: DiskSumo distribution
*   license: Public Domain
*   host-language: Commodore BASIC 2.0
*   host-platform: Commodore 64

### Funicular

*   summary: Scripts to set up dev environments on various OS'es on sundry architectures
*   inception-date: Jun 17 2014
*   development-stage: not fully complete

**Funicular** is a system that semi-automates the creation of development
environments on eclectic architectures. "Semi-automate" means it automates
what it can, and provides repeatable instructions for you to follow for
what it can't.

"Eclectic architectures" is not terribly-well defined, but it includes
retrocomputing and esoteric architectures.  Basically, if you've got an
emulator for it and install and support images for it, you might be able
to install and outfit and and run a system for it, using Funicular.

It replaces [[Amiga Gondola]].  It can handle such OS/emulator combinations
as [[AmigaDOS 1.3]] under [[E-UAE]] emulating an [[Amiga 500]],
[[FreeDOS]] under [[QEMU]], and [[NetBSD]] under [[QEMU]].

#### Implementation: funicular

*   reference: true
*   in-distribution: Funicular distribution
*   license: Public Domain
*   host-language: Lua

### Guten-gutter

*   summary: Extractor of Project Gutenberg texts
*   inception-date: 2014
*   development-stage: mature

Guten-gutter is a command-line tool that removes the boilerplate
from Project Gutenberg text files.

#### Implementation: guten-gutter (Python)

*   reference: true
*   in-distribution: Guten-gutter distribution
*   license: Public Domain
*   host-language: Python

### hatoucan

*   summary: Tokenizer for Commodore BASIC 2.0 programs
*   inception-date: 2015
*   development-stage: not fully complete

`hatoucan` is a tokenizer for Commodore BASIC 2.0 programs.
It is compatible with a subset of `petcat`, but is written in
Python and is in the public domain.

#### Implementation: hatoucan (Python)

*   reference: true
*   in-distribution: hatoucan distribution
*   license: Public Domain
*   host-language: Python

### kinoje

*   inception-date: 2017
*   development-stage: work in progress

**kinoje** is a templating-based animation tool.  A provided template is filled out once for each
frame of the animation; the result of the template expansion is used to create a still image; and
the resulting sequence of images is compiled into the finished movie.

#### Implementation: kinoje (Python)

*   reference: true
*   in-distribution: kinoje distribution
*   license: Public Domain
*   host-language: Python

### MARYSUE

*   summary: An engine for generating non-interactive fiction
*   inception-date: Nov 2015
*   development-stage: not fully complete

MARYSUE is the story generator used to generate the novel
[[A Time for Destiny]] for [[NaNoGenMo 2015]].

#### Implementation: MARYSUE (Python)

*   reference: true
*   in-distributions: MARYSUE distribution
*   license: Public Domain
*   host-language: Python

### seedbank

*   summary: Records seeds used in random generation and allows re-use
*   inception-date: 2014
*   development-stage: mature

`seedbank` is a Python module which takes care of recording the seed
used for random generation, and allowing a previously used seed to
be used again in the future.

#### Implementation: seedbank (Python)

*   reference: true
*   in-distribution: seedbank distribution
*   license: Public Domain
*   host-language: Python

### shelf

*   summary: A "package manager" that doesn't actually install anything
*   inception-date: 2016
*   development-stage: work in progress

`shelf` is a "package manager" which doesn't actually install any files.
Instead, it stores the source trees of sundry packages in a single directory,
creates link farms to the interesting files within those trees,
and manages your search paths to include those link farms.
those trees. The source trees are typically the working directories of
local git or Mercurial clones, or they can be source distributions from tarballs.
`shelf`, written in Bourne shell, is a replacement for `toolshelf`, which was
written in Python.

#### Implementation: shelf.sh

*   reference: true
*   in-distribution: shelf distribution
*   license: Public Domain
*   host-language: Bourne shell

### SITU-MON

*   inception-date: Jul 2015
*   development-stage: mature

SITU-MON is a machine language monitor for [[6502 machine code|6502]]-based
systems, written (by hand!) during RetroChallenge 2015/07 and entered into
an emulated [[Commodore 64]] using [[SITU-PAN]].

#### Implementation: SITU-MON (Commodore 64)

*   reference: true
*   in-distribution: SITU-SOL distribution
*   license: Unknown license
*   host-language: 6502 machine code
*   host-platform: Commodore 64

### SITU-PAN

*   inception-date: Jul 2015
*   development-stage: mature

SITU-PAN is a *front-panel switches simulator* for the [[Commodore 64]].
It displays 8 virtual LEDs and 8 virtual dip switches on the screen.
The LEDs display the bit pattern at the current address in memory.
Via the keyboard, the switches may be toggled, a new bit pattern
written into memory, and the address advanced. In this way, machine
code programs may be entered into memory, and then run.
SITU-PAN was written during RetroChallenge 2015/07 for the purposes
of entering [[SITU-MON]] into an emulated C64.

#### Implementation: frontpanel.bas

*   reference: true
*   in-distribution: SITU-SOL distribution
*   license: Unknown license
*   host-language: Commodore BASIC 2.0
*   host-platform: Commodore 64

### The Swallows Engine

*   summary: An engine for generating non-interactive fiction
*   inception-date: Nov 2013
*   development-stage: not fully complete

The Swallows Engine is the engine used to generate _The Swallows_
series of generated novels for [[NaNoGenMo 2013]].

#### Implementation: The Swallows Engine (Python)

*   reference: true
*   in-distributions: The Swallows distribution
*   license: Public Domain
*   host-language: Python

### T-Rext

*   summary: Tidier-upper for generated text
*   inception-date: Nov 2014
*   development-stage: mature

T-Rext is a command-line filter that attempts to clean up spaces and
punctuation in a text file.  Its purpose is so that, when you are writing
a text generator, such as a Markov processor, you need not worry too much
about its output format; just toss its output through T-Rext when you're
done to make it more presentable.

#### Implementation: t-rext (Python)

*   reference: true
*   in-distribution: T-Rext distribution
*   license: Public Domain
*   host-language: Python

### yucca

*   summary: Static analyzer for 8-bit BASIC programs
*   inception-date: 2012

`yucca` is a dialect-agnostic static analyzer for 8-bit BASIC
programs.  It can find `GOTO`'s and `GOSUB`'s
which refer to non-existent line numbers, or line numbers which contain
only a `REM`, among a few other modest features.

#### Implementation: yucca (Python)

*   reference: true
*   in-distribution: yucca distribution
*   license: MIT license
*   host-language: Python

Forked Tools
------------

### ee

*   development-stage: mature
*   no-specification: true
*   distribution: [ee distribution](/distribution/ee distribution)

`ee` is the "easy editor" which comes with [[FreeBSD]].

### tideay

*   authors: Paul Harrison, Chris Pressey
*   inception-date: Apr 2013
*   development-stage: work in progress

`tideay` is Cat's Eye Technologies' fork of `yaedit`, a GtkSourceView-based
text editor written by Paul Harrison.  In addition to the
features provided by `yaedit`, `tideay` supports things such as
string-rewriting-based editing commands.

#### Implementation: tideay (Python)

*   reference: true
*   in-distribution: tideay distribution
*   license: GPL
*   host-language: Python

Archival Tools
--------------

### mzstorkipiwanbotbotbot

*   inception-date: 2010
*   development-stage: archival

An IRC bot with no purpose or plan.

#### Implementation: mzstorkipiwanbotbotbot (Lua)

*   reference: true
*   in-distribution: mzstorkipiwanbotbotbot distribution
*   license: Public Domain
*   host-language: Lua

#### Implementation: Rtype

*   in-distribution: mzstorkipiwanbotbotbot distribution
*   license: Public Domain
*   host-language: R

### Rooibos

*   summary: Simple, single-module parser combinator library
*   inception-date: '2011'
*   development-stage: archival

Rooibos is a parser combinator library for Python. Modelled somewhat
after yeanpypa (self-contained, public domain), but compensates for what
I considered a fatal flaw in yeanpypa (no good way to describe a
recursive grammar.) Has a fatal flaw of its own (can only parse
strictly LL(1) grammars — no backtracking is yet possible.) Originally
used in [Eightebed][], but provided here for ease of transplanting into
other projects.

#### Implementation: rooibos.py

*   reference: true
*   in-distributions: Eightebed distribution
*   license: Public Domain
*   host-language: Python

### TPiS

*   subtitle: **Total Procedures in Scheme**
*   summary: Totality-checker for Scheme procedures
*   inception-date: ca 2006
*   development-stage: archival

This is a static analyzer, written in Scheme, which can check if
given Scheme procedures are total (always terminate, on any input) by
checking that they are specified primitive-recursively.  What's more, it
is written almost entirely in a primitive-recursive style, so it can
check itself!

#### Implementation: TPiS (Scheme)

*   reference: true
*   in-distribution: TPiS distribution
*   license: BSD license
*   host-language: Scheme

[Eightebed]: http://catseye.tc/node/Eightebed

