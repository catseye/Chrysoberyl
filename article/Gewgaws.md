Gewgaws
=======

*   common reference implementation license: Public Domain
*   common reference implementation language: Javascript
*   common reference implementation platform: HTML5

Gewgaws.

### A Minimalist Critique of Tetris

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: Mar 2015
*   reference implementation name: a-minimalist-critique.js
*   online @ [catseye.tc](http://catseye.tc/installation/A Minimalist Critique of Tetris)

A minimalist critique of Tetris.

### A Non-Random Walk

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: a-non-random-walk.js
*   online @ [catseye.tc](http://catseye.tc/installation/A Non-Random Walk)

This is an animated version of the "non-random walk" on p. 72 of
_Mathematical Circus_ by Martin Gardner.

Instructions:

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

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: May 2013
*   reference implementation name: art-restoration-simulator.js
*   online @ [catseye.tc](http://catseye.tc/installation/Art Restoration Simulator)

A simulator that lets you experience the thrills and spills
of the fascinating world of art restoration.

Instructions:

Use your mouse (or your finger, on a touch device) to restore the artwork.

### Black Hole Poem

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: Jan 2015
*   reference implementation name: black-hole-poem.js
*   online @ [catseye.tc](http://catseye.tc/installation/Black Hole Poem)

An interactive concrete poem about black holes.

Instructions:

Darker-beige squares can be dragged with your mouse or your finger
(for what good it will do you.)

(Yes, you can't see the whole poem.  Yes, that's the point.
Yes, unless you look at the Javascript source.  Yes, that's the point too.)

The background colour is beige because it's based on
[Illuminant E](https://en.wikipedia.org/wiki/Standard_illuminant#Illuminant_E)
because that is our best guess at
[what colour the universe is](http://www.pha.jhu.edu/~kgb/cosspec/).

### Canvas Feedback

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: canvas-feedback.js
*   reference implementation license: MIT license
*   online @ [catseye.tc](http://catseye.tc/installation/Canvas Feedback)

An application of an analogue-video-like feedback effect to an [HTML5][]
canvas element, with in-browser controls by which the feedback properties
can be adjusted.  For some background and an explanation
of how it works, see
[its README document](https://github.com/catseye/Canvas-Feedback/).

*   implementation name: Canvas Feedback 1K
*   implementation license: MIT license

Instructions:

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

### Background

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

### Chzrxl

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: chzrxl.js
*   online @ [catseye.tc](http://catseye.tc/installation/Chzrxl)

"Chzrxl, the Living Inkblot."  Or is it a sort of self-attracting
lava lamp?

Instructions:

The original idea was this: each ball travels on a
sine-wave path (kind of like a spring) between a randomly-chosen
pair of two other balls.

It was soon discovered that if all balls are free to move like this,
they all quickly collapse to a single point.  Thus, some number of
balls are held fixed (5% by default).  The result is a slightly
organic-seeming emergent motion.

### Circus Xamulus

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: circus-xamulus.js
*   online @ [catseye.tc](http://catseye.tc/installation/Circus Xamulus)

A circle-based time-lapse space-filler.

### Cyclobots

*   reference distribution: [???](/distribution/???)
*   inception date: ca 1994
*   reference implementation name: cyclobots.js
*   reference implementation license: Freely Redistributable
*   online @ [catseye.tc](http://catseye.tc/installation/Cyclobots)

Cyclobots is an automaton that consists of a number of little virtual
"turtle robots" called "cyclobots".  Each cyclobot moves with a constant
velocity, and tries to follow exactly one other cyclobot, adjusting
its heading to point towards the cyclobot it is following.
No cylobot is followed by more than one cyclobot.

A group of cyclobots tends to fall into one of several semi-stable
patterns.  The simplest of these is just a rotating circle, but
more complex, [trefoil](http://en.wikipedia.org/wiki/Trefoil_knot)-like
patterns are more common.

*   implementation name: Cyclobots (Visual Basic)
*   implementation license: Freely Redistributable
*   implementation language: Visual Basic
*   implementation platform: Windows 3.1

I originally conceived of this automaton, calling it
an "interactive desktop toy", in or around 1994, and implemented
it immediately in Visual Basic.  I remember the year because I wrote the
first implementation of [SMETANA][] in Visual Basic at about the same time.

The original implementation had a few features which are not present (yet)
in the HTML5 version: cyclobots could collide with each other, and the user
could use the mouse to attract/repel them from a chosen point.

### Eine kleine Glitchfraktal

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: eine-kleine-glitchfraktal.js
*   online @ [catseye.tc](http://catseye.tc/installation/Eine kleine Glitchfraktal)

A simple fractal (each rectangle contains four smaller rectangles)
with colour variance and configurable glitching.

Instructions:

Select a mode from from the MODE dropdown to see different styles
of glitching applied to the rectangles.

### Fibonacci Spiral

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: fibonacci-spiral.js
*   online @ [catseye.tc](http://catseye.tc/installation/Fibonacci Spiral)

A spiral made up of semicircles with proportions in the Fibonacci sequence.

Instructions:

The semicircles alternate being on the left and the right.  The first
two terms of the Fibonacci sequence are `1, 1` and these make up the unit
circle in the center of the spiral.

The animation is simply a zooming out and back in on the spiral.

### Fingerspelling

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: fingerspelling.js
*   online @ [catseye.tc](http://catseye.tc/installation/Fingerspelling)

A simple interactive entertainment, intended to be experienced
on a touchscreen device.

This is most certainly a gewgaw.  It should provide you about
20 seconds of entertainment, give or take.

Instructions:

If you have a touchscreen, prod the lavender area of the screen with your
finger.  If you don't have a touchscreen, you may simulate this action
with your mouse pointer.

### Heronsis hermnonicii

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: heronsis-hermnonicii.js
*   online @ [catseye.tc](http://catseye.tc/installation/Heronsis hermnonicii)

An animated "plate" depicting a proto-cohort of *Heronsis hermnonicii*.

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

Instructions:

It is primarily meant to just be watched, but you may find it entertaining
to try clicking on the entities.

### Hirsute Miasma

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: hirsute-miasma.js
*   online @ [catseye.tc](http://catseye.tc/installation/Hirsute Miasma)

Your web browser is burdened by the sins of its ancestors
and their shower drains.

Instructions:

The animation will eventually cycle if you're patient (although it won't
of course cycle exactly, as there is a random element.)  You may enable
the "terminal" option to prevent this cycling.

### Hypongtrochoid

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: hypongtrochoid.js
*   online @ [catseye.tc](http://catseye.tc/installation/Hypongtrochoid)

"Hypongtrochoid" is a portmanteau of
[hypotrochoid](http://en.wikipedia.org/wiki/Hypotrochoid)
(as popularized by [Spirograph](http://en.wikipedia.org/wiki/Spirograph))
and [Pong](http://en.wikipedia.org/wiki/Pong)
(as popularized by, well, Pong.)

Instructions:

Each box moves with a constant velocity
relative to the box it is contained in, and bounces around inside it in a
simple fashion.  Yet the path traced out by the innermost box is not very
simple at all.

### Lexeduct

*   reference distribution: [Lexeduct distribution](/distribution/Lexeduct distribution)
*   inception date: Apr 2015
*   reference implementation name: lexeduct-browser.js
*   online @ [catseye.tc](http://catseye.tc/installation/Lexeduct)

A "livetextmangler" — an online tool which transforms text.  As you
select different filters to apply to the input, the output is updated in
real-time.  Can also be used on the command-line.

### Markov Font

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: Apr 2016
*   reference implementation name: markov-font.js
*   online @ [catseye.tc](http://catseye.tc/installation/Markov Font)

Uses a 2D Markov chain to generate new glyphs from a character set.

### Multicolouralism

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: multicolouralism.js
*   online @ [catseye.tc](http://catseye.tc/installation/Multicolouralism)

Animated op art: an interactive bleeding of colours.

Instructions:

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

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: Apr 2015
*   reference implementation name: noise-to-signal-1.js
*   online @ [catseye.tc](http://catseye.tc/installation/Noise to Signal No. 1)

A generated animation involving randomness and not-so-much randomness.

Instructions:

The two panels are constructed by randomly distributing the pixels from
a source image randomly onto either panel.

### Prairie

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2012
*   reference implementation name: prairie.js
*   online @ [catseye.tc](http://catseye.tc/installation/Prairie)

An animated impressionistic depiction of the prairies.

I composed this while still in Winnipeg and still
learning about the capabilities of `<canvas>` — something about the
wind and the wheat...  The background is a public-domain drawing
of a grain elevator taken from Wikimedia.

### Progression

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2012
*   reference implementation name: progression.js
*   online @ [catseye.tc](http://catseye.tc/installation/Progression)

Animated op-art exhibiting a [moiré](http://en.wikipedia.org/wiki/Moir%C3%A9_pattern) effect.

A real eye-tickler.  This was one of the first bits of `<canvas>` code I
ever wrote; I essentially wrote it by accident — it wasn't quite what I
meant, but I liked it, and kept it.  For me, in Firefox, it starts getting
interesting around 100 iterations, and starts stopping being interesting
around 1550.  In Chromium, you can still see some activity at about 2000
iterations, but it's very faint thereafter.

### Radialjective

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: radialjective.js
*   online @ [catseye.tc](http://catseye.tc/installation/Radialjective)

An animated mathematical function, depicted in four different ways.

### Tentacles, Undamped

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: ca Feb 2014
*   reference implementation name: tentacles-undamped.js
*   online @ [catseye.tc](http://catseye.tc/installation/Tentacles, Undamped)

A simulation of undulating tentacles.  It starts off alright, but
soon starts doing things real tentacles never do, because they have
damping.

### Text Uniquifier

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: Nov 2014
*   reference implementation name: text-uniquifier.js
*   online @ [catseye.tc](http://catseye.tc/installation/Text Uniquifier)

An online tool/amusement where you paste in some text and it displays
the text with repeated words removed.

Instructions:

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

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2012
*   reference implementation name: the-frame.js
*   online @ [catseye.tc](http://catseye.tc/installation/The Frame)

An interactive exploration of the concept of The Frame in art,
based on **words** and **'do** by [Frank Zappa][].

This piece was conceived and begun in late summer or early autumn of 2012,
in Winnipeg, and finished up and released from Cornwall in spring of
2013.

Instructions:

Note 1. Green things can be dragged.  
Note 2. Due to technical limitations, things cannot be dragged off
of the computer screen.

### The Judgment of Paris

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2014
*   reference implementation name: the-judgment-of-paris.js
*   online @ [catseye.tc](http://catseye.tc/installation/The Judgment of Paris)

A slight reworking of a well-known
[Greek myth](https://en.wikipedia.org/wiki/Judgement_of_Paris).

### Two Fifty Six

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: May 2015
*   reference implementation name: two-fifty-six.js
*   online @ [catseye.tc](http://catseye.tc/installation/Two Fifty Six)

A graphical depiction of the first two hundred and fifty-six natural
numbers, in base four, using coloured squares with potentially varying
assignments of colours to digits.

### Uncle Ankur

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: 2013
*   reference implementation name: uncle-ankur.js
*   online @ [catseye.tc](http://catseye.tc/installation/Uncle Ankur)

An experimental animation employing gradients and
randomly-constructed transformation matrices.

### Woman on Film

*   reference distribution: [HTML5 Gewgaws distribution](/distribution/HTML5 Gewgaws distribution)
*   inception date: ca Apr 2013
*   reference implementation name: woman-on-film.js
*   online @ [catseye.tc](http://catseye.tc/installation/Woman on Film)

An interactive, navigable, animated thing based on several tracings of
a still from a film.

Instructions:

Use the navigation buttons to traverse the space of the work.

- - - -

[Frank Zappa]: https://en.wikipedia.org/wiki/Frank_Zappa
[HTML5]: https://www.w3.org/TR/html5/
[Nam June Paik]: https://en.wikipedia.org/wiki/Nam_June_Paik
[SMETANA]: http://catseye.tc/article/Languages.md#smetana
