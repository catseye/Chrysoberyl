Forks
=====

Cat's Eye Technologies maintains some forks of some projects which are
otherwise abandoned or under-maintained or whose canonical distribution
just doesn't fit our requirements.

Note that kinds of projects forked here range from
[Language Implementations](Language%20Implementations.md) to Emulators to
[Tools](Tools.md).

Language Projects
-----------------

### miniscm

*   implementation of: [Scheme][] (R4RS)
*   implementation type: interpreter
*   license: Public Domain
*   host language: [ANSI C][]
*   inception date: Nov 5, 1989
*   in distribution: [Minischeme distribution](http://catseye.tc/distribution/Minischeme_distribution)

Originally forked in order to make it build on [AmigaDOS 1.3][].
Also a good test target for [Pixley][].

Fork began Dec 13, 2011.

### OpenZz

*   implementation of: [Zz][]
*   implementation type: interpreter
*   license: LGPL
*   host language: [C99][]
*   inception date: Jan 7, 2002
*   in distribution: [OpenZz distribution](http://catseye.tc/distribution/OpenZz_distribution)

Forked because [Zzrk][] depends on it, and I want to maintain that.

Note that while most of the code is LGPL, the REPL is GPL.

Fork began Feb 1, 2012.

Emulators
---------

### JaC64

*   implementation of: [Commodore 64][]
*   implementation type: emulator
*   license: GPL
*   host language: [Java][]
*   inception date: 2006
*   in distribution: [https://github.com/catseye/JaC64](https://github.com/catseye/JaC64)

A Commodore 64 emulator written in Java.  Originally it ran as an applet,
but Java applets are pretty much history now.  It has always ran as a
desktop application.  It can now run as a JNLP application.

We forked this because we wanted to put [Bubble Escape 2K][] online
and this emulator ran as an applet but there were a few bugs in it.
We fixed those bugs and submitted those fixes upstream, but heard
nothing from the maintainer.  Thus we keep this fork.

### Zplet

*   implementation of: [Z-Machine][]
*   implementation type: emulator
*   license: Artistic License
*   host language: [Java][]
*   inception date: Nov 16, 2001
*   in distribution: [https://github.com/catseye/Zplet](https://github.com/catseye/Zplet)

A Z-Machine emulator written in Java.  Originally it ran as an applet,
but Java applets are pretty much history now.  We modified it so that
it can run as a desktop application, so that it can now run as a JNLP
application.

This was for [The Never-Ending Maze][].

### linapple

*   implementation of: [Apple II][]
*   implementation type: emulator
*   license: GPL
*   host language: [C++][]
*   inception date: 1994 (as AppleWin)
*   in distribution: [https://github.com/catseye/linapple](https://github.com/catseye/linapple)

An Apple II emulator.  We maintain a fork only to make it work like
a proper Unix command-line utility and thus play nicely with
[Funicular][].

Tools
-----

### klaus

*   license: MIT-like
*   in distribution: [https://github.com/catseye/klaus](https://github.com/catseye/klaus)

Klaus is a nice-and-simple Git web interface that we are using
to run [git.catseye.tc](http://git.catseye.tc/).

### ee

*   license: BSD 2-clause
*   in distribution: [ee distribution](http://catseye.tc/distribution/ee_distribution)

`ee` is the "easy editor" which comes with [FreeBSD][].  Cat's Eye Technologies
extracted it from there so we could have a nicer text editor in [The Platform][].

Local version 1.5.2ce1.

### tideay

*   original authors: Paul Harrison
*   license: GPL
*   inception date: Apr 2013
*   development stage: work in progress
*   in distribution: [tideay distribution](http://catseye.tc/distribution/tideay_distribution)

`tideay` is Cat's Eye Technologies' fork of `yaedit`, a GtkSourceView-based
text editor written by Paul Harrison.  In addition to the
features provided by `yaedit`, `tideay` supports things such as
string-rewriting-based editing commands.

### a2tools

*   license: GPL
*   inception date: 1998
*   in distribution: [https://github.com/catseye/a2tools](https://github.com/catseye/a2tools)

`a2tools` is a set of programs for copying files off of and onto
[Apple II][] floppy disk images.  We use it as part of [Funicular][].
There was a bug in it that we fixed so we maintain a fork for that.

[Scheme]: ../article/Project%20Dependencies.md#scheme
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[C99]: ../article/Project%20Dependencies.md#c99
[AmigaDOS 1.3]: ../article/Retrocomputing.md#amiga-500
[Pixley]: ../article/Languages.md#pixley
[Zz]: https://cdn.rawgit.com/catseye/OpenZz/90896648/doc/zzdoc.html
[Zzrk]: ../article/Games.md#zzrk
[Java]: ../article/Project%20Dependencies.md#java
[Bubble Escape 2K]: ../article/Games.md#bubble-escape
[The Never-Ending Maze]: ../article/Games.md#the-never-ending-maze
[Z-Machine]: ../article/Retrocomputing.md#z-machine
[C++]: http://www.open-std.org/jtc1/sc22/wg21/
[Funicular]: ../article/Tools.md#funicular
[Commodore 64]: ../article/Retrocomputing.md#commodore-64
[Apple II]: ../article/Retrocomputing.md#apple-ii
[The Platform]: ../article/Platforms.md#the-cats-eye-technologies-platform
[FreeBSD]: https://www.freebsd.org/

