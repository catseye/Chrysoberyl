Project Dependencies
====================

This document lists the software you might need to run the software produced by
Cat's Eye Technologies.  This includes interpreters and compilers for the
programming languages our projects are written in, the platforms or operating
systems that they run on, and libraries and tools they might require when run.

It should be noted that [The Cat's Eye Technologies Platform][] was started
specifically to provide a platform where most all of Cat's Eye Technologies'
software projects can run.  Therefore this document may refer to that project
in many places.

Languages
---------

### ANSI C

*   specification-link: http://clc-wiki.net/wiki/C89

Many of our C programs are written in C89, also colloquially known as "ANSI C".
This is supported by many C compilers.  Indeed, many C compilers understand
an `-ansi` flag, as well as a `-pedantic` flag which makes them stick more
closely to the letter of the ANSI C spec.

Some of our projects can be compiled as either ANSI C or [C99][].  Often, ANSI C
selectable by setting the environment variable `ANSI` to `YES` while running
the build command (which is often `make`.)

### C99

*   specification-link: http://www.open-std.org/jtc1/sc22/WG14/www/docs/n1256.pdf

The disadvantage of ANSI C is that it defines only a very crude model of the world
surrounding the program, and how the program can interact with it.  For example,
a program can sleep, but with coarse granularity; it cannot sleep for less than 1
second.  Interfaces and extensions that were added to various vendors' C language
since ANSI C were collected into a new standard called C99, which improved on this.

Telling a C compiler that it should treat its input files as C99 is often done
with a flag such as `-std=c99`.

Some of our projects can be compiled as either C99 or [ANSI C][].  Often, C99 is
the default, and ANSI C, if desired. must be selected explicitly when building.

### Perl

*   specification-link: http://www.perl.org/

Our Perl projects are written in Perl 5.  For more precise version numbers they have
been tested on, see [The Cat's Eye Technologies Platform][].

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

Our Python projects are written in Python 2.7.  For more precise version numbers
they have been tested on, see [The Cat's Eye Technologies Platform][].

### Bourne shell

*   specification-link: http://steve-parker.org/sh/bourne.shtml

We try to write our Bourne shell scripts to run on plain Bourne shell — nothing
`bash`-specific.  We try to test them on NetBSD for this purpose.  As such, they
run on the version of `sh` that ships with NetBSD 6 (which might be `ash`.)
For more precise version numbers they have been tested on,
see [The Cat's Eye Technologies Platform][].

### Lua

*   specification-link: http://lua.org/

Our Lua projects (barring any that may be in archived projects) are written in Lua 5.1
and tested with Lua 5.1.4.

Note that the 5.1.x series of Lua is not generally compatible with the 5.0.x series.

### Javascript

*   specification-link: http://www.ecma-international.org/publications/standards/Ecma-262.htm

There is no implementation of Javascript bundled with [The Cat's Eye Technologies Platform][].
Some of our Javascript scripts are "universal" and will run under `nodejs`, but we don't have
a versioning plan for those yet.  Most of our Javascript is intended to run in the browser and
is simply kept reasonably up-to-date with current browsers.  (At any given time, your mileage
may of course vary.)

For laughs, here are some old Javascript links that still work:

*   [JavaScript at quirksmode](http://www.quirksmode.org/js/contents.html)
*   [Speed Up Your Javascript Load Time](https://betterexplained.com/articles/speed-up-your-javascript-load-time/)

### Scheme

*   specification-link: http://schemers.org/Documents/Standards/R5RS/
*   suggested-implementation: http://justinethier.github.io/husk-scheme/

Our Scheme projects are generally written in vanilla R5RS Scheme.
Sometimes even R4RS Scheme.  (And it should be noted that this is
like saying "ATM Machine".  But the alternatives all sound worse.)
For more precise version numbers they have been tested on, see
[The Cat's Eye Technologies Platform][].

### Ophis

*   specification-link: https://github.com/michaelcmartin/Ophis

Ophis is an assembler (and its concomitant assembly language) for the 6502 and related
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

BASIC.  TODO: This needs to be more specific.  Some of our projects are
written in Commodore BASIC 2.0.  Others are written in Applesoft BASIC.

### Haskell

*   specification-link: https://www.haskell.org/

Haskell is a lazy functional language.

Some ancient links that still work:

*   [A Haskell regular expression tutorial](http://www.serpentine.com/blog/2007/02/27/a-haskell-regular-expression-tutorial/)

#### Implementation: ghc

*   home-page: http://www.haskell.org/ghc/
*   license: BSD-compatible
*   implementation-type: compiler
*   host-language: [Haskell][]
*   target-language: native code

The Glasgow Haskell Compiler is dangerously close to being "the" implementation of Haskell.

It also has an interpreter, `ghci`.

#### Implementation: hugs

*   home-page: http://www.haskell.org/hugs/
*   license: [BSD-compatible](https://www.haskell.org/hugs/pages/users_guide/license.html)
*   implementation-type: interpreter
*   host-language: [C99][]

`hugs` is a Haskell interpreter.  It's used in [The Cat's Eye Technologies Platform][] because,
being written in C, it builds on NetBSD.  (Boostrapping `ghci` there would, I imagine,
be quite cumbersome.)

### Java

*   specification-link: https://docs.oracle.com/javase/specs/

Our Java projects are, as far as I can recall, written in Java 1.6.  They have not been tested
recently, but when they were, it might have been under the Java SE 6 JDK 1.6.0.

An implementation of Java is *not* included with The Platform.

Generally, we're trying to migrate away from it.  [Etcha][] was originally written
in Java, but it now has a second implementation in Javascript.  ([Whothm][] needs
to go this way too.)  [yoob][] is written in Java, but I don't think any of our
languages is implemented solely in yoob anymore.

Our few installations that are Java Applets have been converted into Java Web Start
applications, since Java Applets are on the obsolescence track.

If you want to try installing a Java Runtime, you can apparently
[download a Java Runtime](http://www.oracle.com/technetwork/java/javase/downloads/index.html),
after you have agreed to the "Oracle Binary Code License Agreement for Java SE".

### Ruby

*   specification-link: http://www.ruby-lang.org/

Some of our projects have some stuff written in Ruby — we implemented
[Thue][] in Ruby, and [Castile][] can output Ruby — but nothing we've
written *relies* on Ruby.  (The original version of [Velo][] was written
in Ruby, but it was re-implemented in [Lua][].)

Therefore an implementation of Ruby is *not* included with The Platform.

But the Ruby things should run in Ruby 1.8 or 1.9 or thereabouts, which
you could once have downloaded [here](http://www.ruby-lang.org/en/downloads/) if you
agreed to this [BSD-compatible license](http://www.ruby-lang.org/en/about/license.txt)
but apparently 1.9 is just too old and not maintained anymore.

Anyway, here is [a fairly good Ruby tutorial](http://www.fincher.org/tips/Languages/Ruby/).

Tools and Libraries
-------------------

### make

*   specification-link: http://pubs.opengroup.org/onlinepubs/009695399/utilities/make.html
*   suggested-implementation: http://www.gnu.org/software/make/

`make` is a tool for orchestrating builds.

### Parsec

*   specification-link: http://legacy.cs.uu.nl/daan/parsec.html
*   suggested-implementation: http://hackage.haskell.org/package/parsec-3.1.1

Parsec is a parser combinator library for Haskell.

### realpath

*   specification-link: N/A
*   suggested-implementation: http://catseye.tc/distribution/realpath_distribution

`realpath` is a tool that reports the real, symbolic-link-free path
for a filepath which may contain symbolic links.

I'm not sure if it's part of any standard, but it really should be, because it's
very useful in scripts.  It does come bundled with many Linux distributions,
but not with NetBSD, so for The Platform, we wrote
[our own implementation](http://catseye.tc/distribution/realpath_distribution) in [Python][].

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

[The Cat's Eye Technologies Platform]: ../article/Platforms.md#the-cats-eye-technologies-platform
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[C99]: ../article/Project%20Dependencies.md#c99
[MS-DOS]: ../article/Retrocomputing.md#ms-dos
[Haskell]: ../article/Project%20Dependencies.md#haskell
[Python]: ../article/Project%20Dependencies.md#python
[Etcha]: ../article/Languages.md#etcha
[Whothm]: ../article/Languages.md#whothm
[yoob]: ../article/Archived.md#yoob
[Thue]: http://esolangs.org/wiki/Thue
[Castile]: ../article/Languages.md#castile
[Velo]: ../article/Languages.md#velo
[Lua]: ../article/Project%20Dependencies.md#lua

