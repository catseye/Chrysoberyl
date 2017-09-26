Retrocomputing
==============

Stuff done at Cat's Eye Technologies on older computers, or more
often, an emulation of such a computer on a modern computer instead.

### Apple II

*   wikipedia: [Apple II](https://en.wikipedia.org/wiki/Apple_II)
*   entry @ [zophar.net](http://www.zophar.net/apple2.html)

The CPU was a 6502.

[Applesoft BASIC](http://www.scribd.com/doc/232832/Applesoft-Basic-Programming-Reference-Manual)
was a dialect of BASIC that was available for
(in fact, generally shipped with) the Apple II series of
microcomputers, including the Apple ][+ and Apple //e.

There was also an "Integer Basic".

**[Apple Befunge][]** is an implementation of Befunge for the Apple II.

[AppleWin](http://applewin.berlios.de/) is an emulator for the Apple II, built for Windows,
written in C++ and distributed under the GPL.

There is also LinApple.

### Commodore VIC-20

*   wikipedia: [Commodore VIC-20](https://en.wikipedia.org/wiki/Commodore_VIC-20)

The CPU was a 6502.  Commodore BASIC 2.0 was in the ROM; this is the same BASIC that was
in the Commodore 64.

The `xvic` executable from [VICE](http://vice-emu.sourceforge.net/), written in C99 and
distributed under the GPL, is a generally recommended emulator for the VIC-20.

**[Dungeons of Ekileugor][]** is a roguelike.

### Commodore 64

*   wikipedia: [Commodore 64](https://en.wikipedia.org/wiki/Commodore_64)

The CPU was a 6510, which was a slightly modified 6502.  Commodore BASIC 2.0 was in the ROM;
this is the same BASIC that was in the VIC-20.

The `x64` executable from [VICE](http://vice-emu.sourceforge.net/), written in C99 and
distributed under the GPL, is a generally recommended emulator for the Commodore 64.

[The Commodore 64 Programmer's Reference Guide](http://www.commodore.ca/manuals/c64_programmers_reference/c64-programmers_reference.htm)
is an invaluable reference, or is it a guide?

**[Bubble Escape][]** is a video game written for the Commodore 64 where the player must guide a bubble through
a multi-screen maze. It was originally designed and implemented in Commodore BASIC 2.0 in the mid-80's, and
rewritten in 6502 assembly language in the late 00's. The assembly version was pared down so that (crunched) it
fit into 2K, christened "Bubble Escape 2K", and submitted to the Mini Game Compo 2009 where it won first place
in its class.

**[DiskSumo][]** is a program to transfer disk images off a Commodore 64 over the RS-232 port via the
XMODEM protocol at 300 baud.

**SITU-PAN** is a front-panel switches simulator for the Commodore 64. It displays 8 virtual LEDs and 8 virtual dip switches on the screen. The LEDs display the bit pattern at the current address in memory. Via the keyboard, the switches may be toggled, a new bit pattern written into memory, and the address advanced. In this way, machine code programs may be entered into memory, and then run. SITU-PAN was written during RetroChallenge 2015/07 for the purposes of entering SITU-MON into an emulated C64.

Lots of C64 stuff at [zimmers.net](http://www.zimmers.net/anonftp/pub/cbm/).

### 6502

*   wikipedia: MOS_Technology_6502
*   specification: http://bytecollector.com/archive/misc/6500-50A_MCS6500pgmManJan76.pdf

The common thread of the above 3 architectures is that they all have a 6502 processor.

Some things Cat's Eye Technologies has done have been 6502-specific but not as specific
to any one architecture.

**SITU-MON** is a machine language monitor for 6502-based systems, written (by hand!) during RetroChallenge 2015/07 and entered into an emulated Commodore 64 using SITU-PAN.

**SITU-SOL** is a vaguely Forth-like language which was designed and implemented (by hand!) during RetroChallenge 2015/07, and entered into an emulated Commodore 64 using SITU-MON.

**SixtyPical**

Here are some links:

*   [6502 Instruction Set reference](http://www.obelisk.demon.co.uk/6502/instructions.html)
*   [scc6502](http://www.reocities.com/SiliconValley/Way/4588/scc6502.html) Small-C for 6502 and LUnix
*   [cc65](http://www.cc65.org/) Freeware C compiler for 6502-based systems

### Amiga 500

*   wikipedia: [Amiga 500](https://en.wikipedia.org/wiki/Amiga_500)

The CPU was a Motorola 68000, but this could be upgraded to a 68020, etc
(and needed to be if you wanted memory protection).  It had many custom chips
with colourful names such as "Angus" and "Paula".

[AmigaDOS 1.3](http://www.pagetable.com/docs/amigados_tripos/amigados_manual.pdf)
was the version of Amiga's operating system which was current when the Amiga 500
was a really popular home computer — mostly for video games, but also for graphics
and video processing, such as ray-tracing and animation.

AmigaBasic was the name of the "advanced" variant of BASIC that shipped with
AmigaDOS.  It was developed by Microsoft.

[E-UAE](http://www.rcdrummond.net/uae/) is an emulator for the Amiga 500
architecture (and several other models such as the Amiga 2000.)  E-UAE is written
in C++ and available under the GPL.

### IBM PC compatible

*   wikipedia: [IBM PC compatible](https://en.wikipedia.org/wiki/IBM_PC_compatible)

The CPU is a 8086, or 80286, 80386, 80486... or just ["X86"](https://en.wikipedia.org/wiki/X86).
Or ["IA-32"](http://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-1-manual.html).
Until you get to the 64-bit architectures — but that's not retrocomputing
anymore.  (yet.)

For emulators, specifications, and other resources,
see [Blurry Memories of DOS Programming](https://github.com/catseye/The-Dossier/blob/master/article/Blurry%20Memories%20of%20DOS%20Programming.md).

running...

### MS-DOS

*   wikipedia: [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS)

By [Microsoft](http://microsoft.com/).  

There's a good free clone of it called [FreeDOS](http://www.freedos.org/) which is
written in (I'm guessing) C99 and assembler and distributed under the GPL.

Can run `.BAT` files.  And `x86` machine code `.COM` files.

[DJGPP](http://www.delorie.com/djgpp/) is a port of GCC to MS-DOS.

Here is a random [MS-DOS game programming link](http://ftp.lanet.lv/ftp/mirror/x2ftp/msdos/programming/).

Emulators include [DOSBox](http://www.dosbox.com/) (written in C++, under the GPL, recommended).

**[Shelta][]** is a programming language.

**[ILLGOL][]** is an illness disguised as a programming language empire.

### Z80

*   genre: machine language
*   specification-link: 'http://www.zilog.com/manage_directlink.php?filepath=docs/z80/um0080&extn=.pdf'
*   wikipedia: [Zilog Z80](https://en.wikipedia.org/wiki/Zilog_Z80)

**[Mildred][]** is a Z80-based homebrew computer.

Here are some links:

*   [Home of the Z80 CPU](http://www.z80.info/) — Lots of useful Z80 information, plus a clock circuit
*   [TI-85 Assembler Programming](http://www.sealiesoftware.com/ti-asm/) — Z80 tutorial for the TI-85 calculator
*   [Opening up Microchips](http://zeptobars.ru/en/read/open-microchip-asic-what-inside-II-msp430-pic-z80) — Innards of a Z80, and more

### Z-Machine

It's actually a virtual machine designed by Infocom so they could port their interactive
fiction onto a multitude of home computers.

(TODO: look up spec, i'm sure it's online.)

**[Zplet](https://github.com/catseye/Zplet/)** is a Java application which emulates a Z-Machine.

There are other, better emulators, such as Frotz.

- - - -

[Apple II]: http://catseye.tc/node/Apple_II
[Apple Befunge]: http://catseye.tc/node/Apple_Befunge
[Dungeons of Ekileugor]: http://catseye.tc/node/Dungeons_of_Ekileugor
[Commodore VIC-20]: http://catseye.tc/node/Commodore_VIC-20
[Commodore 64]: http://catseye.tc/node/Commodore_64
[Bubble Escape]: http://catseye.tc/node/Bubble_Escape
[DiskSumo]: http://catseye.tc/node/DiskSumo
[MS-DOS]: http://catseye.tc/node/MS-DOS
[Shelta]: http://catseye.tc/node/Shelta
[ILLGOL]: http://catseye.tc/node/ILLGOL
[Mildred]: http://catseye.tc/node/Mildred
