HTML5 Installations
===================

*   image_url: https://static.catseye.tc/images/illustrations/Perpetual_Motion_Machine.jpg
*   ok-to-use-as-input-when-creating-a-refdex: false

This is a list of [games][], [platforms][], [automata][], [languages][], and [gewgaws][]
which have HTML5 installations hosted online on [Cat's Eye Technologies][]'
website, `catseye.tc`.

It contains some instructions for using each of these installations.

Note: some of the properties on the installation entries are meant to be
more machine-read than human-read, but you can just skip over those.

### Cosmos Boulders

*   installation-of: [Cosmos Boulders][]
*   installed-implementation: cosmos-boulders.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/cosmos-boulders/contrib/immutable-3.8.2/dist/immutable.min.js,../modules/cosmos-boulders/contrib/redux-4.0.1/dist/redux.min.js,../modules/cosmos-boulders/src/cosmos-boulders.js
*   launch-command: launch({ container: document.getElementById("installation") });
*   inline-description: below
*   online @ [catseye.tc](https://catseye.tc/ix/Cosmos_Boulders)

_Cosmos Boulders_ is an arcade-style HTML5 minigame built with reducers
and immutable data in ES5 JavaScript.

It is playable with keyboard only.  (It will therefore not be playable
on most mobile devices, as they lack keyboards.)  The key mappings are:

*   Insert coin: **5**
*   Start: **1**
*   Fire: **Ctrl** (left or right)
*   Thrust: **Up Arrow**
*   Rotate left: **Left Arrow**
*   Rotate right: **Right Arrow**

If your keypresses seem to be ignored, try clicking inside
the canvas to make sure it's got the keyboard focus.

### Super Wumpus Land

*   installation-of: [Super Wumpus Land][]
*   installed-implementation: swl.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/super-wumpus-land/impl/swl.js/src/swl.js
*   script-root: ../modules/super-wumpus-land/impl/swl.js/src/yoob/
*   online @ [catseye.tc](https://catseye.tc/ix/Super_Wumpus_Land)

It is playable with keyboard only.  It will therefore not be playable
on most mobile devices, as they lack keyboards.

If your keystrokes aren't going into the "terminal", make sure you
click in it first (it's focusable.)

### The New Gamerly Realism

*   installation-of: [The New Gamerly Realism][]
*   installed-implementation: the-new-gamerly-realism.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/the-new-gamerly-realism/src/the-new-gamerly-realism.js
*   script-root: ../modules/the-new-gamerly-realism/src/
*   extra-stylesheets: ../stylesheet/mainstage-400x400.css
*   online @ [catseye.tc](https://catseye.tc/ix/The_New_Gamerly_Realism)

#### Background

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

#### Instructions

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
*   javascript-urls: ../modules/html5-gewgaws/cheshire-text/cheshire-text.js
*   script-root: ../modules/html5-gewgaws/cheshire-text/yoob/
*   style: article { margin: 0; } #installation { padding: 2em; }
*   online @ [catseye.tc](https://catseye.tc/ix/Cheshire_Text)

As if there aren't enough remixes of Lewis Carroll's works already.

Instructions:

Just read the text from beginning to end, at a normal reading rate,
and you may be pleasantly surprised.

### BefOS

*   installation-of: [BefOS][]
*   installation-description: This is a web-based installation of [BefOS][], a Befunge-themed operating system which is neither Befunge, nor an operating system.  (Discuss.)
*   installed-implementation: BefOS (NASM)
*   interactive: true
*   animated: true
*   mediums: [x86 machine code][], [v86][], [HTML5][]
*   v86-floppy-image-url: ../resource/befos-0.10.img
*   online @ [catseye.tc](https://catseye.tc/ix/BefOS)

It runs on a web page thanks to the
[HTML5][]-based [IBM PC compatible][] emulator, [v86][].

The system is delivered on a 1.44M floppy image, which contains the
BefOS boot block, kernal, and the handful of sample pages which are
included in the default build.

If v86 doesn't work in your browser, you can
[download the disk image](https://catseye.tc/distfiles/befos-0.10.img)
and use it in an emulator such as [QEMU][] or [DOSBox][]
or, wonder of wonders, a real IBM PC compatible — if you can write it onto
a floppy disk somehow...

### Backtracking Wang Tiler

*   installation-of: [Backtracking Wang Tiler][]
*   installation-description: This is an in-browser implementation, in [Javascript][] and [HTML5][], of a [Backtracking Wang Tiler][].
*   installed-implementation: backtracking-wang-tiler.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/backtracking-wang-tiler/src/backtracking-wang-tiler.js
*   script-root: ../modules/backtracking-wang-tiler/src/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-440x440.css
*   online @ [catseye.tc](https://catseye.tc/ix/Backtracking_Wang_Tiler)

For more information on Wang tiles, see
[the Wikipedia article on Wang tiles](http://en.wikipedia.org/wiki/Wang_tile).

For more information on this automaton and its implementation, see
the entry for [Backtracking Wang Tiler][].

### Braktif

*   installation-of: [Braktif][]
*   installation-description: This is the [Braktif][] cellular automaton, compiled to Javascript using [ALPACA][] and animated using [yoob.js][].
*   installed-implementation: braktif.alp
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/braktif/script/braktif.js,../modules/braktif/eg/index.js,../modules/braktif/demo/braktif-launcher.js
*   script-root: ../modules/braktif/demo/
*   style: #panel_container { display: inline-block; text-align: left; }
*   online @ [catseye.tc](https://catseye.tc/ix/Braktif)

Instructions:

Select an example program from the dropdown box, then click "Start" to run
it. Or click "Edit" to modify an example program, or create your own program.

You may wish to read the definition of this cellular automaton:
[braktif.alp](https://github.com/catseye/Braktif/blob/master/src/braktif.alp).

### Burro

*   installation-of: [Burro][]
*   installation-description: This is a web-based interpreter for the esoteric programming language [Burro][].
*   installed-implementation: burro.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Burro/eg/examplePrograms.jsonp.js,../modules/Burro/demo/burro-hastec-launcher.js,../modules/Burro/demo/burro.js
*   launch-command: launch({ container: document.getElementById('installation') });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Burro)

Technically, it is `Burro.lhs` (the reference implementation
of Burro, written in Literate [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Burro programming language](https://catseye.tc/view/Burro/README.md).

### Carriage

*   installation-of: [Carriage][]
*   installation-description: This is a web-based interpreter for the "purely concatentive" programming language [Carriage][].
*   installed-implementation: carriage.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Carriage/eg/examplePrograms.jsonp.js,../modules/Carriage/demo/hastec-launcher.js,../modules/Carriage/demo/carriage.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "fun.carriage" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Carriage)

Technically, it is `Language.Carriage` (the reference implementation
of Carriage, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Carriage programming language](https://catseye.tc/view/Carriage/README.md).

### Chzrxl

*   installation-of: [Chzrxl][]
*   installed-implementation: chzrxl.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][], [PixiJS][]
*   javascript-urls: ../contrib/pixi.js-v4.8.5/pixi.min.js,../modules/Chzrxl/src/chzrxl.js,../modules/Chzrxl/demo/dam-plus-widgets-web.js,../modules/Chzrxl/demo/chzrxl-pixi-launcher.js
*   launch-command: launch({ width: 500, height: 500, container: document.getElementById('installation') });
*   style: #installation canvas { background-color: #ffffff; border: 1px solid red }
*   extra-stylesheets: ../stylesheet/mainstage-500x500.css
*   online @ [catseye.tc](https://catseye.tc/ix/Chzrxl)

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
*   installation-description: This is the [Circute][] cellular automaton, compiled to Javascript using [ALPACA][] and animated using [yoob.js][].
*   installed-implementation: circute.alp
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/circute/eg/index.js,../modules/circute/demo/circute-launcher.js
*   script-root: ../modules/circute/demo/
*   style: #display_container { display: inline-block; } canvas { background: #ffffff; border: 1px solid black; display: none; } #panel_container { display: inline-block; text-align: left; }
*   online @ [catseye.tc](https://catseye.tc/ix/Circute)

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

You may wish to read the definition of this cellular automaton:
[circute.alp](https://github.com/catseye/Circute/blob/master/src/circute.alp).

### Cyclobots

*   installation-of: [Cyclobots][]
*   installed-implementation: cyclobots.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][], [PixiJS][]
*   javascript-urls: ../contrib/pixi.js-v4.8.5/pixi.min.js,../contrib/pixi-viewport.js-3.4.1/pixi-viewport.min.js,../modules/Cyclobots/src/cyclobots.js,../modules/Cyclobots/demo/dam-plus-widgets-web.js,../modules/Cyclobots/demo/cyclobots-pixi-launcher.js
*   launch-command: launch({ width: 640, height: 480, container: document.getElementById('installation') });
*   style: #installation canvas { background-color: #ffffff; border: 1px solid blue }
*   extra-stylesheets: ../stylesheet/mainstage-640x480.css
*   online @ [catseye.tc](https://catseye.tc/ix/Cyclobots)

Instructions:

When a revolution occurs, every cyclobot picks a new cyclobot to follow
at random.

In case the cyclobots leave the viewable area of the playfield,
dragging on the playfield will scroll it.  (Possibly not working right now)

### Jaccia

*   installation-of: [Jaccia][]
*   installation-description: This is the [Jaccia][] cellular automaton, compiled to Javascript using [ALPACA][] and animated using [yoob.js][].
*   installed-implementation: jaccia.alp
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/jaccia/eg/index.js,../modules/jaccia/demo/jaccia-launcher.js
*   script-root: ../modules/jaccia/demo/
*   style: #display_container { display: inline-block; } canvas { background: #ffffff; border: 1px solid black; display: none; } #panel_container { display: inline-block; text-align: left; }
*   online @ [catseye.tc](https://catseye.tc/ix/Jaccia)

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

You may wish to read the definition of this cellular automaton:
[jaccia.alp](https://github.com/catseye/Jaccia/blob/master/src/jaccia.alp).

You may also wish to check out this automaton's close relative,
[Jacciata](https://catseye.tc/installation/Jacciata).

### Jacciata

*   installation-of: [Jacciata][]
*   installation-description: This is the [Jacciata][] cellular automaton, compiled to Javascript using [ALPACA][] and animated using [yoob.js][].
*   installed-implementation: jacciata.alp
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/jaccia/eg/index.js,../modules/jaccia/demo/jacciata-launcher.js
*   script-root: ../modules/jaccia/demo/
*   style: #display_container { display: inline-block; } canvas { background: #ffffff; border: 1px solid black; display: none; } #panel_container { display: inline-block; text-align: left; }
*   online @ [catseye.tc](https://catseye.tc/ix/Jacciata)

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

You may wish to read the definition of this cellular automaton:
[jacciata.alp](https://github.com/catseye/Jaccia/blob/master/src/jacciata.alp).

You may also wish to check out this automaton's close relative,
[Jaccia](https://catseye.tc/installation/Jaccia).

### REDGREEN

*   installation-of: [REDGREEN][]
*   installation-description: This is the [REDGREEN][] cellular automaton, compiled to Javascript using [ALPACA][] and animated using [yoob.js][].
*   installed-implementation: redgreen.alp
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/redgreen/script/redgreen.js,../modules/redgreen/eg/index.js,../modules/redgreen/demo/redgreen-launcher.js
*   script-root: ../modules/redgreen/demo/
*   style: #panel_container { display: inline-block; text-align: left; }
*   online @ [catseye.tc](https://catseye.tc/ix/REDGREEN)

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

You may wish to read the definition of this cellular automaton:
[redgreen.alp](https://github.com/catseye/REDGREEN/blob/master/src/redgreen.alp).

### Schrödinger's Game of Life

*   installation-of: [Schrödinger's Game of Life][]
*   installed-implementation: slife.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/schroedingers-game-of-life/impl/slife.js/src/slife.js
*   launch-command: launch('../modules/schroedingers-game-of-life/impl/slife.js/src/yoob/', 'installation', { 'sourceRoot': '../modules/schroedingers-game-of-life/eg/' });
*   style: label { display: block; }
*   online @ [catseye.tc](https://catseye.tc/ix/Schrödinger's_Game_of_Life)

Instructions:

Select a example configuration from the "Preset:" dropdown,
and click "Start" to watch it evolve.  Or click "Edit" to
provide your own configuration.

### noit o' mnain worb

*   installation-of: [noit o' mnain worb][]
*   installation-description: This is a web-based implementation of the [noit o' mnain worb][] probabilistic particle automaton, implemented in Javascript on an HTML5 canvas.
*   installed-implementation: worb.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/noit-o-mnain-worb/impl/worb.js/src/worb-launcher.js,../modules/noit-o-mnain-worb/eg/index.js
*   script-root: ../modules/noit-o-mnain-worb/impl/worb.js/src/
*   style: #load_indicator { border: 1px solid purple; padding: 2px; } #control_panel { text-align: left; display: inline-block; } #installation canvas { background-color: #ffffff; border: 1px solid blue }
*   online @ [catseye.tc](https://catseye.tc/ix/noit_o'_mnain_worb)

Instructions:

Select an example configuration from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example,
or create your own.

### Emmental

*   installation-of: [Emmental][]
*   installation-description: This is a web-based interpreter for the esoteric programming language [Emmental][].
*   installed-implementation: emmental.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Emmental/eg/examplePrograms.jsonp.js,../modules/Emmental/demo/hastec-io-launcher.js,../modules/Emmental/demo/emmental.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "hello.emmental" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Emmental)

Technically, it is `Emmental.hs` (the reference implementation
of Emmental, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

Some programs take input.  When running one of these
programs, you should type all the input into the input box
before running the program.

You might also want to read
[the description of the Emmental programming language](https://catseye.tc/view/Emmental/README.md).

### Equipage

*   installation-of: [Equipage][]
*   installation-description: This is a web-based interpreter for the "purely concatentive" programming language [Equipage][].
*   installed-implementation: equipage.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Equipage/eg/examplePrograms.jsonp.js,../modules/Equipage/demo/hastec-launcher.js,../modules/Equipage/demo/equipage.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "pop-all-positives.equipage" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Equipage)

Technically, it is `Language.Equipage` (the reference implementation
of Equipage, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Equipage programming language](https://catseye.tc/view/Equipage/README.md).

### Etcha

*   installation-of: [Etcha][]
*   installed-implementation: etcha.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Etcha/impl/etcha.js/src/etcha-launcher.js,../modules/Etcha/eg/index.js
*   script-root: ../modules/Etcha/impl/etcha.js/src/
*   style: #installation { text-align: left; margin: 1em; } #playfield_canvas { border: 1px solid blue; margin: 3px; background: white; display: block; } #program_display { border: 1px solid red; }
*   online @ [catseye.tc](https://catseye.tc/ix/Etcha)

It is implemented in [Javascript][], using [yoob.js][].

Instructions:

Click "Start" to run the supplied example program.  Or click "Edit" to
modify it, and create your own program.

### Flobnar

*   installation-of: [Flobnar][]
*   installation-description: This is a web-based interpreter for the esoteric programming language [Flobnar][].
*   installed-implementation: flobnar.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Flobnar/eg/examplePrograms.jsonp.js,../modules/Flobnar/demo/flobnar-hastec-launcher.js,https://static.catseye.tc/generated-js/flobnar-1.0-2019.0328/flobnar.js
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Flobnar)

Technically, it is `Flobnar.hs` (the reference implementation
of Flobnar, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Flobnar programming language](https://catseye.tc/view/Flobnar/README.markdown).

### Gemooy

*   installation-of: [Gemooy][]
*   installed-implementation: gemooy.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Gemooy/eg/index.js,../modules/Gemooy/src/gemooy-launcher.js
*   script-root: ../modules/Gemooy/src/
*   style: #installation { text-align: left; margin: 1em; } #canvas_viewport { width: 100%; height: 420px; background-color: gainsboro; border: 1px solid black; overflow: scroll; scroll-behavior: auto; scrollbar-width: auto; scrollbar-color: rgb(23, 38, 182) rgb(162, 170, 238); } canvas { background-color: white; }
*   online @ [catseye.tc](https://catseye.tc/ix/Gemooy)

It is implemented in [Javascript][], using [yoob.js][].

Select an example program from the dropdown box, then click "Start" to run
it. Or click "Edit" to modify an example program, or create your own program.

Note that the rendering of the program may be larger than the viewport it is
displayed in, and on mobile, said viewport might not display
scrollbars to indicate this.  You can still scroll the program display.

### ILLGOL

*   installation-of: [ILLGOL][]
*   installation-description: This is [ILLGOL][], a communicable disease disguised as a programming language, running under [FreeDOS][] running on a web page via the [HTML5][]-based [IBM PC compatible][] emulator, [v86][].
*   installed-implementation: illgol.exe
*   interactive: true
*   animated: true
*   mediums: [x86 machine code][], [FreeDOS][], [v86][], [HTML5][]
*   v86-floppy-image-url: ../resource/freedos-1.1-illgol-floppy-0.1.img
*   online @ [catseye.tc](https://catseye.tc/ix/ILLGOL)

Instructions:

The system that v86 runs is delivered on a 720K floppy image,
which contains a minimal bootable FreeDOS install, the ILLGOL distribution,
plus various tools such as the `TED3` text editor.
License and distribution information is included on the disk image.

You can use these tools to build and run ILLGOL programs.
See the welcome message, shown after FreeDOS
boots, for more details.

If v86 doesn't work in your browser, you can
[download the disk image](https://catseye.tc/distfiles/freedos-1.1-illgol-floppy-0.1.img)
and use it in an emulator such as [QEMU][] or [DOSBox][]
or, wonder of wonders, a real IBM PC compatible — if you can write it onto
a floppy disk somehow...

### Mascarpone

*   installation-of: [Mascarpone][]
*   installation-description: This is a web-based interpreter for the esoteric programming language [Mascarpone][].
*   installed-implementation: mascarpone.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Mascarpone/eg/examplePrograms.jsonp.js,../modules/Mascarpone/demo/hastec-io-launcher.js,../modules/Mascarpone/demo/mascarpone.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "hello.mascarpone" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Mascarpone)

Technically, it is `Mascarpone.hs` (the reference implementation
of Mascarpone, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

Some programs take input.  When running one of these
programs, you should type all the input into the input box
before running the program.

You might also want to read
[the description of the Mascarpone programming language](https://catseye.tc/view/Mascarpone/README.md).

### Matchbox

*   installation-of: [Matchbox][]
*   installed-implementation: matchbox.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/matchbox/src/matchbox-launcher.js
*   launch-command: launch('../modules/matchbox/src/', 'installation', { 'sourceRoot': '../modules/matchbox/eg/', 'workerURL': '../modules/matchbox/src/matchbox-worker.js' });
*   online @ [catseye.tc](https://catseye.tc/ix/Matchbox)

Instructions:

Select an example configuration from the dropdown box, click "Run"
to run either of the programs individually, or "Find Race Conditions"
to compute all interleavings of the two programs and look for race
conditions between them.

This [Javascript][] implementation of Matchbox uses the *Web Workers*
facility of your browser to run the evaluation process.  So, if your
browser does not support Web Workers, it may not function correctly.

### Oxcart

*   installation-of: [Oxcart][]
*   installation-description: This is a web-based interpreter for the continuation-passing concatentive programming language [Oxcart][].
*   installed-implementation: oxcart.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Oxcart/eg/examplePrograms.jsonp.js,../modules/Oxcart/demo/hastec-launcher.js,../modules/Oxcart/demo/oxcart.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "count-down.oxcart" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Oxcart)

Technically, it is `Language.Oxcart` (the reference implementation
of Oxcart, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Oxcart programming language](https://catseye.tc/view/Oxcart/README.md).

### Pail

*   installation-of: [Pail][]
*   installation-description: This is a web-based interpreter for the esoteric programming language [Pail][].
*   installed-implementation: pail.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Pail/eg/examplePrograms.jsonp.js,../modules/Pail/demo/hastec-launcher.js,../modules/Pail/demo/pail.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "cons.pail" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Pail)

Technically, it is `Pail.lhs` (the reference implementation
of Pail, written in Literate [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Pail programming language](https://catseye.tc/view/Pail/README.md).

### Pixley

*   installation-of: [Pixley][]
*   installed-implementation: pixley.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [Web Workers][], [HTML5][]
*   javascript-urls: ../modules/pixley/impl/pixley.js/demo/launch-pixley.js
*   launch-command: launch('../modules/pixley/impl/pixley.js/', 'installation', { 'workerURL': '../modules/pixley/impl/pixley.js/src/pixley-worker.js' });
*   style: .flex-container { display: flex; margin-left: 1em; margin-right: 1em; } .execution-panel { display: inline-block; flex: 1 1 auto; } .execution-panel pre { max-width: 80em; min-height: 3em; } .depiction-panel { display: inline-block; flex: 1 1 auto; } canvas { margin-top: 0.5em; margin-bottom: 0.5em; border: 3px solid white; }
*   online @ [catseye.tc](https://catseye.tc/ix/Pixley)

Instructions:

Select an example program from the dropdown box,
then click "Start" to run it.  Or click "Edit" to modify an example
program, or create your own program.

Background:

This is a web-based implementation of [Pixley][] which, as a bonus, also
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

### PL-{GOTO}

*   installation-of: [PL-{GOTO}][]
*   installation-description: This is a web-based interpreter for the pedagogical language [PL-{GOTO}][], as described in Brainerd and Landweber's _Theory of Computation_ (1974; ISBN 0471095850), in which it is only possible to express computations which are primitive recursive.
*   installed-implementation: [PL-{GOTO}.NET][]
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/PL-GOTO.NET/eg/examplePrograms.jsonp.js,../modules/PL-GOTO.NET/demo/hastec-launcher.js,../modules/PL-GOTO.NET/demo/PLexceptGOTOdotNET.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "example.pl-g" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/PL-{GOTO})

Technically, it is [PL-{GOTO}.NET][] (written in [Haskell][])
compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Type a PL-{GOTO} program into the text box and click
"Run" to run it.  Here is an [example program](https://git.catseye.tc/PL-GOTO.NET/blob/master/eg/example.pl-g)
you could try pasting in.

You might also want to read
[the description of the PL-{GOTO}.NET compiler](https://catseye.tc/view/PL-GOTO.NET/README.md).

### Quylthulg

*   installation-of: [Quylthulg][]
*   installation-description: This is a web-based interpreter for the esoteric programming language [Quylthulg][].
*   installed-implementation: qlzqqlzuup.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Quylthulg/eg/examplePrograms.jsonp.js,../modules/Quylthulg/demo/qlzqqlzuup-hastec-launcher.js,../modules/Quylthulg/demo/qlzqqlzuup.js
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Quylthulg)

Technically, it is `Qlzqqlzuup.hs` (the reference implementation
of Quylthulg, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Quylthulg programming language](https://catseye.tc/view/Quylthulg/README.md).

### Robin

*   installation-of: [Robin][]
*   installation-description: This is a web-based interpreter for the excessively principled functional programming language [Robin][], version 0.8.
*   installed-implementation: robin.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Robin/eg/examplePrograms.jsonp.js,../modules/Robin/demo/hastec-launcher.js,../modules/Robin/demo/robin.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "fact.robin" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Robin)

Technically, it is `Language.Robin` (the reference implementation
of Robin, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Robin programming language](https://catseye.tc/view/Robin/README.md).

Note that the instrinsics defined by the language are available,
but the standard libraries are not -- if desired, they would need
to be pasted into the textbox above the Robin code that uses them.

### Shelta

*   installation-of: [Shelta][]
*   installation-description: This is a web-based installation of [Shelta][], a programming language with a tiny compiler and a self-hosted compiler.
*   installed-implementation: shelta
*   interactive: true
*   animated: true
*   mediums: [x86 machine code][], [FreeDOS][], [v86][], [HTML5][]
*   v86-floppy-image-url: ../resource/freedos-1.0-shelta-1.2-floppy-2.img
*   online @ [catseye.tc](https://catseye.tc/ix/Shelta)

It is running under [FreeDOS][] running
on a web page via the [HTML5][]-based [IBM PC compatible][]
emulator, [v86][] —  so you can bootstrap it right in your browser.

Instructions:

The system that v86 runs is delivered on a 720K floppy image,
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
[download the disk image](https://catseye.tc/distfiles/freedos-1.0-shelta-1.2-floppy-2.img)
and use it in an emulator such as [QEMU][] or [DOSBox][]
or, wonder of wonders, a real IBM PC compatible — if you can write it onto
a floppy disk somehow...

### Tandem

*   installation-of: [Tandem][]
*   installation-description: This is a web-based interpreter for Tandem, a rewriting language where programs form a Kleene algebra.
*   installed-implementation: tandem.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Tandem/eg/examplePrograms.jsonp.js,../modules/Tandem/demo/hastec-launcher.js,../modules/Tandem/demo/tandem.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "fsa-accept.tandem" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Tandem)

Technically, it is `Language.Tandem` (the reference implementation
of Tandem, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Tandem programming language](https://catseye.tc/view/Tandem/README.md).

### Velo

*   installation-of: [Velo][]
*   installation-description: This is a web-based interpreter for the [Velo][] programming language.
*   installed-implementation: velo.lua
*   interactive: true
*   animated: false
*   mediums: [Lua][], [Fengari][], [Javascript][], [HTML5][]
*   javascript-urls: ../contrib/fengari-web-v0.1.4/fengari-web.js,../modules/velo/eg/examplePrograms.jsonp.js,../modules/velo/impl/velo.lua/demo/velo-fengari-launcher.js
*   lua-urls: ../modules/velo/impl/velo.lua/src/velo.lua
*   launch-command: launch({ container: document.getElementById('installation') });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Velo)

Technically, it is `velo.lua` (an implementation
of Velo in [Lua][]) running under [Fengari][]
(an implementation of the [Lua][] VM in [Javascript][])
running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Velo programming language](https://catseye.tc/view/Velo/README.markdown).

### Wanda

*   installation-of: [Wanda][]
*   installation-description: This is a web-based interpreter for the [Wanda][] programming language.
*   installed-implementation: wanda.lua
*   interactive: true
*   animated: false
*   mediums: [Lua][], [Fengari][], [Javascript][], [HTML5][]
*   javascript-urls: ../contrib/fengari-web-v0.1.4/fengari-web.js,../modules/Wanda/eg/index.js,../modules/Wanda/demo/wanda-fengari-launcher.js
*   lua-urls: ../modules/Wanda/src/wanda.lua
*   launch-command: launch({ container: document.getElementById('installation') });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Wanda)

Technically, it is `wanda.lua` (the reference implementation
of Wanda, in [Lua][]) running under [Fengari][]
(an implementation of the [Lua][] VM in [Javascript][])
running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Wanda programming language](https://catseye.tc/view/Wanda/README.md).

### Wagon

*   installation-of: [Wagon][]
*   installation-description: This is a web-based interpreter for the second-order concatentive programming language [Wagon][].
*   installed-implementation: wagon.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Wagon/eg/examplePrograms.jsonp.js,../modules/Wagon/demo/hastec-launcher.js,../modules/Wagon/demo/wagon.js
*   launch-command: launch({ container: document.getElementById('installation'), initialOption: "reverse0.wagon" });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Wagon)

Technically, it is `Language.Wagon` (the reference implementation
of Wagon, written in [Haskell][]) compiled to [Javascript][]
by the [Haste][] compiler, running in an [HTML5][] document.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the Wagon programming language](https://catseye.tc/view/Wagon/README.md).

### Whothm

*   installation-of: [Whothm][]
*   installation-description: This is a web-based interpreter for the [Whothm][] drawing language.
*   installed-implementation: whothm.lua
*   interactive: true
*   animated: false
*   mediums: [Lua][], [Fengari][], [Javascript][], [HTML5][]
*   javascript-urls: ../contrib/fengari-web-v0.1.4/fengari-web.js,../modules/whothm/eg/examplePrograms.jsonp.js,../modules/whothm/impl/whothm.lua/demo/whothm-fengari-launcher.js
*   lua-urls: ../modules/whothm/impl/whothm.lua/src/whothm.lua
*   launch-command: launch({ container: document.getElementById('installation') });
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/Whothm)

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
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/wierd/dialect/wierd-jnc/impl/wierd-jnc.js/src/wierd-jnc.js
*   launch-command: launch('../modules/wierd/dialect/wierd-jnc/impl/wierd-jnc.js/src/yoob/', 'installation', { 'sourceRoot': '../modules/wierd/dialect/wierd-jnc/eg/' });
*   online @ [catseye.tc](https://catseye.tc/ix/Wierd_(John_Colagioia))

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

### yoob

*   installation-of: [yoob][]
*   installed-implementation: tc.catseye.yoob
*   interactive: true
*   animated: true
*   mediums: Java Web Start, HTML5
*   jnlp-link: https://catseye.tc/applets/yoob_webstart.jnlp
*   jar-url: https://catseye.tc/applets/yoob.jar
*   java-command: java -jar yoob.jar -c tc.catseye.yoob.befunge93.Befunge93State/Befunge93
*   online @ [catseye.tc](https://catseye.tc/ix/yoob)

[yoob][] is a public-domain framework for implementing
[esoteric programming languages][], and allowing them to be
interactively run on programs in a Java application.

Currently, yoob can interpret 21 languages: [1L_AOI][], [1L_a][], [2-ill][], [2L][],
[Ale][], [BackFlip][], [Befunge-93][], [Black][], [brainfuck][], [Circute][], [Etcha][],
[Gemooy][], [LNUSP][], [noit o' mnain worb][], [PATH][], [Qdeql][], [Sceql][],
[SMETANA][], [SNUSP][], [Wunnel][], and [Ypsilax][].  This installation shows yoob in
action, and lets you play with all these esolangs online, using Java Web Start.

### Wunnel

*   installation-of: [Wunnel][]
*   installation-description: This is an HTML5-based implementation of the esoteric programming language [Wunnel][].
*   installed-implementation: wunnel.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Wunnel/impl/wunnel.js/src/wunnel-launcher.js,../modules/Wunnel/eg/index.js
*   script-root: ../modules/Wunnel/impl/wunnel.js/src/
*   style: #installation { text-align: left; margin: 1em; } #display_container { display: flex; } #program_display { display: inline-block; flex: 1 1 auto; } textarea { display: inline-block; flex: 1 1 auto; } #state_display { margin-left: 1em; display: inline-block; flex: 0 1 auto; } #op_table_display { text-align: center; } #tape_display { border: 1px solid black; } #panel_container { display: inline-block; text-align: left; }
*   online @ [catseye.tc](https://catseye.tc/ix/Wunnel)

Instructions:

Select an example program from the drop-down (or click Edit and
compose your own,) then click Run.

When `INP` is highlighted in the instruction matrix, the program is
waiting for input.  Click on the Input text box and input some
`0`s and `1`s (Wunnel programs take bits as input.)  The program
will consume them in order, and continue running.

### ZOWIE

*   installation-of: [ZOWIE][]
*   installation-description: This is a web-based interpreter for the esoteric programming language [ZOWIE][].
*   interactive: true
*   animated: false
*   mediums: [Python][], [Skulpt][], [Javascript][], [HTML5][]
*   javascript-urls: ../contrib/skulpt-0.11.0/skulpt.min.js,../contrib/skulpt-0.11.0/skulpt-stdlib.js,../modules/ZOWIE/eg/examplePrograms.jsonp.js,../modules/ZOWIE/eg/launch-zowie.js
*   script-root: ../modules/ZOWIE/eg/
*   inline-description: right
*   online @ [catseye.tc](https://catseye.tc/ix/ZOWIE)

Technically, it is `zowie.py` (the reference implementation
of ZOWIE, written in [Python][],) running under [Skulpt][]
(a [Python][] interpreter written in [Javascript][])
running in an [HTML5][] document.

Note, input is not yet supported, and errors are not yet handled
in a user-friendly way.

Instructions:

Select an example program from the dropdown box and click
"Run" to run it.  You can also edit the program before
running it.  Or you could clear the textbox and write
an entirely new program there and run it.

You might also want to read
[the description of the ZOWIE programming language](https://catseye.tc/view/ZOWIE/README.md).

### A Minimalist Critique of Tetris

*   installation-of: [A Minimalist Critique of Tetris][]
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/a-minimalist-critique/a-minimalist-critique.js
*   script-root: ../modules/html5-gewgaws/a-minimalist-critique/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 1px solid green }
*   extra-stylesheets: ../stylesheet/mainstage-600x400.css
*   online @ [catseye.tc](https://catseye.tc/ix/A_Minimalist_Critique_of_Tetris)

Instructions:

Just sit back and watch the animation that the computer generates.

### A Non-Random Walk

*   installation-of: [A Non-Random Walk][]
*   installed-implementation: a-non-random-walk.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/a-non-random-walk/a-non-random-walk.js
*   script-root: ../modules/html5-gewgaws/a-non-random-walk/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 1px solid blue }
*   online @ [catseye.tc](https://catseye.tc/ix/A_Non-Random_Walk)

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

On a mobile device, the experience will be better if you zoom out to see
the entire page first.

### Art Restoration Simulator

*   installation-of: [Art Restoration Simulator][]
*   installed-implementation: art-restoration-simulator.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/art-restoration-simulator/art-restoration-simulator.js
*   launch-command: launch('../modules/html5-gewgaws/art-restoration-simulator/yoob/', 'installation', { 'artURL': '../modules/html5-gewgaws/art-restoration-simulator/art.jpg', 'controlPanel': document.getElementById('control_panel') });
*   online @ [catseye.tc](https://catseye.tc/ix/Art_Restoration_Simulator)

Use your mouse (or your finger, on a touch device) to restore the artwork.

On a mobile device, the experience will be better if you zoom out to see
the entire page first.

### Bézier Knots

*   installation-of: [Bézier Knots][]
*   installed-implementation: bezier-knots.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/bezier-knots/bezier-knots.js
*   script-root: ../modules/html5-gewgaws/bezier-knots/yoob/
*   style: #panel-container { display: inline-block; text-align: right; }
*   extra-stylesheets: ../stylesheet/mainstage-600x600.css
*   online @ [catseye.tc](https://catseye.tc/ix/Bézier_Knots)

Changing the number of segments or rings will automatically re-roll the knots.

### Black Hole Poem

*   installation-of: [Black Hole Poem][]
*   installed-implementation: black-hole-poem.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/black-hole-poem/black-hole-poem.js
*   script-root: ../modules/html5-gewgaws/black-hole-poem/yoob/
*   online @ [catseye.tc](https://catseye.tc/ix/Black_Hole_Poem)

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
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/canvas-feedback/demo/canvas-feedback-launcher.js
*   launch-command: launch('../modules/canvas-feedback/src/', 'installation', { imgUrl: 'http://i.imgur.com/SYFLz1X.jpg' });
*   style: #installation > div { display: inline-block; vertical-align: top; } #canvas_container { text-align: center; } #canvas_container canvas { display: block; background: white; border: 1px solid black; } #control_panel > div { background: #c0c0c0; text-align: left; min-width: 30em; } #control_panel > div > div { background: #e0e0e0; padding: 3px; text-align: right; } #control_panel > div > div input { width: auto; }
*   online @ [catseye.tc](https://catseye.tc/ix/Canvas_Feedback)

_Note: on a mobile device, the experience will be better if you zoom out
to see the entire page first._

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
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/circus-xamulus/circus-xamulus.js
*   script-root: ../modules/html5-gewgaws/circus-xamulus/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 2px solid black }
*   extra-stylesheets: ../stylesheet/mainstage-800x400.css
*   online @ [catseye.tc](https://catseye.tc/ix/Circus_Xamulus)

Simply wait, and the rectangle will fill up with randomly-sized circles
(although it will not become entirely full).

### Colourring

*   installation-of: [Colourring][]
*   installed-implementation: colourring.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/colourring/colourring.js
*   script-root: ../modules/html5-gewgaws/colourring/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-800x800.css
*   online @ [catseye.tc](https://catseye.tc/ix/Colourring)

Select a mode from from the MODE dropdown to see the different styles
that are available.  Once you have picked a style, try changing the
numeric parameters.  Not all parameters apply in all styles.  Changing
a parameter will cause a new instance of the ring to be generated.

### Eine kleine Glitchfraktal

*   installation-of: [Eine kleine Glitchfraktal][]
*   installed-implementation: eine-kleine-glitchfraktal.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/eine-kleine-glitchfraktal/eine-kleine-glitchfraktal.js
*   script-root: ../modules/html5-gewgaws/eine-kleine-glitchfraktal/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-500x500.css
*   online @ [catseye.tc](https://catseye.tc/ix/Eine_kleine_Glitchfraktal)

Select a mode from from the MODE dropdown to see different styles
of glitching applied to the rectangles.

### Erratic Turtle Graphics

*   installation-of: [Erratic Turtle Graphics][]
*   installed-implementation: erratic-turtle-graphics-launcher.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Erratic-Turtle-Graphics/src/erratic-turtle.js,../modules/Erratic-Turtle-Graphics/src/erratic-logo.js,../modules/Erratic-Turtle-Graphics/demo/dam-plus-widgets-0.2.min.js,../modules/Erratic-Turtle-Graphics/demo/erratic-turtle-graphics-launcher.js
*   launch-command: launch({ container: document.getElementById('installation') });
*   style: #canvas_viewport { width: 100%; height: 420px; background-color: gainsboro; border: 1px solid blue; overflow: scroll; scroll-behavior: auto; scrollbar-width: auto; scrollbar-color: rgb(23, 38, 182) rgb(162, 170, 238); } textarea { width: 100%; }
*   online @ [catseye.tc](https://catseye.tc/ix/Erratic_Turtle_Graphics)

It's turtle graphics, except there's a small
margin of error.  You might ask for "Turn right 90 degrees"
but you might get only "Turn right 89.91 degrees".

It uses a faint pen, so if you repeat the drawing instructions
many times over, you get a nice pencilly noisy effect.

There is support for a rudimentary command language similar to
Logo, for user-created designs.  The commands are:

    fd NUM             move forward this many pixels
    rt NUM             rotate right this many degrees
    lt NUM             rotate left this many degrees
    setxyr NUM NUM     set the coordinates, as a percentage of the
                       width and height of the canvas
    shiftxyr NUM NUM   adjust the coordinates, as a percentage of the
                       width and height of the canvas
    seterr NUM NUM     set the error rate for rotations and
                       movements respectively
    shifterr NUM NUM   adjust the error rate for rotations and
                       movements respectively

Note that the canvas may be larger than the viewport that it is
displayed in, and that on mobile, the viewport may not display
scrollbars to indicate this.  You can still scroll the canvas.

### Fibonacci Spiral

*   installation-of: [Fibonacci Spiral][]
*   installed-implementation: fibonacci-spiral.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/fibonacci-spiral/fibonacci-spiral.js
*   script-root: ../modules/html5-gewgaws/fibonacci-spiral/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 2px solid black }
*   extra-stylesheets: ../stylesheet/mainstage-1000x500.css
*   online @ [catseye.tc](https://catseye.tc/ix/Fibonacci_Spiral)

The semicircles alternate being on the left and the right.  The first
two terms of the Fibonacci sequence are `1, 1` and these make up the unit
circle in the center of the spiral.

The animation is simply a zooming out and back in on the spiral.

### Fingerspelling

*   installation-of: [Fingerspelling][]
*   installed-implementation: fingerspelling.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/fingerspelling/fingerspelling.js
*   script-root: ../modules/html5-gewgaws/fingerspelling/yoob/
*   style: body { margin: 0; } article { margin: 0; } #canvas { background: #ccaacc; border: none; } #canvas_container { margin: 0; text-align: inherit; } #about_panel p { line-height: 1.5em; }
*   viewport: initial-scale=1, user-scalable=no
*   online @ [catseye.tc](https://catseye.tc/ix/Fingerspelling)

If you have a touchscreen, prod the lavender area of the screen with your
finger.  If you don't have a touchscreen, you may simulate this action
with your mouse pointer.

### Heronsis hermnonicii

*   installation-of: [Heronsis hermnonicii][]
*   installed-implementation: heronsis-hermnonicii.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/heronsis-hermnonicii/heronsis-hermnonicii.js
*   script-root: ../modules/html5-gewgaws/heronsis-hermnonicii/yoob/
*   online @ [catseye.tc](https://catseye.tc/ix/Heronsis_hermnonicii)

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
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/hirsute-miasma/hirsute-miasma.js
*   script-root: ../modules/html5-gewgaws/hirsute-miasma/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 2px solid black }
*   extra-stylesheets: ../stylesheet/mainstage-400x400.css
*   online @ [catseye.tc](https://catseye.tc/ix/Hirsute_Miasma)

The animation will eventually cycle if you're patient (although it won't
of course cycle exactly, as there is a random element.)  You may enable
the "terminal" option to prevent this cycling.

### Hypongtrochoid

*   installation-of: [Hypongtrochoid][]
*   installed-implementation: hypongtrochoid.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/hypongtrochoid/hypongtrochoid.js
*   script-root: ../modules/html5-gewgaws/hypongtrochoid/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 1px solid blue }
*   extra-stylesheets: ../stylesheet/mainstage-600x400.css
*   online @ [catseye.tc](https://catseye.tc/ix/Hypongtrochoid)

Each box moves with a constant velocity
relative to the box it is contained in, and bounces around inside it in a
simple fashion.  Yet the path traced out by the innermost box is not very
simple at all.

### Kolakoski Kurve

*   installation-of: [Kolakoski Kurve][]
*   installed-implementation: kolakoski-kurve.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/Kolakoski-Kurve/src/kolakoski-kurve.js,../modules/Kolakoski-Kurve/demo/dam-plus-widgets-0.2.min.js,../modules/Kolakoski-Kurve/demo/kolakoski-kurve-launcher.js
*   launch-command: launch({ container: document.getElementById('installation') });
*   style: #installation canvas { background-color: #ffffff; border: 1px solid blue }
*   extra-stylesheets: ../stylesheet/mainstage-800x400.css
*   online @ [catseye.tc](https://catseye.tc/ix/Kolakoski_Kurve)

The segment length can be changed while a curve is being drawn.
Changing the draw mode will reset the drawing.
Changing the start or end of a curve while it is being drawn
might result in glitching in XOR mode (depending on your browser's
implementation of the HTML5 canvas -- I don't really know why this
happens.)

### Latcarf

*   installation-of: [Latcarf][]
*   installed-implementation: latcarf.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/latcarf/src/latcarf.js,../modules/latcarf/demo/dam-plus-widgets-web.js,../modules/latcarf/demo/latcarf-launcher.js
*   launch-command: launch({ container: document.getElementById('installation') });
*   extra-stylesheets: ../stylesheet/mainstage-800x600.css
*   online @ [catseye.tc](https://catseye.tc/ix/Latcarf)

Most recursive fractals are created top-down: start with a big thing, add some smaller things to it,
add some even smaller things to those things, etc.

I was curious about what it would be like if a fractal was generated bottom-up: start with many small
things, connect them to larger things, then connect those to even larger things, etc.

This is the result of implementing that method.

### Lexeduct

*   installation-of: [Lexeduct][]
*   installed-implementation: lexeduct-browser.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/lexeduct/demo/launch-lexeduct.js
*   script-root: ../modules/lexeduct/demo/
*   style: textarea { width: 30%; } #container { text-align: center; }
*   online @ [catseye.tc](https://catseye.tc/ix/Lexeduct)

By default it is in "live mode", meaning, whenever you change the text in
the left-side textbox, or whenever you change one of the filters, the
text in the right-side textbox will automatically be updated with the
new input text and settings.

When you select a filter, inputs will appear below it allowing you to
configure it.  Several filters need to know the set of characters that
they should operate on, for example.

### Markov Font

*   installation-of: [Markov Font][]
*   installed-implementation: markov-font.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/markov-font/markov-font.js
*   launch-command: launch('../modules/html5-gewgaws/markov-font/yoob/', 'installation', { imgUrl: "../resource/c64_noninverted.png" });
*   style: canvas { width: 18px; height: 18px; } #charset { width: 512px; height: 128px; margin: 10px } #installation { background: #808080; }
*   online @ [catseye.tc](https://catseye.tc/ix/Markov_Font)

Wait a few seconds while it analyzes the characters in the C64 character set.
Then it will generate some of its own.

### Maze Clouds

*   installation-of: [Maze Clouds][]
*   installed-implementation: maze-clouds.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [SVG][], [HTML5][]
*   javascript-urls: ../modules/maze-clouds/src/maze-clouds.js,../modules/maze-clouds/demo/dam-plus-widgets-web.js,../modules/maze-clouds/demo/maze-clouds-svg-launcher.js
*   launch-command: launch({ container: document.getElementById('installation') });
*   style: #installation svg { display: inline-block; height: 600px; width: 600px; }
*   extra-stylesheets: ../stylesheet/mainstage-600x600.css
*   online @ [catseye.tc](https://catseye.tc/ix/Maze_Clouds)

It implements a simple generative technique to generate mazy, cloudy forms.

Instructions:

The "Re-roll" button will cause a new maze cloud to be generated.  The other
controls will only affect the appearance of the current maze cloud.

### Multicolouralism

*   installation-of: [Multicolouralism][]
*   installed-implementation: multicolouralism.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/multicolouralism/multicolouralism.js
*   script-root: ../modules/html5-gewgaws/multicolouralism/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-400x400.css
*   online @ [catseye.tc](https://catseye.tc/ix/Multicolouralism)

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
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/noise-to-signal-1/noise-to-signal-1.js
*   script-root: ../modules/html5-gewgaws/noise-to-signal-1/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 1px solid black }
*   extra-stylesheets: ../stylesheet/mainstage-600x200.css
*   online @ [catseye.tc](https://catseye.tc/ix/Noise_to_Signal_No._1)

The two panels are constructed by randomly distributing the pixels from
a source image randomly onto either panel.

### Pixed-Point

*   installation-of: [Pixed-Point][]
*   installed-implementation: pixed-point.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/pixed-point/pixed-point.js
*   launch-command: launch('../modules/html5-gewgaws/pixed-point/yoob/', 'installation', { imgUrl: "../resource/c64_upp.gif" });
*   style: #installation canvas { display: inline-block; margin: 2em; } #installation div { display: inline-block; text-align: right; }
*   online @ [catseye.tc](https://catseye.tc/ix/Pixed-Point)

As you adjust the parameters, the computer will attempt to make
the displayed image self-describing.

There are some combinations where the numbers will "settle down",
but there's no guarantee, you see.

### Prairie

*   installation-of: [Prairie][]
*   installed-implementation: prairie.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/prairie/prairie.js
*   launch-command: launch('../modules/html5-gewgaws/prairie/yoob/', 'installation', { imgURL: '../modules/html5-gewgaws/prairie/Elevator_1_(PSF).png' });
*   style: #installation canvas { background-color: #ffffff; border: 1px solid blue }
*   extra-stylesheets: ../stylesheet/mainstage-640x390.css
*   online @ [catseye.tc](https://catseye.tc/ix/Prairie)

Instructions:

Just sit back and watch the animation that the computer generates.  It will
continue indefinitely.

### Progression

*   installation-of: [Progression][]
*   installed-implementation: progression.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/progression/progression.js
*   script-root: ../modules/html5-gewgaws/progression/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 1px solid black }
*   extra-stylesheets: ../stylesheet/mainstage-800x200.css
*   online @ [catseye.tc](https://catseye.tc/ix/Progression)

Instructions:

Just sit back and watch the animation that the computer generates.  It will
eventually become a static form, but it will take a long time to do so.

### Radialjective

*   installation-of: [Radialjective][]
*   installed-implementation: radialjective.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/radialjective/radialjective.js
*   script-root: ../modules/html5-gewgaws/radialjective/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-500x500.css
*   online @ [catseye.tc](https://catseye.tc/ix/Radialjective)

Instructions:

Just sit back and watch the animation that the computer generates.  It will
continue indefinitely.

### Rigamaroads

*   installation-of: [Rigamaroads][]
*   installed-implementation: rigamaroads.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/rigamaroads/rigamaroads.js
*   script-root: ../modules/html5-gewgaws/rigamaroads/yoob/
*   style: #installation canvas { background-color: black; }
*   extra-stylesheets: ../stylesheet/mainstage-800x800.css
*   online @ [catseye.tc](https://catseye.tc/ix/Rigamaroads)

Instructions:

Just sit back and watch as the computer generates the form.  It will stop when
it is finished.

### Semicircle Jam

*   installation-of: [Semicircle Jam][]
*   installed-implementation: semicircle-jam.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/semicircle-jam/semicircle-jam.js
*   script-root: ../modules/html5-gewgaws/semicircle-jam/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-600x600.css
*   online @ [catseye.tc](https://catseye.tc/ix/Semicircle_Jam)

Instructions:

Just sit back and watch as the computer generates the form.  It will stop when
it is finished.

### Spadgets

*   installation-of: [Spadgets][]
*   installed-implementation: spadgets.js
*   interactive: false
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/spadgets/spadgets.js
*   script-root: ../modules/html5-gewgaws/spadgets/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-800x600.css
*   online @ [catseye.tc](https://catseye.tc/ix/Spadgets)

Instructions:

Just sit back and watch as the computer generates the form.  (It is nearly
instantaneous.)  It will stop when it is finished.

### Tentacles, Undamped

*   installation-of: [Tentacles, Undamped][]
*   installed-implementation: tentacles-undamped.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/tentacles-undamped/tentacles-undamped.js
*   script-root: ../modules/html5-gewgaws/tentacles-undamped/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-500x500.css
*   online @ [catseye.tc](https://catseye.tc/ix/Tentacles,_Undamped)

Instructions:

Just sit back and watch the animation that the computer generates.  It will
continue indefinitely.

### Text Uniquifier

*   installation-of: [Text Uniquifier][]
*   installed-implementation: text-uniquifier.js
*   interactive: true
*   animated: false
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/text-uniquifier/text-uniquifier.js
*   script-root: ../modules/html5-gewgaws/text-uniquifier/yoob/
*   online @ [catseye.tc](https://catseye.tc/ix/Text_Uniquifier)

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
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/the-frame/the-frame.js
*   launch-command: launch('../modules/html5-gewgaws/the-frame/yoob/', 'installation', { imgURL: '../modules/html5-gewgaws/the-frame/the-frame.png' });
*   online @ [catseye.tc](https://catseye.tc/ix/The_Frame)

Note 1. Green things can be dragged.  
Note 2. Due to technical limitations, things cannot be dragged off
of the computer screen.

### The Judgment of Paris

*   installation-of: [The Judgment of Paris][]
*   installed-implementation: the-judgment-of-paris.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/the-judgment-of-paris/the-judgment-of-paris.js
*   script-root: ../modules/html5-gewgaws/the-judgment-of-paris/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-500x500.css
*   online @ [catseye.tc](https://catseye.tc/ix/The_Judgment_of_Paris)

Instructions:

Just sit back and watch the animation that the computer generates.  It will
continue indefinitely.

### Two Fifty Six

*   installation-of: [Two Fifty Six][]
*   installed-implementation: two-fifty-six.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/two-fifty-six/two-fifty-six.js
*   script-root: ../modules/html5-gewgaws/two-fifty-six/yoob/
*   online @ [catseye.tc](https://catseye.tc/ix/Two_Fifty_Six)

Try adjusting the Speed, Variety, and Noise settings to affect how the
gewgaw is displayed.  Varieties that are powers of two (2, 4, 8, 16...)
look more orderly than ones that aren't.  The palette can also be
changed.

### Uncle Ankur

*   installation-of: [Uncle Ankur][]
*   installed-implementation: uncle-ankur.js
*   interactive: false
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/uncle-ankur/uncle-ankur.js
*   script-root: ../modules/html5-gewgaws/uncle-ankur/yoob/
*   extra-stylesheets: ../stylesheet/mainstage-500x500.css
*   online @ [catseye.tc](https://catseye.tc/ix/Uncle_Ankur)

Instructions:

Just sit back and watch the animation that the computer generates.  It will
continue indefinitely.

### Woman on Film

*   installation-of: [Woman on Film][]
*   installed-implementation: woman-on-film.js
*   interactive: true
*   animated: true
*   mediums: [Javascript][], [HTML5][]
*   javascript-urls: ../modules/html5-gewgaws/woman-on-film/woman-on-film.js
*   script-root: ../modules/html5-gewgaws/woman-on-film/yoob/
*   style: #installation canvas { background-color: #ffffff; border: 1px solid black }
*   online @ [catseye.tc](https://catseye.tc/ix/Woman_on_Film)

Use the navigation buttons to traverse the space of the work.

On a mobile device, the experience will be better if you zoom out to see
the entire page first.

- - - -

[Cat's Eye Technologies]: ../article/General%20Information.md#cats-eye-technologies
[esoteric programming language]: ../article/General%20Information.md#esolang
[esoteric programming languages]: ../article/General%20Information.md#esolang
[languages]: ../article/Languages.md
[automata]: ../article/Automata.md
[games]: ../article/Games.md
[gewgaws]: ../article/Gewgaws.md
[platforms]: ../article/Platforms.md
[JaC64]: ../article/Forks.md#jac64
[Zplet]: ../article/Forks.md#zplet
[Z-Machine code]: ../article/Project%20Dependencies.md#z-machine
[Javascript]: ../article/Project%20Dependencies.md#javascript
[Web Workers]: https://en.wikipedia.org/wiki/Web_worker
[6502 machine code]: ../article/Project%20Dependencies.md#6502
[x86 machine code]: ../article/Project%20Dependencies.md#ibm-pc-compatible
[v86]: ../article/Project%20Dependencies.md#ibm-pc-compatible
[Fengari]: https://fengari.io/
[Java Web Start]: http://docs.oracle.com/javase/8/docs/technotes/guides/javaws/
[Haskell]: ../article/Project%20Dependencies.md#haskell
[HTML5]: https://www.w3.org/TR/html5/
[Lua]: ../article/Project%20Dependencies.md#lua
[Python]: ../article/Project%20Dependencies.md#python
[Skulpt]: http://www.skulpt.org/
[PixiJS]: http://pixijs.com/
[SVG]: https://www.w3.org/Graphics/SVG/
[Nam June Paik]: https://en.wikipedia.org/wiki/Nam_June_Paik
[Bubble Escape 2K]: ../article/Games.md#bubble-escape
[Cosmos Boulders]: ../article/Games.md#cosmos-boulders
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
[1L_AOI]: https://esolangs.org/wiki/1L_AOI
[1L_a]: https://esolangs.org/wiki/1L_a
[2-ill]: https://esolangs.org/wiki/2-ill
[2L]: https://esolangs.org/wiki/2L
[ALPACA]: ../article/Languages.md#alpaca
[Ale]: https://esolangs.org/wiki/Ale
[BackFlip]: https://esolangs.org/wiki/BackFlip
[Befunge-93]: ../article/Languages.md#befunge-93
[Black]: https://esolangs.org/wiki/Black
[Braktif]: ../article/Automata.md#braktif
[Carriage]: ../article/Languages.md#carriage
[Circute]: ../article/Automata.md#circute
[Cyclobots]: ../article/Automata.md#cyclobots
[DOSBox]: ../article/Project%20Dependencies.md#ms-dos
[Emmental]: ../article/Languages.md#emmental
[Equipage]: ../article/Languages.md#equipage
[Etcha]: ../article/Languages.md#etcha
[Flobnar]: ../article/Languages.md#flobnar
[FreeDOS]: ../article/Project%20Dependencies.md#ms-dos
[Haste]: https://haste-lang.org/
[IBM PC compatible]: ../article/Project%20Dependencies.md#ibm-pc-compatible
[ILLGOL]: ../article/Languages.md#illgol
[Jaccia]: ../article/Automata.md#jaccia
[Jacciata]: ../article/Automata.md#jacciata
[LNUSP]: https://esolangs.org/wiki/LNUSP
[Mascarpone]: ../article/Languages.md#mascarpone
[Oxcart]: ../article/Languages.md#oxcart
[Pail]: ../article/Languages.md#pail
[PATH]: https://esolangs.org/wiki/PATH
[PL-{GOTO}]: http://www.worldcat.org/title/theory-of-computation/oclc/694056
[PL-{GOTO}.NET]: ../article/Language%20Implementations.md#pl-gotonet
[Robin]: ../article/Languages.md#robin
[QEMU]: ../article/Project%20Dependencies.md#ibm-pc-compatible
[Qdeql]: https://esolangs.org/wiki/Qdeql
[Quylthulg]: ../article/Languages.md#quylthulg
[REDGREEN]: ../article/Automata.md#redgreen
[SMETANA]: ../article/Automata.md#smetana
[SNUSP]: https://esolangs.org/wiki/SNUSP
[Sceql]: https://esolangs.org/wiki/Sceql
[Shelta]: ../article/Languages.md#shelta
[Velo]: ../article/Languages.md#velo
[Wanda]: ../article/Languages.md#wanda
[Wagon]: ../article/Languages.md#wagon
[Whothm]: ../article/Languages.md#whothm
[Wunnel]: ../article/Languages.md#wunnel
[Ypsilax]: ../article/Languages.md#ypsilax
[brainfuck]: https://esolangs.org/wiki/brainfuck
[noit o' mnain worb]: ../article/Automata.md#noit-o-mnain-worb
[yoob]: ../article/Archived.md#yoob
[Schrödinger's Game of Life]: ../article/Automata.md#schr%C3%B6dingers-game-of-life
[Matchbox]: ../article/Languages.md#matchbox
[Wierd (John Colagioia)]: ../article/Languages.md#wierd
[A Minimalist Critique of Tetris]: ../article/Gewgaws.md#a-minimalist-critique-of-tetris
[A Non-Random Walk]: ../article/Gewgaws.md#a-non-random-walk
[Art Restoration Simulator]: ../article/Gewgaws.md#art-restoration-simulator
[Bézier Knots]: ../article/Gewgaws.md#b%C3%A9zier-knots
[Black Hole Poem]: ../article/Gewgaws.md#black-hole-poem
[Canvas Feedback]: ../article/Gewgaws.md#canvas-feedback
[Circus Xamulus]: ../article/Gewgaws.md#circus-xamulus
[Colourring]: ../article/Gewgaws.md#colourring
[Eine kleine Glitchfraktal]: ../article/Gewgaws.md#eine-kleine-glitchfraktal
[Erratic Turtle Graphics]: ../article/Gewgaws.md#erratic-turtle-graphics
[Fibonacci Spiral]: ../article/Gewgaws.md#fibonacci-spiral
[Fingerspelling]: ../article/Gewgaws.md#fingerspelling
[Heronsis hermnonicii]: ../article/Gewgaws.md#heronsis-hermnonicii
[Hirsute Miasma]: ../article/Gewgaws.md#hirsute-miasma
[Hypongtrochoid]: ../article/Gewgaws.md#hypongtrochoid
[Kolakoski Kurve]: ../article/Gewgaws.md#kolakoski-kurve
[Latcarf]: ../article/Gewgaws.md#latcarf
[Lexeduct]: ../article/Gewgaws.md#lexeduct
[Markov Font]: ../article/Gewgaws.md#markov-font
[Maze Clouds]: ../article/Gewgaws.md#maze-clouds
[Multicolouralism]: ../article/Gewgaws.md#multicolouralism
[Noise to Signal No. 1]: ../article/Gewgaws.md#noise-to-signal-no-1
[Pixed-Point]: ../article/Gewgaws.md#pixed-point
[Rigamaroads]: ../article/Gewgaws.md#rigamaroads
[Semicircle Jam]: ../article/Gewgaws.md#semicircle-jam
[Prairie]: ../article/Gewgaws.md#prairie
[Progression]: ../article/Gewgaws.md#progression
[Radialjective]: ../article/Gewgaws.md#radialjective
[Spadgets]: ../article/Gewgaws.md#spadgets
[Tentacles, Undamped]: ../article/Gewgaws.md#tentacles-undamped
[Text Uniquifier]: ../article/Gewgaws.md#text-uniquifier
[The Frame]: ../article/Gewgaws.md#the-frame
[The Judgment of Paris]: ../article/Gewgaws.md#the-judgment-of-paris
[Two Fifty Six]: ../article/Gewgaws.md#two-fifty-six
[Uncle Ankur]: ../article/Gewgaws.md#uncle-ankur
[Woman on Film]: ../article/Gewgaws.md#woman-on-film

