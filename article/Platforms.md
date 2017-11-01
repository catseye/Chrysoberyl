Platforms
=========

Various platforms that Cat's Eye Technologies has worked on.

A platform is something you write something else "on".
(Something you write something else "in" is a framework.)

Note that the precise distinctions between a Tool, a Platform, and a Library
are debatable, and entries may be categorized somewhat arbitrarily.

### The Cat's Eye Technologies Platform

*   native-language: many
*   other-languages: many
*   inception-date: Oct 4 2014
*   development-stage: not fully complete
*   reference-distribution: [The Cat's Eye Technologies Platform distribution](/distribution/The Cat's Eye Technologies Platform distribution)

The Cat's Eye Technologies Platform is a [NetBSD][]-based,
[shelf][]-powered, [Funicular][]-built "distro" containing almost all of
[Cat's Eye Technologies][]' software distributions.

#### Reference Implementation: The-Cats-Eye-Technologies-Platform.img

*   license: [BSD-compatible license](https://github.com/catseye/The-Platform/blob/master/LICENSE) (source code); "mere aggregation" of many licenses (built image)
*   host-platform: IBM PC compatible
*   build-requirements: Funicular

Note that the distribution does not contain a built version of
this implementation; the distribution contains [Funicular][]
configurations which allow you to build this disk image from source.

It currently builds for the [IBM PC compatible][] architecture, but in
theory it could be built for other architectures that NetBSD runs on.

A pre-built disk image is available to download via
[this torrent](https://raw.githubusercontent.com/catseye/The-Platform/master/torrent/The-Cats-Eye-Technologies-Platform-0.4.torrent).

### BefOS

![BefOS](http://static.catseye.tc/images/screenshots/BefOS.png)

*   subtitle: **An Operating System for the Linearly Challenged**
*   native-language: x86 machine code
*   other-languages: Befunge-93 (this is sort-of almost true)
*   inception-date: ca 1999
*   development-stage: archival
*   reference-distribution: [BefOS distribution](/distribution/BefOS distribution)
*   online @ [catseye.tc](http://catseye.tc/installation/BefOS)

Begun in the late 90's as a project to write an "operating system"
in the theme of [Befunge-93][], *BefOS* is a program for the
[IBM PC compatible][] architecture which boots off of a floppy disk
and presents the user with a 2-dimensional, text-console-based
interface to the computer system.  However, it omits most of the
functionality of a production operating system, and most of the
functionality of Befunge as well, and therefore might be more
accurately described as a disk sector editor with some unusual
features.

Sometime after 2000 it was modernized (it source code converted from
Turbo Assembler to [NASM][]) and installed online here so you can try
it out in your web browser: online @ [catseye.tc](http://catseye.tc/installation/BefOS)

It has an article on the esowiki here: [BefOS](http://esolangs.org/wiki/BefOS).

#### Reference Implementation: BefOS (NASM)

*   license: Public Domain
*   host-language: [NASM Assembler][]
*   host-platform: [IBM PC compatible][]
*   build-requirements: [ANSI C][], [Perl][]
*   online @ [catseye.tc](http://catseye.tc/installation/BefOS)

[NetBSD]: http://netbsd.org/
[shelf]: ../article/Tools.md#shelf
[Cat's Eye Technologies]: ../article/General%20Information.md#cats-eye-technologies
[IBM PC compatible]: ../article/Retrocomputing.md#ibm-pc-compatible
[Befunge]: http://catseye.tc/node/Befunge
[Befunge-93]: ../article/Languages.md#befunge-93
[NASM]: http://nasm.us/
[NASM Assembler]: http://nasm.us/
[Funicular]: ../article/Tools.md#funicular
[ANSI C]: http://clc-wiki.net/wiki/C89
[Perl]: http://www.perl.org/

