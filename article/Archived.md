Archived
========

These are nominally projects that Cat's Eye Technologies has done in the past,
and which don't have distributions anymore.  But it's very fuzzy actually, and
this article is a real grab-bag right now.

### Amiga Gondola

*   type: Tool
*   inception-date: Oct 25 2013

Amiga Gondola is a set of scripts to set up a development environment
under [[AmigaDOS 1.3]], generally on an [[Amiga 500]] emulated by the
[[E-UAE]] emulator.

#### Implementation: 'populate.sh (Amiga Gondola)':

*   in-distribution: [Amiga Gondola distribution](/distribution/Amiga Gondola distribution)
*   license: Public Domain
*   host-language: Bourne shell
*   target-platform: Amiga 500

### belld

  type: Tool
  summary: FreeBSD 4.x syscons bell hook to run executable

#### Implementation: belld.c

  reference: true
  in-distribution: belld distribution
  license: BSD license
  host-language: C99

### brace

  type: Tool
  summary: Utility to translate I/O interactively

#### brace.c

  reference: true
  in-distribution: brace distribution
  license: BSD license
  host-language: C99

### crone

*   type: Tool
*   summary: Simple, non-polling cron-like scheduler
*   inception-date: Mar 1 2004

`crone` is a simple `cron`-like facility.  Unlike most `cron`s, it does
not periodically activate and run whatever tasks are due to run; instead
it calculates the amount of time between now and when the next is due
to run, and sleeps exactly that long.

#### crone.erl

*   reference: true
*   in-distribution: crone distribution
*   license: BSD license
*   host-language: Erlang

### noise

  type: Tool
  summary: A fairly realistic line-noise generator

#### noise (Perl)

*   reference: true
*   license: BSD license
*   host-language: Perl
*   in-distribution: The Dipple

### luakld

*   type: Kernel module
*   summary: Lua embedded in a FreeBSD 4.x kernel module

This was a little experiment.  Conclusion: Lua interpreter: not a recommended thing to put in a kernel module.

#### Implementation: luakld (C)

*   reference: true
*   in-distribution: luakld distribution
*   license: BSD license
*   host-language: C99

### SP_ASM

*   type: Tool

The SPlenetic ASseMbler.
Possibly the most grotty hack implementation of an "assembler" in existence.
It's possible.

The name of this node is incorrect for technical reasons.
It is actually called `SP\ASM`.

#### Implementation: SP_ASM.BAT

*   reference: true
*   in-distribution: SP_ASM distribution
*   license: Unknown license
*   host-language: MS-DOS Batchfile

The name of this node is incorrect for technical reasons.
It is actually called `SP\ASM.BAT`.

### toolshelf

*   type: Tool
*   summary: A "package manager" that doesn't actually install anything
*   inception-date: 2012

`toolshelf` is a "package manager" which doesn't actually install any files.
Instead, it stores the source trees of sundry packages in a single directory,
and manages your search paths to include the relevant subdirectories of
those trees. The source trees are typically the working directories of
local git or Mercurial clones, or they can be source distributions from tarballs.

#### toolshelf.py

*   reference: true
*   in-distribution: toolshelf distribution
*   license: MIT license
*   host-language: Python

### transmat

*   type: Tool
*   inception-date: ca 2005

`transmat` is a network synchronization tool written in Python. It is not
particularly remarkable, but since it has been used in hostile
environments at points (e.g. unreliable dial-up connections, and
Cygwin on Vista,) it does go to some lengths to be robust, to support
lousy protocols (namely FTP), and to minimize transmission time during
synchronization.

#### transmat (Python)

*   type: Implementation
*   implementation-of:
*   - transmat
*   reference: true
*   in-distribution: transmat distribution
*   license: Public Domain
*   host-language: Python

### yaeolc

*   type: Tool

Yet Another End Of Line Converter

#### yaeolc (Perl)

*   reference: true
*   in-distributions:
*   - yaeolc distribution
*   - The Dipple
*   license: Unknown license
*   host-language: Perl

Links
-----

*   [Bob Jenkins- Comparison of an assortment of hash functions](http://burtleburtle.net/bob/hash/doobs.html)
*   [Theory of Computing](http://theoryofcomputing.org/), an Open-Access Journal
*   [AlertBox](http://www.useit.com/alertbox/), a popular column on Web usability
*   [TinyApps.org](http://www.tinyapps.org/), "A guide to very small software for your PC"
