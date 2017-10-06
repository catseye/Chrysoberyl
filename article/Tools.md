Tools
=====

Note that the precise distinctions between a Tool, a Platform, and a Library are debatable,
and entries may be categorized somewhat arbitrarily.

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

### Falderal

*   subtitle: **Literate Testing for Languages**
*   inception-date: 2011

Falderal is a file format for literate test suites.  It is particularly
suited for documenting programming languages (or other specifications of
ways to transform text) and testing their implementation(s) in a
language-agnostic fashion.  The dumbed-down sound-bite version:
"doctests for DSLs".  It can be embedded in both Markdown and Literate
Haskell.

#### Implementation: py-falderal

*   reference: true
*   in-distribution: Falderal distribution
*   generally-recommended: true
*   license: BSD license
*   host-language: Python

#### Implementation: Test.Falderal

*   in-distribution: 'Falderal distribution'
*   license: BSD license
*   host-language: Haskell

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
