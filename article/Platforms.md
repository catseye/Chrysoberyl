Platforms
=========

Various platforms that Cat's Eye Technologies has worked on.

### The Cat's Eye Technologies Platform

*   native-language: Bourne shell (oh, this is *so* not really true)
*   other-languages: many, many.
*   inception-date: Oct 4 2014
*   development-stage: not fully complete

The Cat's Eye Technologies Platform is a [NetBSD][]-based,
[shelf][]-powered, [Funicular][]-built "distro" containing almost all of
[Cat's Eye Technologies][]' software distributions.

#### Implementation: The-Cats-Eye-Technologies-Platform-0.2.img

*   reference: true
*   implementation-type: framework
*   in-distribution: "The Cat's Eye Technologies Platform distribution"
*   generally-recommended: true
*   license: Unknown license
*   host-language: x86 machine code

Despite what it says above, it is not really "in" the distribution.
The distribution contains [Funicular][] configurations which allow
you to build this disk image from source.  A pre-built disk image
is available to download via
[this torrent](https://raw.githubusercontent.com/catseye/The-Platform/master/torrent/The-Cats-Eye-Technologies-Platform-0.2.torrent).

### BefOS

![BefOS](http://static.catseye.tc/images/screenshots/BefOS.png)

*   subtitle: **An Operating System for the Linearly Challenged**
*   native-language: x86 machine code
*   other-languages: Befunge-93 (this is sort-of almost true)
*   influences: Befunge-93
*   inception-date: ca 1999
*   development-stage: archival
*   dimensionality: 2
*   esowiki: BefOS

BefOS is a program which boots off of a floppy disk, and is
billed as a Befunge-themed toy operating system for the
[IBM PC compatible][] architecture.  However, it omits
most of the functionality of an operating system, and most of the
functionality of Befunge as well, and therefore might be more
accurately described as a disk sector editor with some unusual
features.

#### Implementation: BefOS (NASM)

*   reference: true
*   implementation-type: operating system
*   in-distribution: BefOS distribution
*   license: Public Domain
*   host-language: NASM Assembler
*   host-platform: IBM PC compatible
*   build-requirements: ANSI C, Perl
*   online @ [catseye.tc](http://catseye.tc/installation/BefOS)

- - - -

[NetBSD]: TBD
[shelf]: TBD
[Cat's Eye Technologies]: http://catseye.tc/
[IBM PC compatible]: TBD
