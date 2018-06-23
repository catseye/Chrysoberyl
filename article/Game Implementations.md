Game Implementations
====================

*   common auspices: Cat's Eye Technologies
*   common authors: Chris Pressey
*   common development-stage: mature
*   common type: Game

This is a list of games that Cat's Eye Technologies has implemented,
but which were not designed by Cat's Eye Technologies.
(For those, see [Games](../article/Games.md).)

Note that the distinctions between a Game and a Gewgaw or even an Automaton are not always clear,
and entries here may be categorized somewhat arbitrarily.

### Animals

*   genre: Guessing
*   authors: Unknown
*   auspices: Unknown

_Animals_ is a classic "expert system" game.  The computer asks you to think of an
animal, and then asks you a series of yes/no questions in an attempt to
discover what animal you chose.  If it comes to the wrong conclusion, it
asks you for a question that would distinguish the animal that you chose,
and adds it to its database.  In this way it "learns" about more animals
as more games are played.

#### Implementation: animals.erl

*   in-distribution: [Animals distribution](http://catseye.tc/distribution/Animals_distribution)
*   license: Public Domain
*   inception-date: ca 1999
*   host-language: Erlang
*   interface: terminal

### Flip

*   genre: Guessing
*   inception-date: 1977
*   authors: John S. James
*   auspices: Unknown
*   specification-link: [www.atariarchives.org](http://www.atariarchives.org/morebasicgames/showpage.php?page=61)

_Flip_ is a very simple computer game by John S. James which first appeared
in the March/April 1977 edition of _Creative Computing_.
In the game, the computer flips a virtual coin 50 times, and the object is
for you to guess whether the coin will come up heads or tails each time.
What makes it interesting is that the coin is not fair.  The computer tries
to find patterns in your guesses, and exploit them by biasing the coin toss
away from what it thinks you are likely to guess next.

#### Implementation: flip.erl

*   in-distribution: [Flip distribution](http://catseye.tc/distribution/Flip_distribution)
*   license: Public Domain
*   inception-date: Jul 31 2002
*   host-language: Erlang
*   interface: terminal
    
### Hunt the Wumpus

*   genre: Logic
*   authors: Gregory Yob
*   auspices: Unknown
*   wikipedia: [Hunt the Wumpus](https://en.wikipedia.org/wiki/Hunt_the_Wumpus)
*   specification-link: [www.atariarchives.org](http://www.atariarchives.org/morebasicgames/showpage.php?page=178)

_Hunt the Wumpus_ is a classic topological mythical-beast-hunting game
from the era of teletypes.  Gregory Yob was disappointed by the
number of games based on "find an objective hidden on a
2-dimensional grid", and decided to design one that was based on
a world less orthogonal.

#### Implementation: wumpus.erl

*   in-distribution: [wumpus.erl distribution](http://catseye.tc/distribution/wumpus.erl_distribution)
*   license: BSD license
*   inception-date: Jun 30 2002
*   host-language: Erlang
    
### Sokoban

*   genre: Puzzle
*   authors: Hiroyuki Imabayashi
*   auspices: Unknown
*   wikipedia: [Sokoban](https://en.wikipedia.org/wiki/Sokoban)

_Sokoban_ is the classic Japanese game about lean manufacturing (well, sort of).
    
#### Implementation: esoko

*   in-distribution: [esoko distribution](http://catseye.tc/distribution/esoko_distribution)
*   license: BSD license
*   inception-date: Nov 4 2002
*   host-language: Erlang
*   run-requirements: Tcl/Tk
*   interface: GUI window
*   controls: keyboard

This version stars Rusty the Cat, from Intelligent Humour, as the protagonist.
