Project Dependencies
====================

This document lists the software you might need to run the software produced by
Cat's Eye Technologies.  This includes interpreters and compilers for the
programming languages our projects are written in, the platforms or operating
systems that they run on, and libraries and tools they might require when run.

Some of these dependencies might be technologies which are, nowadays,
considered historical.  Legacy.  Retro.  Vintage.  *Old*.  These dependencies
are listed at the bottom of this article, under
[Retro Dependencies](#retro-dependencies) and [Retro Languages](#retro-languages).
For more information about Retrocomputing at Cat's Eye Technologies, see the
[Retrocomputing](../article/Retrocomputing.md) article.

Languages
---------

### ANSI C

*   specification-link: [ANSI C89 documents](http://port70.net/~nsz/c/c89/)

Many of our C programs are written in C89, also colloquially known as "ANSI C".
This is supported by many C compilers.  Indeed, many C compilers understand
an `-ansi` flag, as well as a `-pedantic` flag which makes them stick more
closely to the letter of the ANSI C spec.

Some of our projects can be compiled as either ANSI C or [C99][].  Often, ANSI C
is selectable by setting the environment variable `ANSI` to `YES` while running
the build command (which is often `make`.)

An older but still interesting link: [C89 at clc-wiki](http://clc-wiki.net/wiki/C89).

### C99

*   specification-link: [ANSI C99 documents](http://port70.net/~nsz/c/c99/)

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

*   specification-link: [Perl.org](http://www.perl.org/)

Our Perl projects are written in Perl 5.  For more precise version numbers they have
been tested on, see [The Cat's Eye Technologies Platform][].

### Python

*   specification-link: [Python.org](http://www.python.org/)

Our Python projects are written in Python 2.7.  Some of them (especially tools)
are written so that they run under both Python 2.7 and Python 3.4.  For more precise
version numbers they have been tested on, see [The Cat's Eye Technologies Platform][].

### Lua

*   specification-link: [Lua.org](http://lua.org/)

Lua is a lightweight scripting language.

Our Lua projects (barring any that may be in archived projects) are written in Lua 5.1
and tested with Lua 5.1.4.

Note that the 5.1.x series of Lua is not generally compatible with the 5.0.x series.
(On the other hand, our 5.1 code appears compatible with 5.2 and 5.3, but we have not
audited it.)

For running Lua programs on a web page, we use [Fengari](https://fengari.io/), a Lua
VM written in Javascript.

### Scheme

*   specification-link: [R5RS documents](http://schemers.org/Documents/Standards/R5RS/)
*   suggested-implementation: [Husk Scheme](http://justinethier.github.io/husk-scheme/)

Our Scheme projects are generally written in vanilla R5RS Scheme.
Sometimes even R4RS Scheme.  (And it should be noted that this is
like saying "ATM Machine".  But the alternatives all sound worse.)
For more precise version numbers they have been tested on, see
[The Cat's Eye Technologies Platform][].

### Haskell

*   specification-link: [Haskell.org](https://www.haskell.org/)

Haskell is a lazy functional language.

Some ancient links that still work:

*   [A Haskell regular expression tutorial](http://www.serpentine.com/blog/2007/02/27/a-haskell-regular-expression-tutorial/)

#### Implementation: ghc

*   home-page: [https://www.haskell.org/ghc/](https://www.haskell.org/ghc/)
*   license: BSD-compatible
*   implementation-type: compiler
*   host-language: [Haskell][]
*   target-language: native code

The Glasgow Haskell Compiler is dangerously close to being "the" implementation of Haskell.

It also has an interpreter, `ghci`.

#### Implementation: hugs

*   home-page: [https://www.haskell.org/hugs/](https://www.haskell.org/hugs/)
*   license: [BSD-compatible](https://www.haskell.org/hugs/pages/users_guide/license.html)
*   implementation-type: interpreter
*   host-language: [C99][]

`hugs` is a Haskell interpreter.  It's used in [The Cat's Eye Technologies Platform][] because,
being written in C, it builds on NetBSD.  (Boostrapping `ghci` there would, I imagine,
be quite cumbersome.)

### Erlang

*   specification-link: [Erlang.org](http://www.erlang.org/)

Our Erlang projects are written in Erlang R16 and tested with
Erlang/OTP R16B03-1.

Note that this is a pretty old version of Erlang at this point.

Note that the following paragraphs are sorely out of date.

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

### Bourne shell

*   specification-link: [An Introduction to the Unix Shell](http://steve-parker.org/sh/bourne.shtml)

We try to write our Bourne shell scripts to run on plain Bourne shell — nothing
`bash`-specific.  We try to test them on NetBSD for this purpose.  As such, they
run on the version of `sh` that ships with NetBSD 6 (which might be `ash`.)
For more precise version numbers they have been tested on,
see [The Cat's Eye Technologies Platform][].

### NASM

*   specification-link: [NASM.us](http://nasm.us/)

In our projects, many of these NASM files were converted from older
assembly-language sources written in the syntax of Turbo Assembler 3.1
(an old-school x86 assembler for [MS-DOS][], written by Borland.)
In some cases the Turbo Assembler sources are still included in the
project for historical interest, but the newer NASM sources are what
the binaries should be built from.

### Javascript

*   specification-link: [ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)

There is no implementation of Javascript bundled with [The Cat's Eye Technologies Platform][].
Some of our Javascript scripts are "universal" and will run under `nodejs`, but we don't have
a versioning plan for those yet.  Most of our Javascript is intended to run in the browser and
is simply kept reasonably up-to-date with current browsers.  (At any given time, your mileage
may of course vary.)

For laughs, here are some old Javascript links that still work:

*   [JavaScript at quirksmode](http://www.quirksmode.org/js/contents.html)
*   [Speed Up Your Javascript Load Time](https://betterexplained.com/articles/speed-up-your-javascript-load-time/)

### Java

*   specification-link: [Java SE specs — docs.oracle.com](https://docs.oracle.com/javase/specs/)

Our Java projects are, as far as I can recall, written in Java 1.6.  They have not been tested
recently, but when they were, it might have been under the Java SE 6 JDK 1.6.0.

An implementation of Java is *not* included with
[The Cat's Eye Technologies Platform][].

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

*   specification-link: [Ruby-lang.org](http://www.ruby-lang.org/)

Some of our projects have some stuff written in Ruby — we implemented
[Thue][] in Ruby, and [Castile][] can output Ruby — but nothing we've
written *relies* on Ruby.  (The original version of [Velo][] was written
in Ruby, but it was re-implemented in [Lua][].)

Therefore an implementation of Ruby is *not* included with
[The Cat's Eye Technologies Platform][].

But the Ruby things should run in Ruby 1.8 or 1.9 or thereabouts, which
you could once have downloaded [here](http://www.ruby-lang.org/en/downloads/) if you
agreed to this [BSD-compatible license](http://www.ruby-lang.org/en/about/license.txt)
but apparently 1.9 is just too old and not maintained anymore.

Anyway, here is [a fairly good Ruby tutorial](http://www.fincher.org/tips/Languages/Ruby/).

### Ophis Assembler

*   specification-link: [michaelcmartin/Ophis](https://github.com/michaelcmartin/Ophis)

Ophis is an assembler (and its concomitant assembly language) for the [6502][] and related
processors, which some of our 6502 code is written in.

Tools and Libraries
-------------------

### make

*   specification-link: [POSIX make](http://pubs.opengroup.org/onlinepubs/009695399/utilities/make.html)
*   suggested-implementation: [GNU make](http://www.gnu.org/software/make/)

`make` is a tool for orchestrating builds.

### Parsec

*   specification-link: [Parsec — Haskell wiki](https://wiki.haskell.org/Parsec)
*   suggested-implementation: [parsec-3.1.1](http://hackage.haskell.org/package/parsec-3.1.1)

Parsec is a parser combinator library for Haskell.

### realpath

*   specification-link: N/A
*   suggested-implementation: [catseye/realpath](https://catseye.tc/distribution/realpath_distribution)

`realpath` is a tool that reports the real, symbolic-link-free path
for a filepath which may contain symbolic links.

I'm not sure if it's part of any standard, but it really should be, because it's
very useful in scripts.  It does come bundled with many Linux distributions,
but not with NetBSD, so for [The Cat's Eye Technologies Platform][], we wrote
[our own implementation](https://catseye.tc/distribution/realpath_distribution) in [Python][].

Interfaces
----------

### ANSI Terminal

*   specification-link: [ECMA-48](http://www.ecma-international.org/publications/standards/Ecma-048.htm)

When a project claims it needs this to run, it needs to run in a terminal which understand
the ANSI terminal control codes (more formally known as "ECMA-48") in
order for their output to be intelligible. Almost all modern consoles
and terminal emulators understand these codes, sometimes under the guise
of a particular terminal standard which includes them, such as `vt100`
or `vt220`. For older [MS-DOS][] systems, a driver such as `ANSI.SYS` may
need to be loaded.

Music Formats
-------------

Here are various formats in which the [Musical Compositions][] have been recorded,
and/or software that plays and/or edits music in these formats.  Indeed, sometimes
the format is named after the software.

### SID Player

*   specification-link: ???

This was a popular(?) music format for the [Commodore 64][].  There was an editor for
this format called SID Editor, which was written largely in [Commodore BASIC 2.0][]
(there were some machine-language subroutines, but it was largely BASIC.)

### MIDI

*   specification-link: [Standard MIDI Files](https://www.midi.org/specifications/category/smf-specifications)
*   wikipedia: [MIDI](https://en.wikipedia.org/wiki/MIDI)

This one's pretty well standardized, I think.

I did a lot of MIDI sequencing with a Roland JV-30 and Cakewalk, back in the Windows 95 era.

MIDI files can be rendered to digital audio using a "soundfont" such as "freepats" and a
renderer like [TiMidity++][].

### DMCS

*   specification-link: None
*   wikipedia: [Deluxe_Music_Construction_Set](https://en.wikipedia.org/wiki/Deluxe_Music_Construction_Set)

By Electronic Arts.  For the Amiga and the Apple Macintosh.

It could export to MIDI.

### Noisetracker MOD

*   specification-link: [Noisetracker/Soundtracker/Protracker Module Format, 4th revision](https://www.aes.id.au/modformat.html)
*   wikipedia: [MOD (file format)](https://en.wikipedia.org/wiki/MOD_(file_format))

This is what we talk about when we talk about MOD files, I think.

There's an open-source audio player called [xmp][] that can play MED, Noisetracker MOD,
and many other formats.

### MED

*   specification-link: [MED/OctaMED MMD0 and MMD1 file formats](http://www.textfiles.com/programming/FORMATS/med-form.txt)

Amiga.  The editor is called MED.  There was a MED Player.

MED has a "transpose" command, but not all players honour it, and when they don't,
well, one of the voices is in the wrong key.

There's an open-source audio player called [xmp][] that can play MED, Noisetracker MOD,
and many other formats.

### Sonant Tracker Format

*   specification-link: [sonantlive.bitsnbites.eu](http://sonantlive.bitsnbites.eu/)

[Sonant Live][] runs in a browser (Javascript and HTML5) and synthesizes its voices.
There is also a [Sonant Tracker][] which uses the same format and runs on Windows.

Retro Dependencies
------------------

### Apple II

*   specification-link: [Apple II](https://en.wikipedia.org/wiki/Apple_II)
*   wikipedia: [Apple II](https://en.wikipedia.org/wiki/Apple_II)

Rundown: The Apple II series of microcomputers included the Apple ][+ and Apple //e.
The CPU was a 6502.  [Applesoft BASIC][] was often in the ROM, but it could have been
loaded from tape or disk.

Emulators: [AppleWin](https://www.zophar.net/apple2/applewin.html) is an emulator for the Apple II, built for Windows,
written in C++ and distributed under the GPL.  [linapple][]
is a port of AppleWin to Linux.  [zophar.net](http://www.zophar.net/apple2.html) has a list of other emulators.

### Commodore VIC-20

*   specification-link: [Commodore VIC-20](https://en.wikipedia.org/wiki/Commodore_VIC-20)
*   wikipedia: [Commodore VIC-20](https://en.wikipedia.org/wiki/Commodore_VIC-20)

Rundown: The CPU was a 6502.  [Commodore BASIC 2.0][] was in the ROM; this is the same BASIC that was
in the Commodore 64.

Emulators: The `xvic` executable from [VICE][], written in C99 and
distributed under the GPL, is a generally recommended emulator for the VIC-20.

### Commodore 64

*   specification-link: [Commodore 64 Programmer's Reference Guide](https://www.commodore.ca/manuals/c64_programmers_reference/c64-programmers_reference.htm)
*   wikipedia: [Commodore 64](https://en.wikipedia.org/wiki/Commodore_64)

Rundown: The CPU was a 6510, which was a slightly modified 6502.  [Commodore BASIC 2.0][] was in the ROM;
this is the same BASIC that was in the VIC-20.
The [Commodore 64 Programmer's Reference Guide][] is an invaluable reference, or is it merely a guide?
There was also a [User's Guide](https://www.commodore.ca/manuals/c64_users_guide/c64-users_guide-00-toc_introduction.pdf).
Lots of C64 stuff can also be found at [zimmers.net](http://www.zimmers.net/anonftp/pub/cbm/).

Emulators: The `x64` executable from [VICE][], written in C99 and
distributed under the GPL, is a generally recommended emulator for the Commodore 64.
Also, [JaC64][] is a GPL Java application which emulates a Commodore 64.
Cat's Eye Technologies uses it to showcase our Commodore 64 games as online installations, using Java Web Start.
We forked it to fix some bugs and because mainline development seemed stalled.

### 6502

*   specification-link: [MOS Technologies' 1976 manual for the 650x series](http://bytecollector.com/archive/misc/6500-50A_MCS6500pgmManJan76.pdf)
*   wikipedia: [MOS Technology 6502](https://en.wikipedia.org/wiki/MOS_Technology_6502)

The common thread of the above 3 architectures is that they all have a 6502 processor.

Some things Cat's Eye Technologies has done (namely [SixtyPical][] and [SITU-SOL][])
have been 6502-specific, but not specific to any one computer architecture.

There are also a couple of C compilers that target 6502, famously [cc65](http://cc65.github.io/cc65/),
but also [scc6502, a Small-C for 6502 and LUnix](https://web.archive.org/web/20110106052323/http://www.reocities.com/SiliconValley/Way/4588/scc6502.html).

### Amiga 500

*   specification-link: [Amiga 500](https://en.wikipedia.org/wiki/Amiga_500)
*   wikipedia: [Amiga 500](https://en.wikipedia.org/wiki/Amiga_500)

Rundown: The CPU was a Motorola 68000, but this could be upgraded to a 68020, etc
(and needed to be if you wanted memory protection).  It had many custom chips
with colourful names such as "Angus" and "Paula".

AmigaDOS 1.3 (with a [manual online here](http://www.pagetable.com/docs/amigados_tripos/amigados_manual.pdf))
was the version of Amiga's operating system which was current when the Amiga 500
was a really popular home computer — mostly for video games, but also for graphics
and video processing, such as ray-tracing and animation.

AmigaBasic was the name of the "advanced" variant of BASIC that shipped with
AmigaDOS.  It was developed by Microsoft.

Emulators: There's an emulator for the Amiga 500 architecture (and several other models such as the Amiga 2000)
called UAE.  It's written in C++ and available under the GPL, and while the build of it for windows,
[WinUAE](http://www.winuae.net/), seems basically stable, every decade or so the Unix version gets forked into
a new incarnation.  A few years ago, [E-UAE](http://www.rcdrummond.net/uae/) was the thing to use, but now it's
apparently [FS-UAE](https://fs-uae.net/).  Last I tried it, E-UAE still worked for me, but I have had mixed
experiences trying to build it over the years.

### IBM PC compatible

*   specification-link: [IBM PC compatible](https://en.wikipedia.org/wiki/IBM_PC_compatible)
*   wikipedia: [IBM PC compatible](https://en.wikipedia.org/wiki/IBM_PC_compatible)

Rundown: The CPU was a 8086, or 80286, 80386, 80486... or just ["X86"](https://en.wikipedia.org/wiki/X86).
Or ["IA-32"](http://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-1-manual.html).
Until you get to the 64-bit architectures — but that's not retrocomputing
anymore.  (yet.)

For any Cat's Eye Technologies project that claims to run on an "IBM PC compatible,"
probably a 486 with a BIOS, keyboard, and basic VGA is the minimum to make it worthwhile.

Some modern PC's can handle running that sort of legacy setup, but most don't.
Or at least, I wouldn't risk it anymore.  Better to run it under an emulator.

Two good emulators are:

*   [v86](https://github.com/copy/v86) -- BSD licensed, written in [Javascript][],
    runs in a web browser.
*   [QEMU](http://www.qemu-project.org/) -- GPL v2 licensed, written in [C++][],
    runs on your desktop.  QEMU can actually emulate more architectures
    than just the IBM PC.

For more in-depth information on this wonderful architecture,
see [Blurry Memories of DOS Programming][].

### MS-DOS

*   specification-link: [Microsoft/MS-DOS](https://github.com/Microsoft/MS-DOS)
*   wikipedia: [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS)

Rundown: By [Microsoft](http://microsoft.com/).
Can run `.BAT` files.  And x86 machine code `.COM` files.

[DJGPP](http://www.delorie.com/djgpp/) is a port of GCC to MS-DOS.
Here is a random [MS-DOS game programming link](http://ftp.lanet.lv/ftp/mirror/x2ftp/msdos/programming/).

I wouldn't assume any modern Windows installation can handle running MS-DOS
programs directly anymore.  Better to run it under an emulator.

Emulators: there are a few recommended choices here:

*   [DOSBox](http://www.dosbox.com/) (written in C++, under the GPL)
    is an emulator, available for many systems, which
    simulates both an [IBM PC compatible][] and
    MS-DOS on top of it.  It should be plenty sufficient for running
    DOS-based software found here.
*   There's a good free DOS clone called [FreeDOS](http://www.freedos.org/)
    which is written in (I'm guessing) C99 and assembler and distributed under
    the GPL.  It is not, by itself, an emulator though, and you'll need
    to run it under an [IBM PC compatible][] emulator such as those listed above.

For more in-depth information on programming for this wonderful operating system,
see [Blurry Memories of DOS Programming][].

Any Cat's Eye Technologies project which claims to need MS-DOS only needs
something which emulates MS-DOS sufficiently well. This includes both the
standard DOS `INT 21h` handler, and the standard DOS utilies like, for example,
`TYPE` and `DEBUG.COM`.

(There are only two projects of Cat's Eye Technologies' that
require MS-DOS (or a compatible operating system) anymore, and
these dependencies are only partial.)

### Z80

*   specification-link: [Z80 Family CPU User Manual](http://z80.info/zip/z80cpu_um.pdf)
*   wikipedia: [Zilog Z80](https://en.wikipedia.org/wiki/Zilog_Z80)

The Z80 is another 8-bit CPU that was popular.

Here are some links:

*   [Home of the Z80 CPU](http://www.z80.info/) — Lots of useful Z80 information, plus a clock circuit
*   [TI-85 Assembler Programming](http://www.sealiesoftware.com/ti-asm/) — Z80 tutorial for the TI-85 calculator
*   [Opening up Microchips](http://zeptobars.ru/en/read/open-microchip-asic-what-inside-II-msp430-pic-z80) — Innards of a Z80, and more

### Z-Machine

*   specification-link: [The Z-Machine Standards Document](http://inform-fiction.org/zmachine/standards/z1point0/index.html)
*   wikipedia: [Z-machine](https://en.wikipedia.org/wiki/Z-machine)

It's actually a virtual machine designed by Infocom so they could port their interactive
fiction onto a multitude of home computers.

Here are its [specifications documents](http://inform-fiction.org/zmachine/standards/).

Emulators: [ZPlet][] is a Java application which emulates a Z-Machine.
There are other, much better emulators, such as [Frotz][].

Retro Languages
---------------

### BASIC

*   specification-link: [Entry on BASIC at Wikipedia](https://en.wikipedia.org/wiki/BASIC)

There are lots and lots and lots of variants of BASIC.  Some of our projects are
written in [Commodore BASIC 2.0][].  Others are written in [Applesoft BASIC][].

### Commodore BASIC 2.0

*   specification-link: [Entry on BASIC at c64-wiki](https://www.c64-wiki.com/wiki/BASIC)

The dialect of BASIC that shipped with the [Commodore 64][] and [Commodore VIC-20][].

### Applesoft BASIC

*   specification-link: [Entry on Applesoft BASIC at Wikipedia](https://en.wikipedia.org/wiki/Applesoft_BASIC)

This was a dialect of BASIC that was available for (in fact, generally shipped with) the [Apple II][].
There is a [manual online here](http://www.scribd.com/doc/232832/Applesoft-Basic-Programming-Reference-Manual).
There was also an "Integer Basic".


- - - -

[The Cat's Eye Technologies Platform]: ../article/Platforms.md#the-cats-eye-technologies-platform
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[C99]: ../article/Project%20Dependencies.md#c99
[MS-DOS]: ../article/Project%20Dependencies.md#ms-dos
[Haskell]: ../article/Project%20Dependencies.md#haskell
[Python]: ../article/Project%20Dependencies.md#python
[Etcha]: ../article/Languages.md#etcha
[Whothm]: ../article/Languages.md#whothm
[yoob]: ../article/Archived.md#yoob
[Thue]: https://esolangs.org/wiki/Thue
[Castile]: ../article/Languages.md#castile
[Velo]: ../article/Languages.md#velo
[Lua]: ../article/Project%20Dependencies.md#lua
[Musical Compositions]: ../article/Musical%20Compositions.md
[TiMidity++]: http://timidity.sourceforge.net/
[xmp]: http://xmp.sourceforge.net/
[Sonant Tracker]: http://www.pouet.net/prod.php?which=53615
[Sonant Live]: http://sonantlive.bitsnbites.eu/
[ZPlet]: ../article/Forks.md#zplet
[Frotz]: https://www.ifarchive.org/if-archive/infocom/interpreters/frotz/
[Commodore BASIC 2.0]: ../article/Project%20Dependencies.md#commodore-basic-20
[Applesoft BASIC]: ../article/Project%20Dependencies.md#applesoft-basic
[Commodore 64]: ../article/Project%20Dependencies.md#commodore-64
[Commodore VIC-20]: ../article/Project%20Dependencies.md#commodore-vic-20
[Apple II]: ../article/Project%20Dependencies.md#apple-ii
[6502]: ../article/Project%20Dependencies.md#6502
[Commodore 64 Programmer's Reference Guide]: https://catseye.tc/view/The-Dossier/article/An%20Esolang%20Reading%20List.md#commodore-64-programmers-reference-guide
[JaC64]: ../article/Forks.md#jac64
[SixtyPical]: ../article/Languages.md#sixtypical
[SITU-SOL]: ../article/Languages.md#situ-sol
[Javascript]: ../article/Project%20Dependencies.md#javascript
[C++]: http://www.open-std.org/jtc1/sc22/wg21/
[Blurry Memories of DOS Programming]: https://catseye.tc/view/The-Dossier/article/Blurry%20Memories%20of%20DOS%20Programming.md
[IBM PC compatible]: ../article/Project%20Dependencies.md#ibm-pc-compatible
[linapple]: https://github.com/linappleii/linapple
[VICE]: https://vice-emu.sourceforge.io/

