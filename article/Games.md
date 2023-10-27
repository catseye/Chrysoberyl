Games
=====

*   common auspices: Cat's Eye Technologies
*   common authors: Chris Pressey
*   common development-stage: mature
*   common type: Game
*   display-illustration: false
*   image_url: https://catseye.tc/modules/dungeons-of-ekileugor/images/dungeons-of-ekileugor.png

This is a list of games designed and implemented by Cat's Eye Technologies, listed in alphabetical order.
For more information on these games, [see below](#about-these-games).

For games implemented by, but not designed by, Cat's Eye Technologies, see
[Game Implementations](Game%20Implementations.md).

The distinction between a Game and a [Gewgaw](Gewgaws.md) or even an
[Automaton](Automata.md) is not always cut-and-dried, so if you can't find what
you're looking for here, try those lists as well.

### Bubble Escape

![screenshot](https://catseye.tc/modules/bubble-escape/images/bubble%20escape%202k.png)

*   genre: Maze-Runner
*   inception-date: ca 1988
*   reference distribution: [Bubble Escape distribution](https://catseye.tc/distribution/Bubble_Escape_distribution)
*   online @ [archive.org](https://archive.org/details/Bubble_Escape_2K_2009_Pressey_C.)

_Bubble Escape_ is a video game written for the [Commodore 64][] where the
player must guide a bubble through a multi-screen maze.  It was originally
designed and implemented in [Commodore BASIC 2.0][] in the mid-80's, and
rewritten in [Ophis Assembler][] in the late 00's.
The assembly version was pared down so that (crunched) it fit into 2K,
christened "Bubble Escape 2K", and submitted to the [Mini Game Compo 2009][]
where it won first place in its class.

It's archived on the Internet Archive, where you can play it in your browser.
Just follow the "online" link shown above.

You can also download the D64 disk image file
[bubble escape.d64](https://github.com/catseye/Bubble-Escape/blob/master/disk/bubble%20escape.d64?raw=true)
and run it in [VICE][]'s `x64` or some other Commodore 64 emulator.

If this game doesn't seem too impressive to you, try to remember, it's
only two kilobytes of code!  These days you can't even sneeze in less
than a megabyte.

#### Implementation: Bubble Escape (BASIC)

*   reference: true
*   license: BSD license
*   host-language: [Commodore BASIC 2.0][]
*   host-platform: [Commodore 64][]
*   controls: joystick

#### Implementation: Bubble Escape 2K

*   prebuilt-for-platforms: [Commodore 64][]
*   license: BSD license
*   host-language: [Ophis Assembler][]
*   host-platform: [Commodore 64][]
*   build-requirements: CRUNCHER AB+
*   controls: joystick
*   submitted-to: [Mini Game Compo 2009][]; 1st place in 2K category
*   online @ [archive.org](https://archive.org/details/Bubble_Escape_2K_2009_Pressey_C.)
*   download @ [github.com](https://github.com/catseye/Bubble-Escape/blob/master/disk/bubble%20escape.d64?raw=true)

#### Implementation: Bubble Escape 8K

*   prebuilt-for-platforms: [Commodore 64][]
*   license: BSD license
*   host-language: [Ophis Assembler][]
*   host-platform: [Commodore 64][]
*   controls: joystick

### Corona: Realm of Magic

![screenshot](https://catseye.tc/modules/corona-realm-of-magic/doc/carpe_ss2.gif)

*   genre: Roguelike
*   inception-date: ca Sep 2000
*   reference distribution: [Corona: Realm of Magic distribution](https://catseye.tc/distribution/Corona:_Realm_of_Magic_distribution)
*   development-stage: archival

_Corona: Realm of Magic_ is an unfinished roguelike written in
[Perl][].  It was written on top of a framework
that Cat's Eye Technologies was developing at the time
called CARPE DIEM (Computer-Assisted Role-Playing Engine for Diverse
Interactive Entertainment Modules.)

#### Implementation: Corona: Realm of Magic (Perl)

*   reference: true
*   license: BSD license
*   host-language: [Perl][] 5.8
*   interface: [ANSI Terminal][]

### Cosmos Boulders

![screenshot](https://catseye.tc/modules/cosmos-boulders/images/cosmos-boulders-screenshot.png)

*   genre: Shoot-em-Up
*   inception-date: 2019
*   reference distribution: [Cosmos Boulders distribution](https://catseye.tc/distribution/Cosmos_Boulders_distribution)
*   online @ [catseye.tc](https://catseye.tc/installation/Cosmos_Boulders)

_Cosmos Boulders_ is an arcade-style HTML5 minigame built with reducers
and immutable data in ES5 JavaScript.

#### Implementation: cosmos-boulders.js

*   license: Freely Redistributable
*   host-language: [Javascript][]
*   host-platform: HTML5
*   controls: keyboard

### Dungeons of Ekileugor

![screenshot](https://catseye.tc/modules/dungeons-of-ekileugor/images/dungeons-of-ekileugor.png)

*   genre: Roguelike
*   inception-date: Aug 2012
*   reference distribution: [Dungeons of Ekileugor distribution](https://catseye.tc/distribution/Dungeons_of_Ekileugor_distribution)
*   online @ [archive.org](https://archive.org/details/dungeons-of-ekileugor)

_Dungeons of Ekileugor_ is a roguelike written for the [Commodore VIC-20][],
which, despite the limitations of that platform, supports a respectable
set of the usual "dungeon furniture": reasonably generated dungeon levels
with tunnels and rooms whose contents are hidden until you enter,
monsters, treasure, potions, traps, chests, combat with experience points,
etc.

#### Implementation: Dungeons of Ekileugor (BASIC)

*   reference: true
*   license: Freely Redistributable
*   host-language: [Commodore BASIC 2.0][]
*   host-platform: [Commodore VIC-20][]
*   controls: keyboard

### Super Wumpus Land

![screenshot](https://catseye.tc/modules/super-wumpus-land/images/Super%20Wumpus%20Land.png)

*   genre: Logic
*   inception-date: ca 1999
*   reference distribution: [Super Wumpus Land distribution](https://catseye.tc/distribution/Super_Wumpus_Land_distribution)
*   online @ [catseye.tc](https://catseye.tc/installation/Super_Wumpus_Land)

_Super Wumpus Land_ is an "extended dance mix" version of Gregory Yob's
[Hunt the Wumpus][].  It's playable in your web browser in a simulation
of an old-school green-screen video terminal.

#### Implementation: swl.pl

*   reference: true
*   license: BSD license
*   host-language: [Perl][] 5.8
*   interface: terminal

#### Implementation: swl.js

*   license: BSD license
*   host-language: [Javascript][]
*   host-platform: HTML5
*   interface: yoob.js TextTerminal
*   online @ [catseye.tc](https://catseye.tc/installation/Super_Wumpus_Land)

### The New Gamerly Realism

![screenshot](https://static.catseye.tc/images/illustrations/The_New_Gamerly_Realism.jpg)

*   genre: Philosophy
*   inception-date: 2015
*   reference distribution: [The New Gamerly Realism distribution](https://catseye.tc/distribution/The_New_Gamerly_Realism distribution)
*   online @ [catseye.tc](https://catseye.tc/installation/The_New_Gamerly_Realism)

Only when the conscious habit of coding culture's little interactions,
Marios and Lara Crofts in games disappears
_will we witness a purely gamerly work of gamedev_.

I have transformed myself _in the zero of gameplay_ and have fished myself out
of the _rubbishy slough of mainstream gaming_...

Only dull and impotent gamedevs veil their work with _sincerity_.
Gaming requires _truth_, not _sincerity_.

_Levels have vanished like smoke; to attain the new gamerly paradigm_,
gamedev advances towards creation as an end in itself and towards
reification of the interactions of culture.

#### Implementation: the-new-gamerly-realism.js

*   reference: true
*   license: Unknown license
*   host-language: [Javascript][]
*   host-platform: HTML5
*   online @ [catseye.tc](https://catseye.tc/installation/The_New_Gamerly_Realism)

### The Never-Ending Maze

![screenshot](https://static.catseye.tc/images/illustrations/Never_Ending_Maze.jpg)

*   genre: Text Adventure
*   inception-date: ca 2000
*   online @ [archive.org](https://archive.org/details/the_never-ending_maze)

An Infocom-style text adventure game based on the defining cultural
phenomenon of a generation.  (Possibly.)

It's archived on the Internet Archive, where you can play it in your browser.
Just follow the "online" link shown above.

You can also download the Z5 story file
[never-ending-maze-1.0.z5](https://static.catseye.tc/distfiles/never-ending-maze-1.0.z5)
and run it in [Frotz][], [ZPlet][], or some other Z-Machine emulator.

#### Implementation: never-ending-maze.z5

*   license: Freely Redistributable
*   host-platform: Z-Machine
*   host-language: Z-Machine code
*   online @ [archive.org](https://archive.org/details/the_never-ending_maze)
*   download @ [static.catseye.tc](https://static.catseye.tc/distfiles/never-ending-maze-1.0.z5)

### Zzrk

![screenshot](https://static.catseye.tc/images/illustrations/Zzrk.jpg)

*   subtitle: **Adventures in the Great Unsaturated Grammar**
*   genre: Text Adventure
*   inception-date: ca 2003
*   reference distribution: [Zzrk distribution](https://catseye.tc/distribution/Zzrk_distribution)
*   online @ [archive.org](https://archive.org/details/zzrk_adventure)

_Zzrk_ is a tiny adventure game written in "100% pure" Zz
(a meta-language normally used for defining programming languages.)

#### Implementation: Zzrk (Zz)

*   reference: true
*   license: BSD license
*   host-language: Zz
*   implemented-in-meta: true
*   interface: terminal

About these Games
-----------------

A game is anything you can play, but most of these are meant to be played on a computer.
Some of them can even be played online, right in your web browser.

See also:

*   [Game Implementations](Game%20Implementations.md)
*   [Video Games of Note](https://catseye.tc/view/The-Dossier/article/Video%20Games%20of%20Note.md) in The Dossier
*   [Text Adventures of Note](https://catseye.tc/view/The-Dossier/article/Text%20Adventures%20of%20Note.md) in The Dossier

- - - -

[Commodore 64]: ../article/Project%20Dependencies.md#commodore-64
[Commodore VIC-20]: ../article/Project%20Dependencies.md#commodore-vic-20
[Commodore BASIC 2.0]: ../article/Project%20Dependencies.md#commodore-basic-20
[Ophis Assembler]: ../article/Project%20Dependencies.md#ophis-assembler
[Mini Game Compo 2009]: ../article/Events.md#mini-game-compo-2009
[Perl]: ../article/Project%20Dependencies.md#perl
[Hunt the Wumpus]: https://codeberg.org/cpressey/Some-Games-of-Note/src/branch/master/article/Classic%20Computer%20Games.md#hunt-the-wumpus
[ANSI Terminal]: ../article/Project%20Dependencies.md#ansi-terminal
[Javascript]: ../article/Project%20Dependencies.md#javascript
[Frotz]: https://www.ifarchive.org/if-archive/infocom/interpreters/frotz/
[ZPlet]: ../article/Forks.md#zplet
[VICE]: https://vice-emu.sourceforge.io/

