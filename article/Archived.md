Archived
========

These are nominally projects that Cat's Eye Technologies has done in the past,
and which don't have distributions anymore.  But it's very fuzzy actually, and
this article is a real grab-bag right now.

### Amiga Gondola

*   inception-date: Oct 25 2013

Amiga Gondola is a set of scripts to set up a development environment
under [AmigaDOS 1.3][], generally on an [Amiga 500][] emulated by the
[E-UAE][] emulator.

#### Implementation: 'populate.sh (Amiga Gondola)':

*   in-distribution: [Amiga Gondola distribution](/distribution/Amiga Gondola distribution)
*   license: Public Domain
*   host-language: Bourne shell
*   target-platform: Amiga 500

### belld

*   inception-date: unknown

FreeBSD 4.x syscons bell hook to run executable.

#### Implementation: belld.c

*   reference: true
*   in-distribution: [belld distribution](/distribution/belld distribution)
*   license: BSD license
*   host-language: C99

### brace

*   inception-date: unknown

Utility to translate I/O interactively.

#### Implementation: brace.c

*   reference: true
*   in-distribution: [brace distribution](/distribution/brace distribution)
*   license: BSD license
*   host-language: C99

### crone

*   summary: Simple, non-polling cron-like scheduler
*   inception-date: Mar 1 2004

`crone` is a simple `cron`-like facility.  Unlike most `cron`s, it does
not periodically activate and run whatever tasks are due to run; instead
it calculates the amount of time between now and when the next is due
to run, and sleeps exactly that long.

#### Implementation: crone.erl

*   reference: true
*   in-distribution: [crone distribution](/distribution/crone distribution)
*   license: BSD license
*   host-language: Erlang

### noise

*   summary: A fairly realistic line-noise generator
*   inception-date: unknown

A fairly realistic line-noise generator.

#### Implementation: noise (Perl)

*   reference: true
*   license: BSD license
*   host-language: Perl
*   in-distribution: [The Dipple](/distribution/The Dipple)

### luakld

*   summary: Lua embedded in a FreeBSD 4.x kernel module
*   inception-date: unknown

This was a little experiment.  Conclusion: Lua interpreter: not a recommended thing to put in a kernel module.

#### Implementation: luakld (C)

*   reference: true
*   in-distribution: [luakld distribution](/distribution/luakld distribution)
*   license: BSD license
*   host-language: C99

### SP_ASM

*   inception-date: unknown

The SPlenetic ASseMbler.
Possibly the most grotty hack implementation of an "assembler" in existence.
It's possible.

The name of this node is incorrect for technical reasons.
It is actually called `SP\ASM`.

#### Implementation: SP_ASM.BAT

*   reference: true
*   in-distribution: [SP_ASM distribution](/distribution/SP_ASM distribution)
*   license: Unknown license
*   host-language: MS-DOS Batchfile

The name of this node is incorrect for technical reasons.
It is actually called `SP\ASM.BAT`.

### toolshelf

*   summary: A "package manager" that doesn't actually install anything
*   inception-date: 2012

`toolshelf` is a "package manager" which doesn't actually install any files.
Instead, it stores the source trees of sundry packages in a single directory,
and manages your search paths to include the relevant subdirectories of
those trees. The source trees are typically the working directories of
local git or Mercurial clones, or they can be source distributions from tarballs.

#### Implementation: toolshelf.py

*   reference: true
*   in-distribution: [toolshelf distribution](/distribution/toolshelf distribution)
*   license: MIT license
*   host-language: Python

### transmat

*   inception-date: ca 2005

`transmat` is a network synchronization tool written in Python. It is not
particularly remarkable, but since it has been used in hostile
environments at points (e.g. unreliable dial-up connections, and
Cygwin on Vista,) it does go to some lengths to be robust, to support
lousy protocols (namely FTP), and to minimize transmission time during
synchronization.

#### Implementation: transmat (Python)

*   reference: true
*   in-distribution: [transmat distribution](/distribution/transmat distribution)
*   license: Public Domain
*   host-language: Python

### yaeolc

*   inception-date: unknown

Yet Another End Of Line Converter

#### Implementation: yaeolc (Perl)

*   reference: true
*   in-distributions: [The Dipple](/distribution/The Dipple)
*   license: Unknown license
*   host-language: Perl

### yoob

*   inception-date: Mar 15 2011
*   development-stage: not fully complete

`yoob` is a framework for implementing esoteric programming languages
in Java.  It aims to make it easy for a user to experiment with a large
number of esolangs with a minimal install burden (i.e. in a Java Web
Start application), and to make it easy for designers to rapidly
implement and showcase their esolangs.

It has an article on the esowiki, [yoob](http://esolangs.org/wiki/yoob),
but being written in Java, with the intent of being distributed as an
applet, it's largely considered deprecated these days.

#### Implementation: tc.catseye.yoob

*   reference: true
*   in-distribution: [yoob distribution](/distribution/yoob distribution)
*   license: Public Domain
*   host-language: Java
*   online @ [catseye.tc](http://catseye.tc/installation/yoob)

Links
-----

*   [Bob Jenkins- Comparison of an assortment of hash functions](http://burtleburtle.net/bob/hash/doobs.html)
*   [Theory of Computing](http://theoryofcomputing.org/), an Open-Access Journal
*   [AlertBox](http://www.useit.com/alertbox/), a popular column on Web usability
*   [TinyApps.org](http://www.tinyapps.org/), "A guide to very small software for your PC"

[AmigaDOS 1.3]: ../article/Retrocomputing.md#amiga-500
[Amiga 500]: ../article/Retrocomputing.md#amiga-500
[E-UAE]: ../article/Retrocomputing.md#amiga-500

