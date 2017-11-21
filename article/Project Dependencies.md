Project Dependencies
====================

These are the things you might need to use the things produced by
Cat's Eye Technologies.  I mean software.

To start, you usually need a relatively Unix-like environment.  That could
be Linux or FreeBSD.  These days, it could probably be MacOS.  On Windows,
Cygwin or SFU or whatever does that these day might be enough.

It should be noted that [The Cat's Eye Technologies Platform][], which is
based on NetBSD, was put together specifically for this purpose.  It should
work on QEMU or other x86-based IBM PC-architecture emulators, and possibly
even on x86-based IBM PCs, if they can run NetBSD.

Stuff written in compiled languages needs to be built before it can run.

This is a work-in-progress.  It doesn't really include [Retrocomputing][]
but it probably should.

Languages
---------

### ANSI C

*   specification-link: http://clc-wiki.net/wiki/C89

ANSI C

### C99

*   specification-link: http://www.open-std.org/jtc1/sc22/WG14/www/docs/n1256.pdf

C99

### Perl

*   specification-link: http://www.perl.org/

Perl

### Erlang

*   specification-link: http://www.erlang.org/

Erlang

### Python

*   specification-link: http://www.python.org/

Python

### Bourne shell

*   specification-link: http://steve-parker.org/sh/bourne.shtml

Bourne shell

### Lua

*   specification-link: http://lua.org/

Lua

### Javascript

*   specification-link: http://www.ecma-international.org/publications/standards/Ecma-262.htm

Javascript

### Scheme

*   specification-link: http://schemers.org/Documents/Standards/R5RS/
*   suggested-implementation: http://justinethier.github.io/husk-scheme/

R5RS Scheme

### Ophis

*   specification-link: https://github.com/michaelcmartin/Ophis

An assembler (and its concomitant assembly language) for the 6502 and related
processors, which some of our 6502 code is written in.

### BASIC

*   specification-link: http://en.wikipedia.org/wiki/BASIC

### Haskell

*   specification-link: https://www.haskell.org/

Haskell

### Java

*   specification-link: http://www.oracle.com/technetwork/java/index.html

Java

Tools and Libraries
-------------------

### make

*   specification-link: http://pubs.opengroup.org/onlinepubs/009695399/utilities/make.html
*   suggested-implementation: http://www.gnu.org/software/make/

make is a tool for orchestrating builds.

### Parsec

*   specification-link: http://legacy.cs.uu.nl/daan/parsec.html
*   suggested-implementation: http://hackage.haskell.org/package/parsec-3.1.1

Parsec is a parser combinator library for Haskell.

### realpath

*   specification-link: N/A
*   suggested-implementation: http://catseye.tc/distribution/realpath_distribution

`realpath` is a tool that reports the real, symbolic-link-free path
for a filepath which may contain symbolic links.

Interfaces
----------

### ANSI Terminal

*   specification-link: http://www.ecma-international.org/publications/standards/Ecma-048.htm

When a project claims it needs this to run, it needs to run in a terminal which understand
the ANSI terminal control codes (more formally known as "ECMA-48") in
order for their output to be intelligible. Almost all modern consoles
and terminal emulators understand these codes, sometimes under the guise
of a particular terminal standard which includes them, such as `vt100`
or `vt220`. For older MS-DOS systems, a driver such as `ANSI.SYS` may
need to be loaded.

[Retrocomputing]: ../article/Retrocomputing.md
