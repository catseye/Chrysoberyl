Games
=====

*   common type: Game
*   common authors: Chris Pressey
*   common auspices: Cat's Eye Technologies
*   common development-stage: mature

### Bubble Escape

![screenshot](http://catseye.tc/modules/bubble-escape/images/bubble%20escape%202k.png)

*   genre: Maze-Runner
*   inception-date: ca 1988

Bubble Escape is a video game written for the [Commodore 64][] where the
player must guide a bubble through a multi-screen maze.  It was originally
designed and implemented in Commodore BASIC 2.0 in the mid-80's, and
rewritten in [Ophis Assembler][] in the late 00's.
The assembly version was pared down so that (crunched) it fit into 2K,
christened "Bubble Escape 2K", and submitted to the [Mini Game Compo 2009][]
where it won first place in its class.

#### Implementation: Bubble Escape (BASIC)

*   reference: true
*   in-distribution: 'Bubble Escape distribution'
*   license: BSD license
*   host-language: Commodore BASIC 2.0
*   host-platform: Commodore 64
*   controls: joystick

#### Implementation: Bubble Escape 2K

*   in-distribution: 'Bubble Escape distribution'
*   prebuilt-for-platforms:
*   - Commodore 64
*   license: BSD license
*   host-language: Ophis Assembler
*   host-language-version: "2.0"
*   host-platform: Commodore 64
*   build-requirements:
*   - CRUNCHER AB+
*   controls: joystick
*   submitted-to:
*   - competition: Mini Game Compo 2009
*     prize: 1st place in 2K category
*   online-locations:
*   - installation/Bubble Escape

#### Implementation: Bubble Escape 8K

*   in-distribution: 'Bubble Escape distribution'
*   prebuilt-for-platforms:
*   - Commodore 64
*   license: BSD license
*   host-language: Ophis Assembler
*   host-language-version: "2.0"
*   host-platform: Commodore 64
*   controls: joystick

### Corona: Realm of Magic'

![screenshot](http://catseye.tc/modules/corona-realm-of-magic/doc/carpe_ss2.gif)

*   genre: Roguelike
*   inception-date: ca Sep 2000
*   development-stage: archival

Corona: Realm of Magic is an unfinished roguelike written in
[Perl][].  It was written on top of a framework
that Cat's Eye Technologies was developing at the time
called CARPE DIEM (Computer-Assisted Role-Playing Engine for Diverse
Interactive Entertainment Modules.)

#### Implementation: Corona: Realm of Magic (Perl)

*   reference: true
*   in-distribution: 'Corona: Realm of Magic distribution'
*   license: BSD license
*   host-language: Perl 5.8
*   interface: ANSI Terminal

### Dungeons of Ekileugor

![screenshot](http://catseye.tc/modules/dungeons-of-ekileugor/images/dungeons-of-ekileugor.png)

*   genre: Roguelike
*   inception-date: Aug 2012

Dungeons of Ekileugor is a roguelike written for the [[Commodore VIC-20]],
which, despite the limitations of that platform, supports a respectable
set of the usual "dungeon furniture": reasonably generated dungeon levels
with tunnels and rooms whose contents are hidden until you enter,
monsters, treasure, potions, traps, chests, combat with experience points,
etc.

#### Implementation: Dungeons of Ekileugor (BASIC)

*   reference: true
*   in-distribution: 'Dungeons of Ekileugor distribution'
*   license: Freely Redistributable
*   host-language: Commodore BASIC 2.0
*   host-platform: Commodore VIC-20
*   controls: keyboard

### Super Wumpus Land

![screenshot](http://catseye.tc/modules/super-wumpus-land/images/Super%20Wumpus%20Land.png)

*   genre: Logic
*   inception-date: ca 1999

Super Wumpus Land is an "extended dance mix" version of Gregory Yob's
[Hunt the Wumpus][].  It's playable in your web browser in a simulation
of an old-school green-screen video terminal.

#### Implementation: swl.pl

*   reference: true
*   in-distribution: Super Wumpus Land distribution
*   license: BSD license
*   host-language: Perl
*   host-language-version: "5.8"
*   interface: terminal

#### Implementation: swl.js

*   in-distribution: Super Wumpus Land distribution
*   license: BSD license
*   host-language: Javascript
*   host-platform: HTML5
*   interface: yoob.js TextTerminal
*   online @ [catseye.tc](http://catseye.tc/installation/Super_Wumpus_Land)

### The New Gamerly Realism

![screenshot](http://catseye.tc/images/illustrations/The_New_Gamerly_Realism.jpg)

*   genre: Philosophy
*   inception-date: 2015

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

*   in-distribution: The New Gamerly Realism distribution
*   reference: true
*   license: Unknown license
*   host-language: Javascript
*   host-platform: HTML5
*   online @ [catseye.tc](http://catseye.tc/installation/The_New_Gamerly_Realism)

### The Never-Ending Maze

![screenshot](http://catseye.tc/images/illustrations/Never_Ending_Maze.jpg)

*   genre: Text Adventure
*   inception-date: ca 2000

An Infocom-style text adventure game based on the defining cultural
phenomenon of a generation.  (Possibly.)

#### Implementation: never-ending-maze.z5

    license: Freely Redistributable
    host-platform: Z-Machine
    host-language: Z-Machine code
    implementation-of:
    - The Never-Ending Maze
    online-locations:
    - installation/The Never-Ending Maze
    file-locations:
    - http://catseye.tc/distfiles/never-ending-maze-1.0.z5

### Zzrk

![screenshot](http://catseye.tc/images/illustrations/Zzrk.jpg)

*   subtitle: **Adventures in the Great Unsaturated Grammar**
*   genre: Text Adventure
*   inception-date: ca 2005
*   development-stage: mature

Zzrk is a tiny adventure game written in "pure" Zz
(a meta-language normally used for defining compilers.)

#### Implementation: Zzrk (Zz)

    reference: true
    in-distribution: Zzrk distribution
    license: BSD license
    host-language: Zz
    implemented-in-meta: true
    interface: terminal

Implemented Games
-----------------

### Animals

*   genre: Guessing
*   authors: Unknown
*   auspices: Unknown

Animals is a classic "expert system" game.  The computer asks you to think of an
animal, and then asks you a series of yes/no questions in an attempt to
discover what animal you chose.  If it comes to the wrong conclusion, it
asks you for a question that would distinguish the animal that you chose,
and adds it to its database.  In this way it "learns" about more animals
as more games are played.

#### Implementation: animals.erl

*   in-distribution: Animals distribution
*   license: Public Domain
*   inception-date: ca 1999
*   host-language: Erlang
*   interface: terminal
    
    
    Flip:
      type: Game
      genre: Guessing
      vintage: true
      description: |
        Flip is a very simple computer game by John S. James which first appeared
        in the March/April 1977 edition of _Creative Computing_.
        In the game, the computer flips a virtual coin 50 times, and the object is
        for you to guess whether the coin will come up heads or tails each time.
        What makes it interesting is that the coin is not fair.  The computer tries
        to find patterns in your guesses, and exploit them by biasing the coin toss
        away from what it thinks you are likely to guess next.
      specification-link: http://www.atariarchives.org/morebasicgames/showpage.php?page=61
      development-stage: vintage
      authors:
      - John S. James
    
    flip.erl:
      type: Implementation
      implementation-of:
      - Flip
      in-distribution: Flip distribution
      prebuilt-for-platforms:
      - Erlang
      authors:
      - Chris Pressey
      auspices:
      - Cat's Eye Technologies
      license: Public Domain
      inception-date: Jul 31 2002
      host-language: Erlang
      interface: terminal
    
    Hunt the Wumpus:
      type: Game
      genre: Logic
      wikipedia: Hunt_the_Wumpus
      authors:
      - Gregory Yob
      description: |
        Hunt the Wumpus is a classic topological mythical-beast-hunting game
        from the era of teletypes.  [[Gregory Yob]] was disappointed by the
        number of games based on "find an objective hidden on a
        [[2-dimensional]] grid", and decided to design one that was based on
        a world less orthogonal.
      specification-link: http://www.atariarchives.org/morebasicgames/showpage.php?page=178
      development-stage: vintage
    
    wumpus.erl:
      type: Implementation
      implementation-of:
      - Hunt the Wumpus
      in-distribution: Hunt the Wumpus distribution
      prebuilt-for-platforms:
      - Erlang
      authors:
      - Chris Pressey
      auspices:
      - Cat's Eye Technologies
      license: BSD license
      inception-date: Jun 30 2002
      host-language: Erlang
    
    
    Sokoban:
      type: Game
      genre: Puzzle
      wikipedia: Sokoban
      vintage: false
      description: |
        Sokoban is the classic Japanese game about lean manufacturing (well, sort of).
      # need to look this up someday
      no-specification: true
      development-stage: mature
      authors: []
    
    esoko:
      type: Implementation
      implementation-of:
      - Sokoban
      in-distribution: esoko distribution
      prebuilt-for-platforms:
      - Erlang
      authors:
      - Chris Pressey
      auspices:
      - Cat's Eye Technologies
      license: BSD license
      inception-date: Nov 4 2002
      host-language: Erlang
      run-requirements:
      - Tcl/Tk
      description: |
        This version stars Rusty the Cat, from Intelligent Humour, as the protagonist.
      interface: GUI window
      controls: keyboard

- - - -

[Commodore 64]: http://catseye.tc/article/Retrocomputing#commodore-64
[Ophis Assembler]: TBD
[Mini Game Compo 2009]: TBD
[Perl]: TBD
[Hunt the Wumpus]: TBD
