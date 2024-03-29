Forks
=====

*   image_url: https://static.catseye.tc/images/illustrations/Fork_(PSF).jpg

Cat's Eye Technologies maintains some forks of some projects which are
otherwise abandoned or under-maintained or whose canonical distribution
just doesn't fit our requirements.

Note that kinds of projects forked here range from
[Language Implementations](Language%20Implementations.md) to Emulators to
[Tools](Tools.md).

Language Projects
-----------------

### minischeme

*   implementation of: [Scheme][] (R4RS)
*   implementation type: interpreter
*   license: Public Domain
*   host language: [ANSI C][]
*   inception date: Nov 5, 1989
*   in distribution: [Minischeme distribution](https://catseye.tc/distribution/Minischeme_distribution)

Originally forked in order to make it build on [AmigaDOS 1.3][].
Also a good test target for [Pixley][].

Fork began Dec 13, 2011.

### OpenZz

*   implementation of: [Zz][]
*   implementation type: interpreter
*   license: LGPL
*   host language: [C99][]
*   inception date: Jan 7, 2002
*   in distribution: [OpenZz distribution](https://catseye.tc/distribution/OpenZz_distribution)

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
*   in distribution: [JaC64 distribution](https://catseye.tc/distribution/JaC64_distribution)

A Commodore 64 emulator written in Java.  Originally it ran as an applet,
but Java applets are pretty much history now.  It has always ran as a
desktop application.  It can now run as a JNLP application.

We forked this from [http://jac64.sourceforge.net/](http://jac64.sourceforge.net/)
because we wanted to put [Bubble Escape 2K][] online
and this emulator ran as an applet but there were a few bugs in it.
We fixed those bugs and submitted those fixes upstream, but heard
nothing from the maintainer.  Thus we keep this fork.

Fork began on June 30, 2011.

### ZPlet

*   implementation of: [Z-Machine][]
*   implementation type: emulator
*   license: Artistic License
*   host language: [Java][]
*   inception date: Nov 16, 2001
*   in distribution: [ZPlet distribution](https://catseye.tc/distribution/Zplet_distribution)

A Z-Machine emulator written in Java.  Originally it ran as an applet,
but Java applets are pretty much history now.  We modified it so that
it can run as a desktop application, so that it can now run as a JNLP
application.

This was for [The Never-Ending Maze][].

Tools
-----

### klaus

*   license: MIT-like
*   in distribution: [klaus distribution](https://catseye.tc/distribution/klaus_distribution)

Klaus is a nice-and-simple Git web interface that we are using
to run [git.catseye.tc](http://git.catseye.tc/).

### ee

*   license: BSD 2-clause
*   in distribution: [ee distribution](https://catseye.tc/distribution/ee_distribution)

`ee` is the "easy editor" which comes with [FreeBSD][].  Cat's Eye Technologies
extracted it from there so we could have a nicer text editor in [The Platform][].

Local version 1.5.2ce1.

### tideay

*   original authors: Paul Harrison
*   license: GPL
*   inception date: Apr 2013
*   development stage: work in progress
*   in distribution: [tideay distribution](https://catseye.tc/distribution/tideay_distribution)

`tideay` is Cat's Eye Technologies' fork of `yaedit`, a GtkSourceView-based
text editor written by Paul Harrison.  In addition to the
features provided by `yaedit`, `tideay` supports things such as
string-rewriting-based editing commands.

### a2tools

*   license: GPL
*   inception date: 1998
*   in distribution: [a2tools distribution](https://catseye.tc/distribution/a2tools_distribution)

`a2tools` is a set of programs for copying files off of and onto
[Apple II][] floppy disk images.  We use it as part of [Funicular][].
There was a bug in it that we fixed so we maintain a fork for that.

[Scheme]: ../article/Project%20Dependencies.md#scheme
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[C99]: ../article/Project%20Dependencies.md#c99
[AmigaDOS 1.3]: ../article/Project%20Dependencies.md#amiga-500
[Pixley]: ../article/Languages.md#pixley
[Zz]: https://catseye.tc/modules/OpenZz/doc/zzdoc.html
[Zzrk]: ../article/Games.md#zzrk
[Java]: ../article/Project%20Dependencies.md#java
[Bubble Escape 2K]: ../article/Games.md#bubble-escape
[The Never-Ending Maze]: ../article/Games.md#the-never-ending-maze
[Z-Machine]: ../article/Project%20Dependencies.md#z-machine
[C++]: http://www.open-std.org/jtc1/sc22/wg21/
[Funicular]: ../article/Tools.md#funicular
[Commodore 64]: ../article/Project%20Dependencies.md#commodore-64
[Apple II]: ../article/Project%20Dependencies.md#apple-ii
[The Platform]: ../article/Platforms.md#the-cats-eye-technologies-platform
[FreeBSD]: https://www.freebsd.org/

