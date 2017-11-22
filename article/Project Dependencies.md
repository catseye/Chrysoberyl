Project Dependencies
====================

These are the things you might need to use the things produced by
Cat's Eye Technologies.  I mean software — the interpreters and
compilers for the programming languages our projects are written
in, and the platforms or operating systems that they run on.

It should be noted that [The Cat's Eye Technologies Platform][], which is
based on NetBSD, was put together specifically for this purpose.  Most of
the dependency versions listed below, are the same as those in The Platform
(suggesting that this document may merge with The Platform somehow in the future.)
The Platform runs under QEMU, and possibly under other x86-based
IBM PC-architecture emulators, and possibly even on actual x86-based computers,
if they can run NetBSD.

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

Our Erlang projects are written in Erlang R16 and tested with
Erlang/OTP R16B03-1.

Note that this is a pretty old version of Erlang at this point.

Note that compiled Erlang modules are `.beam` files in the `ebin`
directory. The source code lives in the `src` directory, and an Erlang
compiler (such as the one which ships with Erlang/OTP) is required to
build the modules.

Also note that the `.beam` files will have to be recompiled in order to
run under recent versions (e.g. R13B) of Erlang/OTP, as the
binary format has changed.

Also note there is a good chance that the sources will compile and run
on an older version (say, R9C) of Erlang/OTP, but you may need
to make some manual changes and system setup.

### Python

*   specification-link: http://www.python.org/

Our Python code is written in Python 2.7.x.

### Bourne shell

*   specification-link: http://steve-parker.org/sh/bourne.shtml

Bourne shell

### Lua

*   specification-link: http://lua.org/

Our Lua projects (barring any that may be in archived projects) are written in Lua 5.1
and tested with Lua 5.1.4.

Note that the 5.1.x series of Lua is not generally compatible with the 5.0.x series.

### Javascript

*   specification-link: http://www.ecma-international.org/publications/standards/Ecma-262.htm

Javascript

### Scheme

*   specification-link: http://schemers.org/Documents/Standards/R5RS/
*   suggested-implementation: http://justinethier.github.io/husk-scheme/

Our Scheme projects are generally written in vanilla R5RS Scheme and
are tested with CHICKEN Scheme 4.9.0.1.

### Ophis

*   specification-link: https://github.com/michaelcmartin/Ophis

An assembler (and its concomitant assembly language) for the 6502 and related
processors, which some of our 6502 code is written in.

### NASM

*   specification-link: http://nasm.us/

In our projects, many of these NASM files were converted from older
assembly-language sources written in the syntax of Turbo Assembler 3.1
(an old-school x86 assembler for [MS-DOS][], written by Borland.)
In some cases the Turbo Assembler sources are still included in the
project for historical interest, but the newer NASM sources are what
the binaries should be built from.

### BASIC

*   specification-link: http://en.wikipedia.org/wiki/BASIC


### Haskell

*   specification-link: https://www.haskell.org/

Haskell is a lazy functional language.

#### Implementation: ghc

*   home-page: http://www.haskell.org/ghc/
*   license: BSD-compatible
*   implementation-type: compiler
*   host-language: [Haskell][]
*   target-language: native code

The Glasgow Haskell Compiler is dangerously close to being "the" implementation of Haskell.

#### Implementation: hugs

*   home-page: http://www.haskell.org/hugs/
*   license: [BSD-compatible](https://www.haskell.org/hugs/pages/users_guide/license.html)
*   implementation-type: interpreter
*   host-language: [C99][]

`hugs` is a Haskell interpreter.  It's used in The Platform because,
being written in C, it builds on NetBSD.

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

[Retrocomputing]: http://catseye.tc/article/Retrocomputing
[MS-DOS]: TBD
[Haskell]: TBD
[C99]: TBD
