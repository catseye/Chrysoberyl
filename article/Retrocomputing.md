Retrocomputing
==============

This document contains stuff done at Cat's Eye Technologies on older computers
(or more often, an emulation of such a computer on a modern computer), and tries
to list what you might need to run them, over and above the standard contemporary
[Project Dependencies](../article/Project%20Dependencies.md).

Some of the information here is not specific to Cat's Eye Technologies
and may be moved to [The Dossier][] at a future date.

### Apple II

*   wikipedia: [Apple II](https://en.wikipedia.org/wiki/Apple_II)

Rundown: The Apple II series of microcomputers included the Apple ][+ and Apple //e.
The CPU was a 6502.  [Applesoft BASIC][] was often in the ROM, but it could have been
loaded from tape or disk.

Emulators: [AppleWin](https://www.zophar.net/apple2/applewin.html) is an emulator for the Apple II, built for Windows,
written in C++ and distributed under the GPL.  [Linapple](https://github.com/catseye/linapple)
is a port of AppleWin to Linux.  [zophar.net](http://www.zophar.net/apple2.html) has a list of other emulators.

#### Apple Befunge

![Apple Befunge](http://static.catseye.tc/images/screenshots/Apple%20Befunge.png)

**[Apple Befunge][]** is a variant of Befunge for the Apple II which resembles
Befunge-93, with some extra Befunge-96-esque instructions and some Apple II-specific
instructions.  It was written for the Apple ][+, but should also run on an Apple //e.

### Commodore VIC-20

*   wikipedia: [Commodore VIC-20](https://en.wikipedia.org/wiki/Commodore_VIC-20)

Rundown: The CPU was a 6502.  [Commodore BASIC 2.0][] was in the ROM; this is the same BASIC that was
in the Commodore 64.

Emulators: The `xvic` executable from [VICE](http://vice-emu.sourceforge.net/), written in C99 and
distributed under the GPL, is a generally recommended emulator for the VIC-20.

#### Dungeons of Ekileugor

![Dungeons of Ekileugor](http://catseye.tc/modules/dungeons-of-ekileugor/images/dungeons-of-ekileugor.png)

**[Dungeons of Ekileugor][]** is a roguelike written for the *unexpanded* Commodore VIC-20, which,
despite the limitations of that platform, supports a respectable set of the usual "dungeon furniture":
reasonably generated dungeon levels with tunnels and rooms whose contents are hidden until you enter,
monsters, treasure, potions, traps, chests, combat with experience points, etc.

### Commodore 64

*   wikipedia: [Commodore 64](https://en.wikipedia.org/wiki/Commodore_64)

Rundown: The CPU was a 6510, which was a slightly modified 6502.  [Commodore BASIC 2.0][] was in the ROM;
this is the same BASIC that was in the VIC-20.
The [Commodore 64 Programmer's Reference Guide][] is an invaluable reference, or is it merely a guide?
Lots of C64 stuff can also be found at [zimmers.net](http://www.zimmers.net/anonftp/pub/cbm/).

Emulators: The `x64` executable from [VICE](http://vice-emu.sourceforge.net/), written in C99 and
distributed under the GPL, is a generally recommended emulator for the Commodore 64.
Also, [JaC64](https://github.com/catseye/JaC64) is a GPL Java application which emulates a Commodore 64.
Cat's Eye Technologies uses it to showcase our Commodore 64 games as online installations, using Java Web Start.
We forked it to fix some bugs and because mainline development seemed stalled.

#### Bubble Escape

![Bubble Escape 2K](http://catseye.tc/modules/bubble-escape/images/bubble%20escape%202k.png)

**[Bubble Escape][]** is a video game written for the Commodore 64 where the player must guide a bubble through
a multi-screen maze. It was originally designed and implemented in [Commodore BASIC 2.0][] in the mid-80's, and
rewritten in 6502 assembly language in the late 00's. The assembly version was pared down so that (crunched) it
fit into 2K, christened "Bubble Escape 2K", and submitted to the Mini Game Compo 2009 where it won first place
in its class.

#### DiskSumo

![DiskSumo](http://static.catseye.tc/images/screenshots/DiskSumo.png)
![DiskSumo (transfer)](http://static.catseye.tc/images/screenshots/DiskSumo%20(transfer).png)

**[DiskSumo][]** is a program to transfer disk images off a Commodore 64 over the RS-232 port via the
XMODEM protocol at 300 baud.

#### SITU-PAN

**[SITU-PAN][]** is a front-panel switches simulator for the Commodore 64. It displays 8 virtual LEDs and 8 virtual dip switches on the screen. The LEDs display the bit pattern at the current address in memory. Via the keyboard, the switches may be toggled, a new bit pattern written into memory, and the address advanced. In this way, machine code programs may be entered into memory, and then run. SITU-PAN was written during RetroChallenge 2015/07 for the purposes of entering SITU-MON into an emulated C64.

### 6502

*   wikipedia: [MOS Technology 6502](https://en.wikipedia.org/wiki/MOS_Technology_6502)

The common thread of the above 3 architectures is that they all have a 6502 processor.
Here is MOS Technologies' [1976 manual for the 650x series](http://bytecollector.com/archive/misc/6500-50A_MCS6500pgmManJan76.pdf) (PDF).
There are also a couple of C compilers that target 6502, famously [cc65](http://cc65.github.io/cc65/),
but also [scc6502, a Small-C for 6502 and LUnix](https://web.archive.org/web/20110106052323/http://www.reocities.com/SiliconValley/Way/4588/scc6502.html).

Some things Cat's Eye Technologies has done have been 6502-specific but not as specific
to any one architecture.

#### SITU-MON

![SITU-MON](https://raw.githubusercontent.com/catseye/SITU-SOL/master/doc/bootstrap-zero/images/tumblr_inline_nrdcglfU4p1tvda25_540.png)

**[SITU-MON][]** is a machine language monitor for 6502-based systems, written (by hand!) during RetroChallenge 2015/07 and entered into an emulated Commodore 64 using SITU-PAN.

#### SITU-SOL

![SITU-SOL](https://raw.githubusercontent.com/catseye/SITU-SOL/master/doc/bootstrap-zero/images/tumblr_inline_nrw4gcaz1J1tvda25_540.png)

**[SITU-SOL][]** is a vaguely Forth-like language which was designed and implemented (by hand!) during RetroChallenge 2015/07, and entered into an emulated Commodore 64 using SITU-MON.

#### SixtyPical

![SixtyPical program](https://pbs.twimg.com/media/CSAznWgUsAEOCwB.png)
![SixtyPical output](https://pbs.twimg.com/media/CSAznX7UsAAZki4.png)

**[SixtyPical][]** is a very low-level programming language, similar to 6502 assembly, which defines a set of
static analyses via type-checking and abstract interpretation (liveness analysis of variables, i.e. memory locations.)

### Amiga 500

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
apparently [FS-UAE](https://fs-uae.net/).

### IBM PC compatible

*   wikipedia: [IBM PC compatible](https://en.wikipedia.org/wiki/IBM_PC_compatible)

Rundown: The CPU was a 8086, or 80286, 80386, 80486... or just ["X86"](https://en.wikipedia.org/wiki/X86).
Or ["IA-32"](http://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-1-manual.html).
Until you get to the 64-bit architectures — but that's not retrocomputing
anymore.  (yet.)

For any Cat's Eye Technologies project that claims to run on an "IBM PC compatible,"
probably a 486 with a BIOS, keyboard, and basic VGA is the minimum to make it worthwhile.

Some modern PC's can handle running that sort of legacy setup, but most don't.
Or at least, I wouldn't risk it anymore.  Better to run it under an emulator.

For emulators, specifications, and other resources,
see [Blurry Memories of DOS Programming](https://github.com/catseye/The-Dossier/blob/master/article/Blurry%20Memories%20of%20DOS%20Programming.md).

#### BefOS

![BefOS](http://static.catseye.tc/images/screenshots/BefOS.png)

**[BefOS][]** is an "operating system" for this architecture.
But it's incomplete and terrible.
Generally you would instead be running...

### MS-DOS

*   wikipedia: [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS)

Rundown: By [Microsoft](http://microsoft.com/).  There's a good free clone of it
called [FreeDOS](http://www.freedos.org/) which is
written in (I'm guessing) C99 and assembler and distributed under the GPL.
Can run `.BAT` files.  And x86 machine code `.COM` files.
[DJGPP](http://www.delorie.com/djgpp/) is a port of GCC to MS-DOS.
Here is a random [MS-DOS game programming link](http://ftp.lanet.lv/ftp/mirror/x2ftp/msdos/programming/).

I wouldn't assume any modern Windows installation can handle running MS-DOS
programs directly anymore.  Better to run it under an emulator.

Emulators: there are a few recommended choices here:

*   [DOSBox](http://www.dosbox.com/) (written in C++, under the GPL)
    is an emulator, available for many systems, which
    simulates both an IBM PC compatible and
    MS-DOS on top of it.  It should be plenty sufficient for running
    DOS-based software found here.
*   For a more heavyweight solution, you could install [FreeDOS](http://www.freedos.org/)
    on a PC emulator such as [QEMU](http://www.qemu-project.org/).
    (Note that QEMU can actually emulate many more architectures than just the IBM PC.)

For other emulators, specifications, and other resources,
see [Blurry Memories of DOS Programming](https://github.com/catseye/The-Dossier/blob/master/article/Blurry%20Memories%20of%20DOS%20Programming.md).

Any Cat's Eye Technologies project which claims to need MS-DOS only needs
something which emulates MS-DOS sufficiently well. This includes both the
standard DOS `INT 21h` handler, and the standard DOS utilies like, for example,
`TYPE` and `DEBUG.COM`.

There are only two projects of Cat's Eye Technologies' that
require MS-DOS (or a compatible operating system) anymore, and
these dependencies are only partial:

#### Shelta

![An example session with Shelta](http://static.catseye.tc/images/screenshots/Shelta.png)

**[Shelta][]** is an extremely minimal Forth-like language with barely any semantics; it relies on inline
machine code to write anything resembling an actual program in it. In the spirit of compilers for languages
such as FALSE and brainfuck, a Shelta-to-8086 compiler was implemented (with help from Ben Olmstead) in
less than 512 bytes of 80286 machine code. What's more, it's also been bootstrapped — that is to say, a
Shelta compiler was written in Shelta, which was compiled with the original compiler, and then compiled
again with the resulting compiler, producing a wholly self-hosted executable!

Shelta can be built under any system with a [NASM][] assembler,
but requires DOS to run, and the executables it produces also
run only under DOS (unless you bypass that part of the stdlib).

#### ILLGOL

![An example session with ILLGOL](http://static.catseye.tc/images/screenshots/ILLGOL.png)

**[ILLGOL][]** is an illness disguised as a programming language empire.

ILLGOL can be built and run on any system with a decent [ANSI C][]
compiler, such as `gcc`, but the executables it produces
will only run under DOS.

### Z80

*   wikipedia: [Zilog Z80](https://en.wikipedia.org/wiki/Zilog_Z80)

The [Z80](http://www.zilog.com/manage_directlink.php?filepath=docs/z80/um0080&extn=.pdf)
is another 8-bit CPU that was popular.

Here are some links:

*   [Home of the Z80 CPU](http://www.z80.info/) — Lots of useful Z80 information, plus a clock circuit
*   [TI-85 Assembler Programming](http://www.sealiesoftware.com/ti-asm/) — Z80 tutorial for the TI-85 calculator
*   [Opening up Microchips](http://zeptobars.ru/en/read/open-microchip-asic-what-inside-II-msp430-pic-z80) — Innards of a Z80, and more

#### Mildred

![Mildred](http://catseye.tc/modules/electronics-projects/mildred/doc/mildred_photo.jpg)

**[Mildred][]** is a 4MHz Z80-based homebrew computer with 40K of memory (8K EEPROM, 32K SRAM.)

### Z-Machine

*   wikipedia: [Z-machine](https://en.wikipedia.org/wiki/Z-machine)

It's actually a virtual machine designed by Infocom so they could port their interactive
fiction onto a multitude of home computers.

Here are its [specifications documents](http://inform-fiction.org/zmachine/standards/).

Emulators: [Zplet](https://github.com/catseye/Zplet/) is a Java application which emulates a Z-Machine.
There are other, much better emulators, such as Frotz.

#### The Never-Ending Maze

![The Never-Ending Maze](http://static.catseye.tc/images/illustrations/Never_Ending_Maze.jpg)

**[The Never-Ending Maze][]** is an Infocom-style text adventure game based on the defining cultural phenomenon
of a generation. (Possibly.)

Languages
---------

### Ophis

*   specification-link: https://github.com/michaelcmartin/Ophis

Ophis is an assembler (and its concomitant assembly language) for the 6502 and related
processors, which some of our 6502 code is written in.

### BASIC

*   specification-link: http://en.wikipedia.org/wiki/BASIC

There are lots and lots and lots of variants of BASIC.  Some of our projects are
written in [Commodore BASIC 2.0][].  Others are written in [Applesoft BASIC][].

### Commodore BASIC 2.0

*   specification-link: http://en.wikipedia.org/wiki/BASIC

BASIC for the [Commodore 64][] and [Commodore VIC-20][].  TODO: find better specification link.

### Applesoft BASIC

*   specification-link: https://en.wikipedia.org/wiki/Applesoft_BASIC

This was a dialect of BASIC that was available for (in fact, generally shipped with) the [Apple II][].
There is a [manual online here](http://www.scribd.com/doc/232832/Applesoft-Basic-Programming-Reference-Manual).
There was also an "Integer Basic".

### NASM

*   specification-link: http://nasm.us/

In our projects, many of these NASM files were converted from older
assembly-language sources written in the syntax of Turbo Assembler 3.1
(an old-school x86 assembler for [MS-DOS][], written by Borland.)
In some cases the Turbo Assembler sources are still included in the
project for historical interest, but the newer NASM sources are what
the binaries should be built from.

- - - -

TODO: other things that can redirect here: `emulator`, `BASIC`, `vintage`

[Apple II]: ../article/Retrocomputing.md#apple-ii
[Apple Befunge]: ../article/Languages.md#apple-befunge
[Dungeons of Ekileugor]: ../article/Games.md#dungeons-of-ekileugor
[Commodore VIC-20]: ../article/Retrocomputing.md#commodore-vic-20
[Commodore 64]: ../article/Retrocomputing.md#commodore-64
[Bubble Escape]: ../article/Games.md#bubble-escape
[DiskSumo]: ../article/Tools.md#disksumo
[MS-DOS]: ../article/Retrocomputing.md#ms-dos
[Shelta]: ../article/Languages.md#shelta
[ILLGOL]: ../article/Languages.md#illgol
[Mildred]: ../article/Electronics%20Projects.md#mildred
[Commodore 64 Programmer's Reference Guide]: https://github.com/catseye/The-Dossier/blob/master/article/An%20Esolang%20Reading%20List.md#commodore-64-programmers-reference-guide
[NASM]: ../article/Retrocomputing.md#nasm
[SixtyPical]: ../article/Languages.md#sixtypical
[SITU-PAN]: ../article/Tools.md#situ-pan
[SITU-SOL]: ../article/Languages.md#situ-sol
[SITU-MON]: ../article/Tools.md#situ-mon
[BefOS]: ../article/Platforms.md#befos
[The Never-Ending Maze]: ../article/Games.md#the-never-ending-maze
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[The Dossier]: ../article/General%20Information.md#the-dossier
[Commodore BASIC 2.0]: ../article/Retrocomputing.md#commodore-basic-20

