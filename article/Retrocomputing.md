Retrocomputing
==============

*   display-illustration: false
*   image_url: https://catseye.tc/modules/dungeons-of-ekileugor/images/dungeons-of-ekileugor.png

This document contains stuff done at Cat's Eye Technologies on older computers
(or more often, an emulation of such a computer on a modern computer).

When a project of Cat's Eye Technologies is built upon some particular retrotechnology
we try to have an entry for that dependency in our
[Project Dependencies](../article/Project%20Dependencies.md) article, where
we describe what modern alternatives, such as emulators, there are for getting
such a project up and running.

#### Apple Befunge

![Apple Befunge](https://static.catseye.tc/images/screenshots/Apple%20Befunge.png)

*   main article: *[Apple Befunge][]*

**[Apple Befunge][]** is a variant of Befunge for the [Apple II][] which resembles
Befunge-93, with some extra Befunge-96-esque instructions and some Apple II-specific
instructions.  It was written for the Apple ][+, but should also run on an Apple //e.

#### Dungeons of Ekileugor

![Dungeons of Ekileugor](https://catseye.tc/modules/dungeons-of-ekileugor/images/dungeons-of-ekileugor.png)

*   main article: *[Dungeons of Ekileugor][]*

**[Dungeons of Ekileugor][]** is a roguelike written for the *unexpanded* [Commodore VIC-20][], which,
despite the limitations of that platform, supports a respectable set of the usual "dungeon furniture":
reasonably generated dungeon levels with tunnels and rooms whose contents are hidden until you enter,
monsters, treasure, potions, traps, chests, combat with experience points, etc.

#### Bubble Escape

![Bubble Escape 2K](https://catseye.tc/modules/bubble-escape/images/bubble%20escape%202k.png)

*   main article: *[Bubble Escape][]*

**[Bubble Escape][]** is a video game written for the Commodore 64 where the player must guide a bubble through
a multi-screen maze. It was originally designed and implemented in [Commodore BASIC 2.0][] in the mid-80's, and
rewritten in 6502 assembly language ([Ophis Assembler][]) in the late 00's. The assembly version was pared down
so that (crunched) it fit into 2K, christened "Bubble Escape 2K", and submitted to the [Mini Game Compo 2009][]
where it won first place in its class.

#### DiskSumo

![DiskSumo main menu](https://static.catseye.tc/images/screenshots/DiskSumo.png)
![DiskSumo during transfer](https://static.catseye.tc/images/screenshots/DiskSumo%20%28transfer%29.png)

*   main article: *[DiskSumo][]*

**[DiskSumo][]** is a program to transfer disk images off a [Commodore 64][] over the RS-232 port via the
XMODEM protocol at 300 baud.

#### SITU-PAN

![SITU-PAN](https://git.catseye.tc/SITU-SOL/blob/master/doc/bootstrap-zero/images/tumblr_inline_nr19fai3D41tvda25_540.jpg?raw=true)

**[SITU-PAN][]** is a front-panel switches simulator for the [Commodore 64][]. It displays 8 virtual LEDs and 8 virtual dip switches on the screen. The LEDs display the bit pattern at the current address in memory. Via the keyboard, the switches may be toggled, a new bit pattern written into memory, and the address advanced. In this way, machine code programs may be entered into memory, and then run. SITU-PAN was written during RetroChallenge 2015/07 for the purposes of entering SITU-MON into an emulated C64.

#### SITU-MON

![SITU-MON](https://git.catseye.tc/SITU-SOL/blob/master/doc/bootstrap-zero/images/tumblr_inline_nrdcglfU4p1tvda25_540.png?raw=true)

**[SITU-MON][]** is a machine language monitor for [6502][]-based systems, written (by hand!) during RetroChallenge 2015/07 and entered into an emulated Commodore 64 using SITU-PAN.

#### SITU-SOL

![SITU-SOL](https://git.catseye.tc/SITU-SOL/blob/master/doc/bootstrap-zero/images/tumblr_inline_nrw4gcaz1J1tvda25_540.png?raw=true)

**[SITU-SOL][]** is a vaguely Forth-like language which was designed and implemented (by hand!) during RetroChallenge 2015/07, and entered into an emulated Commodore 64 using SITU-MON.

#### SixtyPical

![Output of a simple SixtyPical program](https://git.catseye.tc/SixtyPical/blob/master/images/hearts.png?raw=true)

*   main article: *[SixtyPical][]*

**[SixtyPical][]** is a very low-level programming language, similar to [6502][] assembly, which defines a set of
static analyses via type-checking and abstract interpretation (liveness analysis of variables, i.e. memory locations.)

#### BefOS

![BefOS](https://static.catseye.tc/images/screenshots/BefOS.png)

*   main article: *[BefOS][]*

**[BefOS][]** is an "operating system" for this architecture.
But it's incomplete and terrible.

#### Shelta

![An example session with Shelta](https://static.catseye.tc/images/screenshots/Shelta.png)

*   main article: *[Shelta][]*

**[Shelta][]** is an extremely minimal Forth-like language with barely any semantics; it relies on inline
machine code to write anything resembling an actual program in it. In the spirit of compilers for languages
such as FALSE and brainfuck, a Shelta-to-8086 compiler was implemented (with help from Ben Olmstead) in
less than 512 bytes of 80286 machine code. What's more, it's also been bootstrapped — that is to say, a
Shelta compiler was written in Shelta, which was compiled with the original compiler, and then compiled
again with the resulting compiler, producing a wholly self-hosted executable!

Shelta can be built under any system with a [NASM][] assembler,
but requires [MS-DOS][] (or compatible) to run, and the executables it produces also
run only under [MS-DOS][] (unless you bypass that part of the stdlib).

#### ILLGOL

![An example session with ILLGOL](https://static.catseye.tc/images/screenshots/ILLGOL.png)

*   main article: *[ILLGOL][]*

**[ILLGOL][]** is an illness disguised as a programming language empire.

ILLGOL can be built and run on any system with a decent [ANSI C][]
compiler, such as `gcc`, but the executables it produces
will only run under [MS-DOS][] (or compatible).

#### Mildred

![Mildred](https://catseye.tc/modules/electronics-projects/mildred/doc/mildred_photo.jpg)

*   main article: *[Mildred][]*

**[Mildred][]** is a 4MHz [Z80][]-based homebrew computer with 40K of memory (8K EEPROM, 32K SRAM.)

#### The Never-Ending Maze

![The Never-Ending Maze](https://static.catseye.tc/images/illustrations/Never_Ending_Maze.jpg)

*   main article: *[The Never-Ending Maze][]*

**[The Never-Ending Maze][]** is an Infocom-style text adventure game (a [Z-Machine][] story file)
based on the defining cultural phenomenon of a generation. (Possibly.)

[Apple II]: ../article/Project%20Dependencies.md#apple-ii
[Apple Befunge]: ../article/Languages.md#apple-befunge
[Dungeons of Ekileugor]: ../article/Games.md#dungeons-of-ekileugor
[Commodore VIC-20]: ../article/Project%20Dependencies.md#commodore-vic-20
[Commodore 64]: ../article/Project%20Dependencies.md#commodore-64
[Bubble Escape]: ../article/Games.md#bubble-escape
[DiskSumo]: ../article/Tools.md#disksumo
[MS-DOS]: ../article/Project%20Dependencies.md#ms-dos
[Shelta]: ../article/Languages.md#shelta
[ILLGOL]: ../article/Languages.md#illgol
[Mildred]: ../article/Electronics%20Projects.md#mildred
[Commodore 64 Programmer's Reference Guide]: https://catseye.tc/view/The-Dossier/article/An%20Esolang%20Reading%20List.md#commodore-64-programmers-reference-guide
[NASM]: ../article/Project%20Dependencies.md#nasm
[SixtyPical]: ../article/Languages.md#sixtypical
[SITU-PAN]: ../article/Tools.md#situ-pan
[SITU-SOL]: ../article/Languages.md#situ-sol
[SITU-MON]: ../article/Tools.md#situ-mon
[BefOS]: ../article/Platforms.md#befos
[The Never-Ending Maze]: ../article/Games.md#the-never-ending-maze
[ANSI C]: ../article/Project%20Dependencies.md#ansi-c
[The Dossier]: ../article/General%20Information.md#the-dossier
[Commodore BASIC 2.0]: ../article/Project%20Dependencies.md#commodore-basic-20
[Applesoft BASIC]: ../article/Project%20Dependencies.md#applesoft-basic
[Blurry Memories of DOS Programming]: ../view/The-Dossier/article/Blurry%20Memories%20of%20DOS%20Programming.md
[JaC64]: ../article/Forks.md#jac64
[Zplet]: ../article/Forks.md#zplet
[Ophis Assembler]: ../article/Project%20Dependencies.md#ophis-assembler
[Mini Game Compo 2009]: ../article/Events.md#mini-game-compo-2009
[6502]: ../article/Project%20Dependencies.md#6502
[Z80]: ../article/Project%20Dependencies.md#z80
[Z-Machine]: ../article/Project%20Dependencies.md#z-machine

