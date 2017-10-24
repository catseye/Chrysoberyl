HTML5 Installations
===================

This is a list of [languages][], [automata][], [games][] and [gewgaws][]
which have HTML5 installations hosted online on [Cat's Eye Technologies][]'
website, `catseye.tc`.

It contains some instructions for using each of these installations.

Note: some of the properties on the installation entries are meant to be
more machine-read than human-read, but you can just skip over those.

Internal note: this file should not be used as input when creating a refdex.

Games
-----

### Bubble Escape

*   installation-of: [Bubble Escape 2K][]
*   installed-implementation: bubble_escape_2k.prg
*   interactive: true
*   animated: true
*   mediums: [6502 machine code][], [JaC64][], [Java Web Start][], [HTML5][]

You can play it online in the [JaC64][] emulator using Java Web Start.
Use your arrow keys to guide the bubble through the maze.  Avoid the
hazards and find the five keys to unlock the exit.

If this game doesn't seem too impressive to you, try to remember, it's
only two kilobytes of code!  These days you can't even sneeze in less
than a megabyte.

### Super Wumpus Land

*   installation-of: [Super Wumpus Land][]
*   installed-implementation: swl.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: super-wumpus-land
*   javascript-urls: impl/swl.js/src/swl.js
*   script-root: ../modules/super-wumpus-land/impl/swl.js/src/yoob/

If your keystrokes aren't going into the "terminal", make sure you
click in it first (it's focusable.)

### The Never-Ending Maze

*   installation-of: [The Never-Ending Maze][]
*   installed-implementation: never-ending-maze.z5
*   interactive: true
*   animated: false
*   mediums: [Z-Machine code][], [Zplet][], [Java Web Start][], [HTML5][]

It's a text adventure.  You can play it online in the [Zplet][] emulator using Java Web Start.
Type commands for the actions that you want to undertake in the game.  For instance, `go east`.

### The New Gamerly Realism

*   installation-of: [The New Gamerly Realism][]
*   installed-implementation: the-new-gamerly-realism.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-module: the-new-gamerly-realism
*   javascript-urls: src/the-new-gamerly-realism.js
*   script-root: ../modules/the-new-gamerly-realism/src/

Use the arrow keys to guide the protagonist (represented by a black square)
around the playfield (represented by a black square) to collect all the
treasures (represented by black squares) while avoiding the pits (represented
by black squares.)  Each treasure collected earns the player 10 points; the
score is shown in the upper-left (in black).  The player begins the game with
three lives; succumbing to a pit costs a life; the number of lives is
displayed in the lower-left (in black).  When the game is over, left-click
the canvas to start a new game.

Detractors and other peasants may satisfy themselves that this is actually a
game and not just an entirely black gif or something by opening a Javascript
console and typing `BACKGROUND_COLOR='green'`.

### Cheshire Text

*   installation-of: [Cheshire Text][]
*   installed-implementation: cheshire-text.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-module: html5-gewgaws
*   javascript-urls: cheshire-text/cheshire-text.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Platforms
---------

### BefOS

*   installation-of: [BefOS][]
*   installed-implementation: BefOS (NASM)
*   interactive: true
*   animated: true
*   mediums: [x86 machine code][], [v86][], [HTML5][]

This is an HTML5 installation of [[BefOS]], a Befunge-themed operating
system which is neither Befunge, nor an operating system.  (Discuss.)
It runs on a web page thanks to the
[[HTML5]]-based [[IBM PC compatible]] emulator, [[v86]].

The system is delivered on a 1.44M floppy image, which contains the
BefOS boot block, kernal, and the handful of sample pages which are
included in the default build.

If v86 doesn't work in your browser, you can
[download the disk image](http://catseye.tc/distfiles/befos-0.10.img)
and use it in an emulator such as [[QEMU]] or [[Bochs]] or [[DOSBox]]
or, wonder of wonders, a real IBM PC compatible — if you can write it onto
a floppy disk somehow...

Automata
--------

### Backtracking Wang Tiler

*   installation-of: [Backtracking Wang Tiler][]
*   installed-implementation: backtracking-wang-tiler.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-module: wang-tilers
*   javascript-urls: src/backtracking-wang-tiler.js
*   script-root: ../modules/wang-tilers/src/yoob/

This is an in-browser implementation, in [Javascript][] and [HTML5][],
of a backtracking Wang tiler.

For more information on Wang tiles, see
[the Wikipedia article on Wang tiles](http://en.wikipedia.org/wiki/Wang_tile).

For more information on this automaton and its implementation, see
[the README in the Wang Tilers distribution](https://github.com/catseye/Wang-Tilers).

### Braktif

*   installation-of: [Braktif][]
*   installed-implementation: braktif.alp
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5

This is the [Braktif][] cellular automaton, compiled to Javascript
using [ALPACA][] and animated using [yoob.js][].

Instructions:

Select an example program from the dropdown box, then click "Start" to run
it. Or click "Edit" to modify an example program, or create your own program.

### Chzrxl

*   installation-of: [Chzrxl][]
*   installed-implementation: chzrxl.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-module: html5-gewgaws
*   javascript-urls: chzrxl/chzrxl.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Instructions:

The percentage of balls held fixed can be changed by the slider, and
the "Restart" button can be used to scatter the balls and restart their
movements.  You can try out different values and see which one you like
the best.

Background:

The original idea was this: each ball travels on a
sine-wave path (kind of like a spring) between a randomly-chosen
pair of two other balls.

It was soon discovered that if all balls are free to move like this,
they all quickly collapse to a single point.  Thus, some number of
balls are held fixed (5% by default).  The result is a slightly
organic-seeming emergent motion.

### Circute

*   installation-of: [Circute][]
*   installed-implementation: circute.alp
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]

This is the [Circute][] cellular automaton, compiled to Javascript
using [ALPACA][] and animated using [yoob.js][].

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

### Cyclobots

*   installation-of: [Cyclobots][]
*   installed-implementation: cyclobots.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-module: html5-gewgaws
*   javascript-urls: cyclobots/cyclobots.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/
*   launch-config: { width: 640, height: 480 }

This is an in-browser implementation of [Cyclobots][].

Instructions:

When a revolution occurs, every cyclobot picks a new cyclobot to follow
at random.

In case the cyclobots leave the viewable area of the playfield,
dragging on the playfield will scroll it.

### Jaccia

*   installation-of: [Jaccia][]
*   installed-implementation: jaccia.alp
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]

This is the [Jaccia][] cellular automaton, compiled to Javascript
using [ALPACA][] and animated using [yoob.js][].

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

### Jacciata

*   installation-of: [Jacciata][]
*   installed-implementation: jacciata.alp
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]

This is the [Jacciata][] cellular automaton, compiled to Javascript
using [ALPACA][] and animated using [yoob.js][].

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

### REDGREEN

*   installation-of: [REDGREEN][]
*   installed-implementation: redgreen.alp
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5

This is the [REDGREEN][] cellular automaton, compiled to Javascript using [ALPACA][]
and animated using [yoob.js][].

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

### Schrödinger's Game of Life

*   installation-of: [Schrödinger's Game of Life][]
*   installed-implementation: slife.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: schroedingers-game-of-life
*   javascript-urls: impl/slife.js/src/slife.js
*   script-root: ../modules/schroedingers-game-of-life/impl/slife.js/src/yoob/
*   launch-config: { 'sourceRoot': '../modules/schroedingers-game-of-life/eg/' }

Schrödinger's Game of Life.

### noit o' mnain worb

*   installation-of: [noit o' mnain worb][]
*   installed-implementation: worb.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5

This online interpreter for the
[noit o' mnain worb][] probabilistic particle automaton
is implemented in Javascript, on an HTML5 canvas.

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

Languages
---------

### Etcha

*   installation-of: [Etcha][]
*   installed-implementation: etcha.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5

This in-browser installation of [Etcha][] is implemented in
[Javascript][], using [yoob.js][].

Instructions:

Click "Start" to run the supplied example program.  Or click "Edit" to
modify it, and create your own program.

### Gemooy

*   installation-of: [Gemooy][]
*   installed-implementation: gemooy.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]

This in-browser installation of [Gemooy][] is implemented in
[Javascript][], using [yoob.js][].

Select an example program from the dropdown box, then click "Start" to run
it. Or click "Edit" to modify an example program, or create your own program.

### Matchbox

*   installation-of: [Matchbox][]
*   installed-implementation: matchbox.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: matchbox
*   javascript-urls: src/matchbox-launcher.js
*   script-root: ../modules/matchbox/src/
*   launch-config: { 'sourceRoot': '../modules/matchbox/eg/', 'workerURL': '../modules/matchbox/src/matchbox-worker.js' }

Instructions:

Select an example configuration from the dropdown box, click "Run"
to run either of the programs individually, or "Find Race Conditions"
to compute all interleavings of the two programs and look for race
conditions between them.

### Pixley

*   installation-of: [Pixley][]
*   installed-implementation: pixley.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [Web Workers][], [HTML5][]
*   javascript-module: wang-tilers
*   javascript-urls: src/backtracking-wang-tiler.js
*   script-root: ../modules/wang-tilers/src/yoob/

Instructions:

Select an example program from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example
program, or create your own program.

Background:

This is an online implementation of [Pixley][] which, as a bonus, also
depicts the Pixley program as a set of coloured, nested rectangles.

This [Javascript][] implementation of Pixley uses the *Web Workers*
facility of your browser to run the evaluation process.  So, if your
browser does not support Web Workers, it may not function correctly.

For the Pixley project, a Pixley interpreter was implemented in
Pixley itself ("meta-circularly") and in this installation,
the **Wrap in Pixley Interpreter** button will take the Pixley
program that has been loaded and put it inside this
Pixley-interpreter-in-Pixley.

Evaluating a program wrapped in a Pixley interpreter will result
in the same result as the unwrapped program.  It will just take
longer.

Evaluating a program wrapped in a Pixley interpreter
*wrapped in a Pixley interpreter* will also result
in the same result as the unwrapped program.  It will just take
*quite a bit* longer.

In theory, this "tower" of wrapped interpreters could go on forever,
and they should all produce the same result.

However, in physical reality, computers have limitations, such as
a finite amount of memory available.  In my installation of Firefox,
for example, wrapping a program in three levels of interpreters
results in a "stack overflow" error being displayed in the Javascript
console, and the evaluation process never finishing.

### Shelta

*   installation-of: [Shelta][]
*   installed-implementation: shelta
*   interactive: true
*   animated: true
*   mediums: x86 machine code, FreeDOS, v86, HTML5

This is [Shelta][], a language with a tiny compiler and a
self-hosted compiler, running under [FreeDOS][] running
on a web page via the [HTML5][]-based [IBM PC compatible][]
emulator, [v86][] —  so you can bootstrap it right in your browser.

Instructions:

The system running online on v86 is delivered on a 720K floppy image,
which contains a minimal bootable FreeDOS install, the Shelta distribution,
plus various tools such as the `TED3` text editor, and `YASM`.
License and distribution information is included on the disk image.

You can use the pre-built Shelta compiler (whose source is written in NASM)
to build the example programs, or to bootstrap the Shelta compiler
written in Shelta.  See the welcome message, shown after FreeDOS
boots, for more details.

Documentation for Shelta is also on the disk image, and can be viewed
with `TYPE` or `EDIT`, but you may find it more convenient to browse
these files online:

*   [Original Shelta README, 1999](https://github.com/catseye/Shelta/blob/master/doc/readme.txt)
*   [Making the Snake Eat its Tail: Bootstrapping](https://github.com/catseye/Shelta/blob/master/doc/bootstrp.txt)
*   [Shelta in NASM, 2009](https://github.com/catseye/Shelta/blob/master/doc/nasm2009.txt)
*   [Shelta under FreeDOS, 2013](https://github.com/catseye/Shelta/blob/master/doc/fdos2013.txt)

If v86 doesn't work in your browser, you can
[download the disk image](http://catseye.tc/distfiles/freedos-1.0-shelta-1.2-floppy-2.img)
and use it in an emulator such as [QEMU][] or [Bochs][] or [DOSBox][]
or, wonder of wonders, a real IBM PC compatible — if you can write it onto
a floppy disk somehow...

### Whothm

*   installation-of: [Whothm][]
*   installed-implementation: tc.catseye.whothm
*   interactive: true
*   animated: false
*   mediums: Java Web Start, HTML5

[Whothm][] is a simple language for describing infinite two-colour bitmapped graphics.
This installation contains a Java application which implements Whothm, and lets you
interactively try out Whothm programs online, using Java Web Start. The implementation
is only an approximation; only a small portion of the infinite drawing (a couple of
hundred iterations) is rendered.  The rest is left up to your imagination.

Instructions:

Whothm is a simple language for describing infinite shapes. It is
described fully in the documentation in the [Whothm][] distribution.

Click "Run" or press Alt+R to run the program.  The result is displayed in
the canvas on the right.  Page Up and Page Down can be used to zoom in and
out of the canvas.

Syntax errors often result in an error message in the status bar,
but might not in all cases.  In these cases, consulting your browser's
Java console, if it has one, might elucidate the cause of the error.
Or it might not.

Obviously, this implementation does not support generating or
displaying the entire infinite drawing.  In fact, it only runs the loop
for a couple of hundred iterations.  The full shape is left up to your
imagination.

### Wierd (John Colagioia)

*   installation-of: [Wierd (John Colagioia)][]
*   installed-implementation: wierd-jnc.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: wierd
*   javascript-urls: dialect/wierd-jnc/impl/wierd-jnc.js/src/wierd-jnc.js
*   script-root: ../modules/wierd/dialect/wierd-jnc/impl/wierd-jnc.js/src/yoob/
*   launch-config: { 'sourceRoot': '../modules/wierd/dialect/wierd-jnc/eg/' }

Wierd.

### yoob

*   installation-of: [yoob][]
*   installed-implementation: tc.catseye.yoob
*   interactive: true
*   animated: true
*   mediums: Java Web Start, HTML5

[yoob][] is a public-domain framework for implementing
[esoteric programming languages](Esolang), and allowing them to be
interactively run on programs in a Java application.

Currently, yoob can interpret 21 languages: [1L_AOI][], [1L_a][], [2-ill][], [2L][],
[Ale][], [BackFlip][], [Befunge-93][], [Black][], [brainfuck][], [Circute][], [Etcha][],
[Gemooy][], [LNUSP][], [noit o' mnain worb][], [PATH][], [Qdeql][], [Sceql][],
[SMETANA][], [SNUSP][], [Wunnel][], and [Ypsilax][].  This installation shows yoob in
action, and lets you play with all these esolangs online, using Java Web Start.

### Wunnel

*   installation-of: [Wunnel][]
*   installed-implementation: wunnel.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5

This is an HTML5-based implementation of the
esoteric programming language [Wunnel][].

Instructions:

Select an example program from the drop-down (or click Edit and
compose your own,) then click Run.

When `INP` is highlighted in the instruction matrix, the program is
waiting for input.  Click on the Input text box and input some
`0`s and `1`s (Wunnel programs take bits as input.)  The program
will consume them in order, and continue running.

### ZOWIE

*   installation-of: zowie.py
*   interactive: true
*   animated: false
*   mediums: [Python][], [Skulpt][], [Javascript][], [HTML5][]

This is an [HTML5][]-based interpreter for the
[esoteric programming language][] [ZOWIE][].
The reference implementation of the interpreter, written in [Python][],
is itself being interpreted by [Skulpt][], written in [Javascript][].

Instructions:

Input is not yet supported, and errors are not yet handled
in a user-friendly way, but it does work, as the example sources show.

Select an example program from the dropdown box, then click "Run" to
run it.  Or edit an example program in the text box, or create your own
program.

Gewgaws
-------

### A Minimalist Critique of Tetris

*   installation-of: a-minimalist-critique.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-module: html5-gewgaws
*   javascript-urls: a-minimalist-critique/a-minimalist-critique.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

A minimalist critique of Tetris.

### A Non-Random Walk

*   installation-of: [A Non-Random Walk][]
*   installed-implementation: a-non-random-walk.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-module: html5-gewgaws
*   javascript-urls: a-non-random-walk/a-non-random-walk.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Pick a card, any card.  Half are red, half are black.  Each time a
card is picked, the wheel moves.  The distance moved is always
half the distance from the wheel to the origin (the black dot), *but*
the direction depends on the colour of the card: red moves left,
black moves right.

Because the cards are shuffled, the picks are random, and you might think
that it's not possible to tell where the wheel will stop, once all cards
have been turned over.  However, that's not the case.  The wheel always
stops at a distance *a* - *a* × 0.75^*n* from the origin, where *a* is
the starting position of the wheel, and *n* is the number of red (or black)
cards.

### Art Restoration Simulator

*   installation-of: [Art Restoration Simulator][]
*   installed-implementation: art-restoration-simulator.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-module: html5-gewgaws
*   javascript-urls: art-restoration-simulator/art-restoration-simulator.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/
*   launch-config: { 'artURL': '../modules/html5-gewgaws/art-restoration-simulator/art.jpg', 'controlPanel': document.getElementById('control_panel') }

Use your mouse (or your finger, on a touch device) to restore the artwork.

### Black Hole Poem

*   installation-of: [Black Hole Poem][]
*   installed-implementation: black-hole-poem.js
*   interactive: true
*   animated: false
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: black-hole-poem/black-hole-poem.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Darker-beige squares can be dragged with your mouse or your finger
(for what good it will do you.)

(Yes, you can't see the whole poem.  Yes, that's the point.
Yes, unless you look at the Javascript source.  Yes, that's the point too.)

The background colour is beige because it's based on
[Illuminant E](https://en.wikipedia.org/wiki/Standard_illuminant#Illuminant_E)
because that is our best guess at
[what colour the universe is](http://www.pha.jhu.edu/~kgb/cosspec/).

### Canvas Feedback

*   installation-of: [Canvas Feedback][]
*   installed-implementation: canvas-feedback.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: canvas-feedback
*   javascript-urls: src/canvas-feedback.js
*   script-root: ../modules/canvas-feedback/src/yoob/
*   launch-config: { 'imgUrl': 'http://i.imgur.com/SYFLz1X.jpg', 'controlPanel': document.getElementById('control_panel') }

To begin exploring, we suggest you first try different presets
from the *Presets* drop-down in the control panel on the right.

You can also paste the URL of an image in the *Image URL* text box,
and click "Load", to try a different image.

If you want to get your hands dirty, you can open the *Adjustments*
panel, in which you will find various sliders with which you can
control all the parameters.

#### How can I save an image?

In Firefox, you can right-click on the canvas and select "View image",
and save that.  In other browsers, the easiest way may be to click the
_Pause_ button and take a screenshot.
(You can thank the security model used in the HTML5 canvas for this.)

#### The animation isn't perfectly smooth.

This is an unavoidable consequence of conventional operating systems —
your web browser isn't the only thing that's running, and may not get a
chance to run until it's too late to display the next animation frame.

In other HTML animations, this can be worked around — the animation still
drops frames, but intermediate steps can be computed so that it doesn't
look excessively jerky.  However, that may not be a realistic option here,
due to how the feedback process works.

You can minimize frame-dropping by:

*   choosing a relatively small image
*   finding a sufficiently powerful computer (with sufficiently powerful
    video hardware, especially) to run it on
*   making sure you have no other programs running, and no other tabs
    open in your browser
*   letting your browser "warm up" a bit after closing other tabs etc.,
    so that it doesn't have anything pending to clean up after
*   **not** moving the mouse pointer.

#### Now my desktop is twisting counter-clockwise!

You've just been staring at it too long.

#### Wait, I see _five-fold symmetry_.  Where is that coming from?

To be honest, I really don't know.

#### Background

The idea came about while discussing [Nam June Paik][], and video art in
general, with Gareth Jackson.

It was noted by one of us that, before digital video technology, there were
a number of analogue effects that were employed in video art that aren't
seen as frequently these days.  A notable one was the use of _feedback_, the
simplest version being training a camera on a monitor that is displaying
the feed from that same camera.  More sophisticated applications are
of course possible; a relatively famous example is the 1970's version of
the Doctor Who title sequence.

The question arose: could something analogous could be done with digital
video, and if so, how?

And I came up with this as a simple technique which is similar to video
feedback and which can be implemented straightforwardly in an HTML5
canvas element.

The default image used when Canvas Feedback starts up was designed by
Gareth Jackson specifically to be a pleasing subject for this feedback
process.

### Circus Xamulus

*   installation-of: [Circus Xamulus][]
*   installed-implementation: circus-xamulus.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: circus-xamulus/circus-xamulus.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

### Eine kleine Glitchfraktal

*   installation-of: [Eine kleine Glitchfraktal][]
*   installed-implementation: eine-kleine-glitchfraktal.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: eine-kleine-glitchfraktal/eine-kleine-glitchfraktal.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Select a mode from from the MODE dropdown to see different styles
of glitching applied to the rectangles.

### Fibonacci Spiral

*   installation-of: [Fibonacci Spiral][]
*   installed-implementation: fibonacci-spiral.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: fibonacci-spiral/fibonacci-spiral.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

The semicircles alternate being on the left and the right.  The first
two terms of the Fibonacci sequence are `1, 1` and these make up the unit
circle in the center of the spiral.

The animation is simply a zooming out and back in on the spiral.

### Fingerspelling

*   installation-of: [Fingerspelling][]
*   installed-implementation: fingerspelling.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: fingerspelling/fingerspelling.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

If you have a touchscreen, prod the lavender area of the screen with your
finger.  If you don't have a touchscreen, you may simulate this action
with your mouse pointer.

### Heronsis hermnonicii

*   installation-of: [Heronsis hermnonicii][]
*   installed-implementation: heronsis-hermnonicii.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: heronsis-hermnonicii/heronsis-hermnonicii.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

*Warning: the following may contain tedious and/or glib
background and/or analysis.*

Casting a negative space of knowledge.  Calling itself a "plate" frames
it as a work of learning, like some kind of 19th-century anthropology text.
Yet it only raises questions — what are these entities?  what kind of
world do they inhabit?  what are they protecting?  who is Clarkson?
— without providing answers, leaving it up to the observer to either
imagine their own answers, or decide that answers to these questions
are not necessary.

Plus it's fun to click on the red balls.

### Hirsute Miasma

*   installation-of: [Hirsute Miasma][]
*   installed-implementation: hirsute-miasma.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: hirsute-miasma/hirsute-miasma.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

The animation will eventually cycle if you're patient (although it won't
of course cycle exactly, as there is a random element.)  You may enable
the "terminal" option to prevent this cycling.

### Hypongtrochoid

*   installation-of: [Hypongtrochoid][]
*   installed-implementation: hypongtrochoid.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: hypongtrochoid/hypongtrochoid.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Each box moves with a constant velocity
relative to the box it is contained in, and bounces around inside it in a
simple fashion.  Yet the path traced out by the innermost box is not very
simple at all.

### Lexeduct

*   installation-of: [Lexeduct][]
*   installed-implementation: lexeduct-browser.js
*   interactive: true
*   animated: false
*   mediums: Javascript, HTML5
*   javascript-module: lexeduct
*   javascript-urls: demo/lexeduct-transformers.js, demo/yoob/element-factory.js, demo/lexeduct-browser.js
*   script-root: ../modules/lexeduct/src/

### Markov Font

*   installation-of: [Markov Font][]
*   installed-implementation: markov-font.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: markov-font/markov-font.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

### Multicolouralism

*   installation-of: [Multicolouralism][]
*   installed-implementation: multicolouralism.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: multicolouralism/multicolouralism.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Each frame, the colour of each cell is chosen randomly from the set
{cyan, magenta, yellow, white}.  The probability of each of the
colours is determined by the distance from the cell to each corner
of the square, raised to a power (the "field strength") which can
be selected by the slider.

Do you see false colours at the "borders" between the "fields"?
You certainly *can*, but how much you see them seems to depend on
several factors (your computer, monitor, lighting, persistence
of vision, focus and peripheral vision...)

### Noise to Signal No. 1

*   installation-of: [Noise to Signal No. 1][]
*   installed-implementation: noise-to-signal-1.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: noise-to-signal-1/noise-to-signal-1.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

The two panels are constructed by randomly distributing the pixels from
a source image randomly onto either panel.

### Plea of Thunder

*   installation-of: [Plea of Thunder][]
*   installed-implementation: PleaOfThunder.java
*   interactive: false
*   animated: true
*   mediums: Java applet, HTML5

### Prairie

*   installation-of: [Prairie][]
*   installed-implementation: prairie.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: prairie/prairie.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/
*   launch-config: { 'imgURL': '../modules/html5-gewgaws/prairie/Elevator_1_(PSF).png' }

### Progression

*   installation-of: [Progression][]
*   installed-implementation: progression.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: progression/progression.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/


### Radialjective

*   installation-of: [Radialjective][]
*   installed-implementation: radialjective.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: radialjective/radialjective.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

### Tentacles, Undamped

*   installation-of: [Tentacles, Undamped][]
*   installed-implementation: tentacles-undamped.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: tentacles-undamped/tentacles-undamped.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

### Text Uniquifier

*   installation-of: [Text Uniquifier][]
*   installed-implementation: text-uniquifier.js
*   interactive: true
*   animated: false
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: text-uniquifier/text-uniquifier.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Copy some text of your choosing (from a web page, a local document, etc.)
and paste it into the text area in the top half of the page.  Then click
"Uniquify" and see the uniquified text in the bottom half of the page.

Case-sensitive means that `THIS`, `This`, and `this` are treated as different
words for uniquification purposes.

Punctuation-sensitive means that `this`, `this?`, `"this"` and `(this` are
treated as different words for uniquification purposes.

You can also select to retain paragraph breaks only (output will look fairly
similar to the input text), all line breaks (output tends to resemble
free verse), or no breaks at all (output is one long unbroken stream of text.)

### The Frame

*   installation-of: [The Frame][]
*   installed-implementation: the-frame.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: the-frame/the-frame.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/
*   launch-config: { 'imgURL': '../modules/html5-gewgaws/the-frame/the-frame.png' }

Note 1. Green things can be dragged.  
Note 2. Due to technical limitations, things cannot be dragged off
of the computer screen.

### The Judgment of Paris

*   installation-of: [The Judgment of Paris][]
*   installed-implementation: the-judgment-of-paris.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: the-judgment-of-paris/the-judgment-of-paris.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/


### Two Fifty Six

*   installation-of: [Two Fifty Six][]
*   installed-implementation: two-fifty-six.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: two-fifty-six/two-fifty-six.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/


### Uncle Ankur

*   installation-of: [Uncle Ankur][]
*   installed-implementation: uncle-ankur.js
*   interactive: false
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: uncle-ankur/uncle-ankur.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

### Woman on Film

*   installation-of: [Woman on Film][]
*   installed-implementation: woman-on-film.js
*   interactive: true
*   animated: true
*   mediums: Javascript, HTML5
*   javascript-module: html5-gewgaws
*   javascript-urls: woman-on-film/woman-on-film.js
*   script-root: ../modules/html5-gewgaws/common-yoob.js-0.11/

Use the navigation buttons to traverse the space of the work.

- - - -

[Cat's Eye Technologies]: ../article/General%20Information.md#cats-eye-technologies
[esoteric programming language]: ../article/General%20Information.md#esolang
[languages]: ../article/Languages.md
[automata]: ../article/Automata.md
[games]: ../article/Games.md
[gewgaws]: ../article/Gewgaws.md
[JaC64]: ../article/Retrocomputing.md#commodore-64
[Zplet]: ../article/Retrocomputing.md#z-machine
[Z-Machine code]: ../article/Retrocomputing.md#z-machine
[Javascript]: http://www.ecma-international.org/publications/standards/Ecma-262.htm
[Web Workers]: https://en.wikipedia.org/wiki/Web_worker
[6502 machine code]: ../article/Retrocomputing.md#6502
[x86 machine code]: ../article/Retrocomputing.md#ms-dos
[v86]: ../article/Retrocomputing.md#ms-dos
[Java Web Start]: http://docs.oracle.com/javase/8/docs/technotes/guides/javaws/
[HTML5]: https://www.w3.org/TR/html5/
[Python]: http://www.python.org/
[Skulpt]: http://www.skulpt.org/
[Nam June Paik]: https://en.wikipedia.org/wiki/Nam_June_Paik
[Bubble Escape 2K]: ../article/Games.md#bubble-escape
[The New Gamerly Realism]: ../article/Games.md#the-new-gamerly-realism
[The Never-Ending Maze]: ../article/Games.md#the-never-ending-maze
[Super Wumpus Land]: ../article/Games.md#super-wumpus-land
[Cheshire Text]: ../article/Texts.md#cheshire-text
[BefOS]: ../article/Platforms.md#befos
[Backtracking Wang Tiler]: ../article/Automata.md#backtracking-wang-tiler
[Chzrxl]: ../article/Automata.md#chzrxl
[Pixley]: ../article/Languages.md#pixley
[Gemooy]: ../article/Languages.md#gemooy
[ZOWIE]: ../article/Languages.md#zowie
[yoob.js]: ../article/Tools.md#yoobjs
[1L_AOI]: http://esolangs.org/wiki/1L_AOI
[1L_a]: http://esolangs.org/wiki/1L_a
[2-ill]: http://esolangs.org/wiki/2-ill
[2L]: http://esolangs.org/wiki/2L
[ALPACA]: ../article/Languages.md#alpaca
[Ale]: http://esolangs.org/wiki/Ale
[BackFlip]: http://esolangs.org/wiki/BackFlip
[Befunge-93]: ../article/Languages.md#befunge-93
[Black]: http://esolangs.org/wiki/Black
[Bochs]: ../article/Retrocomputing.md#ms-dos
[Braktif]: ../article/Automata.md#braktif
[Circute]: ../article/Automata.md#circute
[Cyclobots]: ../article/Automata.md#cyclobots
[DOSBox]: ../article/Retrocomputing.md#ms-dos
[Etcha]: ../article/Languages.md#etcha
[FreeDOS]: ../article/Retrocomputing.md#ms-dos
[IBM PC compatible]: ../article/Retrocomputing.md#ibm-pc-compatible
[Jaccia]: ../article/Automata.md#jaccia
[Jacciata]: ../article/Automata.md#jacciata
[LNUSP]: http://esolangs.org/wiki/LNUSP
[PATH]: http://esolangs.org/wiki/PATH
[QEMU]: ../article/Retrocomputing.md#ms-dos
[Qdeql]: http://esolangs.org/wiki/Qdeql
[REDGREEN]: ../article/Automata.md#redgreen
[SMETANA]: ../article/Automata.md#smetana
[SNUSP]: http://esolangs.org/wiki/SNUSP
[Sceql]: http://esolangs.org/wiki/Sceql
[Shelta]: ../article/Languages.md#shelta
[Whothm]: ../article/Languages.md#whothm
[Wunnel]: ../article/Languages.md#wunnel
[Ypsilax]: ../article/Languages.md#ypsilax
[brainfuck]: http://esolangs.org/wiki/brainfuck
[noit o' mnain worb]: ../article/Automata.md#noit-o-mnain-worb
[yoob]: ../article/Archived.md#yoob
