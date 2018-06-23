Game Implementations
====================

*   common auspices: Cat's Eye Technologies
*   common authors: Chris Pressey
*   common development-stage: mature
*   common type: Game Implementation

This is a list of games that Cat's Eye Technologies has implemented,
but which were not designed by Cat's Eye Technologies.
(For those, see [Games](../article/Games.md).)

### animals.erl

*   implementation-of: Animals
*   game-genre: Guessing
*   game-author: Unknown
*   in-distribution: [Animals distribution](http://catseye.tc/distribution/Animals_distribution)
*   license: Public Domain
*   inception-date: ca 1999
*   host-language: Erlang
*   interface: terminal

_Animals_ is a classic "expert system" game.  The computer asks you to think of an
animal, and then asks you a series of yes/no questions in an attempt to
discover what animal you chose.  If it comes to the wrong conclusion, it
asks you for a question that would distinguish the animal that you chose,
and adds it to its database.  In this way it "learns" about more animals
as more games are played.

### flip.erl

*   implementation-of: Flip
*   game-genre: Guessing
*   game-inception-date: 1977
*   game-author: John S. James
*   game-description: [www.atariarchives.org](http://www.atariarchives.org/morebasicgames/showpage.php?page=61)
*   in-distribution: [Flip distribution](http://catseye.tc/distribution/Flip_distribution)
*   license: Public Domain
*   inception-date: Jul 31 2002
*   host-language: Erlang
*   interface: terminal

_Flip_ is a very simple computer game by John S. James which first appeared
in the March/April 1977 edition of _Creative Computing_.
In the game, the computer flips a virtual coin 50 times, and the object is
for you to guess whether the coin will come up heads or tails each time.
What makes it interesting is that the coin is not fair.  The computer tries
to find patterns in your guesses, and exploit them by biasing the coin toss
away from what it thinks you are likely to guess next.

### wumpus.erl

*   implementation-of: Hunt the Wumpus
*   game-genre: Logic
*   game-authors: Gregory Yob
*   game-wikipedia: [Hunt the Wumpus](https://en.wikipedia.org/wiki/Hunt_the_Wumpus)
*   game-description: [www.atariarchives.org](http://www.atariarchives.org/morebasicgames/showpage.php?page=178)
*   in-distribution: [wumpus.erl distribution](http://catseye.tc/distribution/wumpus.erl_distribution)
*   license: BSD license
*   inception-date: Jun 30 2002
*   host-language: Erlang

_Hunt the Wumpus_ is a classic topological mythical-beast-hunting game
from the era of teletypes.  Gregory Yob was disappointed by the
number of games based on "find an objective hidden on a
2-dimensional grid", and decided to design one that was based on
a world less orthogonal.
    
### esoko

*   implementation-of: Sokoban
*   game-genre: Puzzle
*   game-authors: Hiroyuki Imabayashi
*   game-wikipedia: [Sokoban](https://en.wikipedia.org/wiki/Sokoban)
*   in-distribution: [esoko distribution](http://catseye.tc/distribution/esoko_distribution)
*   license: BSD license
*   inception-date: Nov 4 2002
*   host-language: Erlang
*   run-requirements: Tcl/Tk
*   interface: GUI window
*   controls: keyboard

_Sokoban_ is the classic Japanese game about lean manufacturing (well, sort of).

This version stars Rusty the Cat, from Intelligent Humour, as the protagonist.
