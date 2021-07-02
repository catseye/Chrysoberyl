Archived
========

These are nominally projects that Cat's Eye Technologies has done in the past,
and which don't have distributions anymore.  But it's very fuzzy actually, and
this article is a real grab-bag right now.

### Amiga Gondola

*   inception-date: Oct 25 2013
*   reference-distribution: [amiga-gondola-0.1-2013.1111.zip](https://catseye.tc/distfiles/amiga-gondola-0.1-2013.1111.zip)

Amiga Gondola is a set of scripts to set up a development environment
under [AmigaDOS 1.3][], generally on an [Amiga 500][] emulated by the
[E-UAE][] emulator.

It has been superceded by [Funicular][].

#### Implementation: 'populate.sh (Amiga Gondola)':

*   license: Public Domain
*   host-language: [Bourne shell][]
*   target-platform: Amiga 500

### belld

*   inception-date: unknown
*   reference-distribution: [belld-2004.0303.zip](https://catseye.tc/distfiles/belld-2004.0303.zip)

FreeBSD 4.x syscons bell hook to run executable.

#### Implementation: belld.c

*   reference: true
*   license: BSD license
*   host-language: C99

### brace

*   inception-date: unknown
*   reference-distribution: [brace-2004.0920.zip](https://catseye.tc/distfiles/brace-2004.0920.zip)

Utility to translate I/O interactively.

#### Implementation: brace.c

*   reference: true
*   license: BSD license
*   host-language: C99

### Console::Virtual

*   summary: Package for simulating a virtual console
*   inception-date: ca 2003
*   reference-distribution: [Console::Virtual distribution](https://catseye.tc/distribution/Console::Virtual_distribution) (discontinued)

`Console::Virtual` is a simple, lightweight abstraction layer which
allows a program to interact with the user through a console, which
is emulated on whatever user interface is really available.

It's bundled with several distributions of esolangs implemented in
Perl (Ypsilax, noit o' mnain worb, HUNTER).  It also has its own
distribution, but this is discontinued, as no further work will be
done on it, and it will not be used in new products.

#### Implementation: Console::Virtual (Perl module)

*   reference: true
*   in-distributions:
    *   [Console::Virtual distribution](https://catseye.tc/distribution/Console::Virtual_distribution)
    *   [Corona: Realm of Magic distribution](https://catseye.tc/distribution/Corona:_Realm_of_Magic_distribution)
    *   [Ypsilax distribution](https://catseye.tc/distribution/Ypsilax_distribution)
    *   [noit o' mnain worb distribution](https://catseye.tc/distribution/noit_o'_mnain_worb_distribution)
    *   [HUNTER distribution](https://catseye.tc/distribution/HUNTER_distribution)
*   license: BSD license
*   host-language: [Perl][]

### crone

*   summary: Simple, non-polling cron-like scheduler
*   inception-date: Mar 1 2004
*   reference-distribution: [crone-1.0-2014.0819.zip](https://catseye.tc/distfiles/crone-1.0-2014.0819.zip)

`crone` is a simple `cron`-like facility.  Unlike most `cron`s, it does
not periodically activate and run whatever tasks are due to run; instead
it calculates the amount of time between now and when the next is due
to run, and sleeps exactly that long.

#### Implementation: crone.erl

*   reference: true
*   license: BSD license
*   host-language: Erlang

### noise

*   summary: A fairly realistic line-noise generator
*   inception-date: unknown
*   reference-distribution: [The Dipple](https://catseye.tc/distribution/The_Dipple)

A fairly realistic line-noise generator.

#### Implementation: noise (Perl)

*   reference: true
*   license: BSD license
*   host-language: Perl

### luakld

*   summary: Lua embedded in a FreeBSD 4.x kernel module
*   inception-date: unknown
*   reference-distribution: [luakld-2004.1219.zip](https://catseye.tc/distfiles/luakld-2004.1219.zip)

This was a little experiment.  Conclusion: Lua interpreter: not a recommended thing to put in a kernel module.

#### Implementation: luakld (C)

*   reference: true
*   license: BSD license
*   host-language: C99

### mzstorkipiwanbotbotbot

*   inception-date: 2010
*   development-stage: archival
*   reference-distribution: [mzstorkipiwanbotbotbot distribution](https://catseye.tc/distribution/mzstorkipiwanbotbotbot_distribution)

An IRC bot with no purpose or plan.

#### Implementation: mzstorkipiwanbotbotbot (Lua)

*   reference: true
*   license: Public Domain
*   host-language: Lua

#### Implementation: Rtype

*   license: Public Domain
*   host-language: R

(This is kind of wrong because this bot isn't another implementation of
mzstorkipiwanbotbotbot, in fact in some way it's a completely different
bot.  But whatever.)

### Rooibos

*   summary: Simple, single-module parser combinator library
*   inception-date: 2011
*   development-stage: archival
*   reference-distribution: [Eightebed distribution](https://catseye.tc/distribution/Eightebed_distribution)

Rooibos is a parser combinator library for Python. Modelled somewhat
after yeanpypa (self-contained, public domain), but compensates for what
I considered a fatal flaw in yeanpypa (no good way to describe a
recursive grammar.) Has a fatal flaw of its own (can only parse
strictly LL(1) grammars — no backtracking is yet possible.) Originally
used in [Eightebed][], but provided here for ease of transplanting into
other projects.

#### Implementation: rooibos.py

*   reference: true
*   license: Public Domain
*   host-language: Python

### SP_ASM

*   inception-date: 1998
*   reference-distribution: [sp_asm-1998.0716.zip](https://static.catseye.tc/distfiles/sp_asm-1998.0716.zip)

The SPlenetic ASseMbler.
Possibly the most grotty hack implementation of an "assembler" in existence.
It's possible.

The name of this node is incorrect for technical reasons.
It is actually called `SP\ASM`.

#### Implementation: SP_ASM.BAT

*   reference: true
*   license: Unknown license
*   host-language: MS-DOS Batchfile

The name of this node is incorrect for technical reasons.
It is actually called `SP\ASM.BAT`.

### toolshelf

*   summary: A "package manager" that doesn't actually install anything
*   inception-date: 2012
*   reference-distribution: [toolshelf distribution](https://catseye.tc/distribution/toolshelf_distribution)

`toolshelf` is a "package manager" which doesn't actually install any files.
Instead, it stores the source trees of sundry packages in a single directory,
and manages your search paths to include the relevant subdirectories of
those trees. The source trees are typically the working directories of
local git or Mercurial clones, or they can be source distributions from tarballs.

#### Implementation: toolshelf.py

*   reference: true
*   license: MIT license
*   host-language: Python

### yaeolc

*   inception-date: unknown
*   reference-distribution: [The Dipple](https://catseye.tc/distribution/The_Dipple)

Yet Another End Of Line Converter

#### Implementation: yaeolc (Perl)

*   reference: true
*   license: Unknown license
*   host-language: [Perl][]

### yoob

*   inception-date: Mar 15 2011
*   development-stage: not fully complete
*   reference-distribution: [yoob distribution](https://catseye.tc/distribution/yoob_distribution)

`yoob` is a framework for implementing esoteric programming languages
in Java.  It aims to make it easy for a user to experiment with a large
number of esolangs with a minimal install burden (i.e. in a Java Web
Start application), and to make it easy for designers to rapidly
implement and showcase their esolangs.

It has an article on the esowiki, [yoob](http://esolangs.org/wiki/yoob),
but being written in Java, with the intent of being distributed as an
applet, it's largely considered deprecated these days.

However, it can still be started from a web page, if you have Java
Web Start installed — so you can still see it in action
[here](https://catseye.tc/installation/yoob).

#### Implementation: tc.catseye.yoob

*   reference: true
*   license: Public Domain
*   host-language: Java
*   online @ [catseye.tc](https://catseye.tc/installation/yoob)

Links
-----

*   [Bob Jenkins- Comparison of an assortment of hash functions](http://burtleburtle.net/bob/hash/doobs.html)
*   [Theory of Computing](http://theoryofcomputing.org/), an Open-Access Journal
*   [AlertBox](http://www.useit.com/alertbox/), a popular column on Web usability
*   [TinyApps.org](http://www.tinyapps.org/), "A guide to very small software for your PC"

[AmigaDOS 1.3]: ../article/Project%20Dependencies.md#amiga-500
[Amiga 500]: ../article/Project%20Dependencies.md#amiga-500
[Eightebed]: ../article/Languages.md#eightebed
[E-UAE]: ../article/Project%20Dependencies.md#amiga-500
[Bourne shell]: ../article/Project%20Dependencies.md#bourne-shell
[Perl]: ../article/Project%20Dependencies.md#perl
[Funicular]: ../article/Tools.md#funicular

