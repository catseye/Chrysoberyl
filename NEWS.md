# Cat's Eye Technologies: New Developments

*   author: Chris Pressey
*   url: http://catseye.tc/news.xml

### Dropped support for Mercurial repos on Bitbucket

*   summary: Dropped support for our mirror repos on [Bitbucket](https://bitbucket.org/catseye/).
*   date: Fri, 05 Aug 2016 19:26:11 GMT

I like [Mercurial](https://www.mercurial-scm.org/).  It was the first DVCS I learned to use, and I've
always found it easier to use than [git](https://git-scm.com/).  I like [Bitbucket](https://bitbucket.org/)
too, largely because they'll give you private repositories for no charge, if you're a small team.  I like that.

In fact, I like both of them enough to have gone to the trouble of keeping all of Cat's Eye Technologies'
distributions mirrored in both git repositories on [GitHub](https://github.com/catseye/) and Mercurial repositories
on Bitbucket.

But alas, this has become far too much trouble in the upkeep, mainly because
[hg-git](https://bitbucket.org/durin42/hg-git/) no longer works reliably for me.  (You can see the
[fascinating bug report](https://bitbucket.org/durin42/hg-git/issues/181/git-mapfile-is-sometimes-completely)
if you would like more details.)  Even when it does work, it's yet another step I need to remember to take, and
Mercurial doesn't work entirely reliably on my web server either now, etc., and basically I have better things
to do with my time than hassle with this.

So, if you were using this Mercurial repositories on Bitbucket and are inconvenienced that you now must
use Git repositories on GitHub instead, I apologize, but by all accounts you are in the distinct minority.

As for this news feed, I've been lax in updating it, and yes, I apologize for that too.  I will try to post
a catch-up update sometime in the near future.

### RetroChallenge July 2015, and other updates

*   summary: RetroChallenge 2015/07, and other updates.
*   date: Tue, 30 Jun 2015 17:13:24 GMT

We've decided to enter [RetroChallenge 2015/07](http://www.wickensonline.co.uk/retrochallenge-2012sc/).
We're going to write some code... *by hand!*  To this end, we've started a blog to track
our progress, and have [already made a few posts](http://bootstrap-zero.tumblr.com/archive),
even though it's not July yet.

Also, some new things done with the site since the last update:

*   Documentation for all of our projects is now hosted on this website.

    It's still on Github too, but the documents on `catseye.tc` are nicely marked up
    and should be searchable by the search box on the main page (via duckduckgo.com).
    
*   [Text](http://catseye.tc/node/Text)s are hosted on this website, too.

*   Some new [Gewgaw](http://catseye.tc/node/Gewgaw)s are now installed online here:
    *   [Art Restoration Simulator](http://catseye.tc/installation/Art%20Restoration%20Simulator)
    *   [Two Fifty Six](http://catseye.tc/installation/Two%20Fifty%20Six)

*   [Lexeduct](http://catseye.tc/node/Lexeduct), a result of NaPoGenMo 2015, is installed online — but not here.
    It's on [catseye.github.io](http://catseye.github.io/Lexeduct/).
    So [go there and try it out](http://catseye.github.io/Lexeduct/in-browser/).
    (It will be hosted on `catseye.tc` too... someday.)

### Interview with Chris Pressey, by Daniel Temkin

*   summary: [Interview on esoteric.codes](http://esoteric.codes/post/118780138572/interview-with-chris-pressey).
*   date: Thu, 28 May 2015 20:46:13 GMT

A little while ago I was [interviewed by Daniel Temkin](http://esoteric.codes/post/118780138572/interview-with-chris-pressey)
on the subject of [Esolang](http://catseye.tc/node/Esolang).

Since that's something I've been doing for ages, it goes into a lot of
history, including pre-Internet stuff like BBS'es and the
[Amiga](http://catseye.tc/node/Amiga%20500) — so if you're interested in that, definitely read it!

And of course a bit of chat about [Befunge](http://catseye.tc/node/Befunge-93), [Gemooy](http://catseye.tc/node/Gemooy),
[SMETANA](http://catseye.tc/node/SMETANA), and such things, which may also be of interest.

Enjoy!

In the meantime, I'll be over here, feeling old.

### 0x04 is the cruelest month: NaPoGenMo and altgamejam

*   summary: [NaPoGenMo](https://github.com/NaPoGenMo/NaPoGenMo2015/) and [altgamejam](http://jams.gamejolt.io/altgamejam) underway!
*   date: Sun, 12 Apr 2015 16:46:33 GMT

April is National Poetry Writing Month!  And as [NaNoGenMo](http://catseye.tc/node/NaNoGenMo) is to
NaNoWriMo, so [NaPoGenMo](https://github.com/NaPoGenMo/NaPoGenMo2015/)
is to NaPoWriMo:

> The Goal:
> Spend the month of April writing code that generates a poem. Repeat.
> 
> The Rules:
> The only rule is that you share at least one poem and also your source code at the end.

And who, I ask, can resist poetry written by computers?

For our part, we have written a few short poetry generators,
mostly in the form of `bash` one-liners, whose output can be found
[in this Github issue](https://github.com/NaPoGenMo/NaPoGenMo2015/issues/9).

More significantly, we've also written a
[Hello, world!](https://github.com/catseye/Beatnik/blob/master/eg/hello-world.beatnik)
program in the [Beatnik](http://esolangs.org/wiki/Beatnik) programming
language (and, for the record, determined that writing a quine in Beatnik
is out of the question.)

Oh, but that's not all!  Oh, but you'll wish it was all, you will!

For it is the case that the month of April is also when the
[ALTERNATIVE GAME JAM](http://jams.gamejolt.io/altgamejam)
is taking place.

What exactly an "alt game" *is* we're still not sure, but that didn't
stop us from making one.  It's hosted on GameJolt as a condition of
the jam, and there's this annoying ad that you have to wait through
to see the actual game, but that shouldn't stop you from trying it.
Here it is:

[The New Gamerly Realism](http://gamejolt.com/games/other/the-new-gamerly-realism/59524/)

*WE ENCOURAGE YOU TO JOIN AND PARTICIPATE YOUR BEST IN THESE GLORIOUS NEW OLYMPIADS*

### Matchbox, a toy race-condition finder

*   summary: We present [Matchbox](http://catseye.tc/installation/Matchbox), a toy race-condition finder.
*   date: Mon, 30 Mar 2015 07:42:48 GMT

We present [Matchbox](http://catseye.tc/installation/Matchbox), a toy race-condition finder —
it's an analyzer for a toy [assembly](http://catseye.tc/node/Assembly)-like language that
runs in a [web browser](http://catseye.tc/node/HTML5).  It finds all interleavings between
two programs, runs them all on shared memory, and declares there to
be no race conditions if and only if every interleaving is either
impossible, or produces the same result.

I wrote Matchbox to (cheesy as it sounds) raise awareness of race
conditions.  Also, [Peterson's Algorithm](http://en.wikipedia.org/wiki/Peterson%27s_algorithm)
is beautiful, and Matchbox graphically demonstrates that it does work.
For a fuller account of why I wrote Matchbox, see the commentary on
the [Matchbox](http://catseye.tc/node/Matchbox) node, and the projects' [README](https://github.com/catseye/Matchbox/)
file.

Two more gewgaws have been installed online since the last announcement, too;
[Black Hole Poem](http://catseye.tc/installation/Black%20Hole%20Poem) and [Noise to Signal No. 1](http://catseye.tc/installation/Noise%20to%20Signal%20No.%201).
Enjoy.

### One way to tile the plane with Wang tiles

*   summary: One way to [tile the plane with Wang tiles](http://catseye.tc/installation/Backtracking%20Wang%20Tiler).
*   date: Fri, 20 Feb 2015 11:08:52 GMT

tl;dr [Backtracking Wang Tiler](http://catseye.tc/installation/Backtracking%20Wang%20Tiler) and it's pretty to watch go.

You're probably familiar with tesselations.  Tilings, that is.  A Cartesian
grid tiles a plane with squares, a honeycomb tiles a plane with hexagons,
and so forth.  There are lots of examples.  But the most interesting tilings,
to me, are _aperiodic_ ones — tilings that are not regular.  Similar-looking
sections of them may repeat, but the tiling as a whole never repeats
exactly.

The most well-known example is probably Roger Penrose's kite-and-dart
construction.  But, as is often the case, the most famous example was not
the first.  The foundational work on aperiodic tilings was done years
earlier, by Hao Wang, who came up with the concept, and posed the question
(I'm paraphrasing):

> Given a set of tiles, is there an algorithm that tells if they tile
> the plane aperiodically or not?

In other words, is the set of aperiodic tilings decidable?  And Berger
proved that it was not, by reducing it to the Halting Problem for
Turing machines.  Each aperiodic tiling can be put into one-to-one
correspondence with a Turing machine that never halts.

That suggests that aperiodic tilings are tricky business, indeed.

But to be clear, this is a general question about arbitrary sets of tiles.
Once you have picked a set of tiles, you may well prove it is aperiodic,
and you may well tile the plane with them.

Of course, that business is still a little tricky.  You can certainly
work out an aperiodic tiling by hand, using human ingenuity and trial and
error.  Can you instruct a computer to do it?  Yes, although unsurprisingly
it leans a bit more on the trial and error side.
    
But wait — if a tiling corresponds to a Turing machine that never halts,
how can you write a program for it?  Ah, red herring — you just write a
program that never quits.  (Indeed, if you want to tile the "entire"
infinite plane, what choice do you have?)  But note that, technically,
this might not be an algorithm, because algorithms are generally defined
to terminate and produce a result.  But we can put off that inevitable
semantic debate by just avoiding that term.

At any rate, the process I've used is:

*   Select tiles randomly and place them in a spiral, so that new tiles
    are always adjacent to existing tiles.  (Except the first one, of
    course.)
*   If at any point you find you can't place a new tile along the
    spiral, because it doesn't match any of the existing tiles,
    then backtrack — erase the previous tile you placed, try another
    possibility for that position chosen at random, and continue
    again from there.

I'm not claiming this is efficient!  It ain't, not by a long shot.
But it's correct — it _will_ tile the plane "eventually", as long as the
set of tiles permit tiling (whether periodic or aperiodic) — and it can be
[pretty to watch go](http://catseye.tc/installation/Backtracking%20Wang%20Tiler).

It's also apparent that "spiral" and "backtrack" are incidental;
it's just nicely linear to arrange it this way, but you should be able
to accrete random clumps too.  Which might be even more inefficient,
but even prettier to watch go.  Dunno, would have to try it, and I
haven't yet.

One slightly interesting thing about the implementation is that the
backtracking is not implemented the obvious way, with recursion,
because we want to display the state of the tiling as we go along,
and Javascript in a web browser in particular won't allow that; it
won't update the display until the current computation is finished
and it's ready to handle a new event.

Therefore, backtracking is implemented with what are essentially
continuations.  All of the alternate, untried possibilities for each
position are stored along with every tile, as it is placed.  To be
sure, this is not a general-purpose continuation, but it does
encapsulate all the pertinent data for the tiling process — data that
would otherwise be embedded in the function call stack, and not
accessible to us.

The implementation is also in the public domain, so if you want to
hack on it, feel free.  It resides in the
[Wang Tilers repository on Github](https://github.com/catseye/Wang-Tilers),
in which you can also find further documentation on it.  And maybe,
in the future, other implementations and/or other tiling strategies.

Since this announcement has already gotten quite long, maybe I'll cap
it off with an interesting question.

There are, as I understand it, Wang tilings which aren't even computable:
they correspond to Turing machines for which there is no computable method
to generate them.  (They never halt, but we can't prove this.)

However, this automaton we got here operates _randomly_.  The implementation
is pseudo-random, to be true, but let's assume this is just an approximation
of an idealized automaton with genuinely randomized tiling choices.

In a sense, it is always trying to find a non-terminating Turing machine.
If the current tiling it's trying to lay down doesn't work (= represents
a Turing machine which halts,) it backtracks and tries a different
randomly-chosen tiling until it finds a a tiling that does work
(= represents a Turing machine that doesn't halt.)

If left to run forever, might this automaton generate a non-computable
never-halting Turing machine, in the guise of a Wang tiling?

Perhaps I misunderstand it, but I think it could.  Just because you
can't computationally generate such a Turing machine, doesn't mean
that taking the limit of an infinite random sequence couldn't yield
such a thing.  Certainly, the closure of all such tilings would include
these, and I can't see what's _stopping_ this automaton from "accidentally"
picking one.

Of course, taking the limit of an infinite random sequence could be a
philosophically troubling concept — perhaps as philosophically troubling
as generating an uncomputable object.

After all, if your tiling does tile the plane, you've proved the
corresponding Turing machine does indeed never halt.

But it's hard to see how you'd know your tiling _does_ tile the plane,
without first knowing that the Turing machine does not halt.

Perhaps questions about infinity are best saved for people who have
an awful lot of time on their hands.

### Is Twitter your thing?

*   summary: Is [Twitter](https://twitter.com/catseye_tc) your thing?
*   date: Fri, 13 Feb 2015 09:54:57 GMT

I ask because it is definitely not my thing.

But I recognize that it might be *your* thing, and that you might find it
convenient to receive updates about Cat's Eye Technologies, via Twitter.

I mean, on a technical level, there's no reason it *shouldn't* serve as a
good platform for announcements and updates.  It's not my fault that
that's not how most people use it.

And, hey, it's Friday the 13th today!.  Spooky stuff happens on Friday
the 13th,  right?  Spooky stuff like announcing that you are now on
(*ugh*) Twitter.

Thus, I will grit my teeth and bear it.

Here, follow your little hearts out:

*   **[@catseye_tc](https://twitter.com/catseye_tc)**

*Content you can expect*:

*   announcements of new things at Cat's Eye Technologies, **yes**;
*   highlighting interesting esolangs, computational art,
    conceptual art, and related stuff out there, **yes**;
*   every single brainfart I have, **no**;
*   retweets of every clever thing that passes through my feed, **no**.

*Frequency you can expect*:

*   We're aiming for 1 tweet per day.
*   Rarely will you ever see more than 2 tweets in the space of 12 hours.

If Twitter is *not* your thing, fear not, as this self-same [Article](http://catseye.tc/node/Article)
[feed](http://catseye.tc/feeds/atom_30_news.xml) will continue, and
will remain pretty much as it has been for the past, um, seven and a
half years! (holy cow!)

### Wierd (one of 'em) is now installed online

*   summary: [Wierd](http://catseye.tc/node/Wierd) ([one of 'em](http://catseye.tc/node/Wierd%20%28John%20Colagioia%29), anyway) is now [installed online](http://catseye.tc/installation/Wierd%20%28John%20Colagioia%29).
*   date: Mon, 09 Feb 2015 12:44:58 GMT

So back in the mists of time — by which I mean the late 90's — there was this three-way
email conversation between me, [Ben Olmstead](http://catseye.tc/node/Ben%20Olmstead), and [John Colagioia](http://catseye.tc/node/John%20Colagioia), right?

And in it, we collectively sketched a fungeoid language which combined elements of
[Befunge-93](http://catseye.tc/node/Befunge-93) with elements of [brainfuck](http://catseye.tc/node/brainfuck) and added an original element — it's the
bends in the chain of symbols, rather than the symbols themselves, that determine
which instructions are executed.

And now, a new page has been added to this language's
[long and fuzzy history](https://github.com/catseye/Wierd/blob/master/README.markdown):
it, or rather, [one of the extant dialects of it](http://catseye.tc/node/Wierd%20%28John%20Colagioia%29),
has been implemented in [Javascript](http://catseye.tc/node/Javascript) and [HTML5](http://catseye.tc/node/HTML5) with [yoob.js](http://catseye.tc/node/yoob.js) and installed online
here:

*  [installation/Wierd (John Colagioia)](http://catseye.tc/installation/Wierd%20%28John%20Colagioia%29)

This may be the first implementation of (any) Wierd in a web browser.  Or it may not;
searching the web for "wierd javascript" doesn't return as many results as you might
think (as, apparently, a lot of people think Javascript is pretty weird, and have a
propensity to mis-spell the word "weird".)

I would like to implement [the other extant dialect](http://catseye.tc/node/Wierd%20%28Milo%20van%20Handel%29), too,
some day.  But not today.

### Presenting Schrödinger's Game of Life

*   summary: Presenting [Schrödinger's Game of Life](http://catseye.tc/installation/Schr%C3%B6dinger%27s%20Game%20of%20Life).
*   date: Sat, 07 Feb 2015 12:50:11 GMT

We present [Schrödinger's Game of Life](http://catseye.tc/node/Schr%C3%B6dinger%27s%20Game%20of%20Life), which is exactly what it
sounds like: [Conway's Game of Life](http://catseye.tc/node/Conway%27s%20Game%20of%20Life) meets [Schrödinger's Cat](http://catseye.tc/node/Schr%C3%B6dinger%27s%20Cat).

Each individual cell in the playfield may be in one of three states:
**Alive**, **Dead**, or **Possibly-Alive-Possibly-Dead** (which we call
**Cat**.)

Put another way, it's a [cellular automaton](http://catseye.tc/node/Cellular%20automaton)
that incorporates [non-determinism](http://catseye.tc/node/Non-deterministic).

To see it in action and play with it in your web browser, you can
go over to its [online installation](http://catseye.tc/installation/Schr%C3%B6dinger%27s%20Game%20of%20Life).
    
For a full account of its development, see
[its README document](https://github.com/catseye/Schroedingers-Game-of-Life/blob/master/README.md).

### Canvas Feedback: rated T for Trippy

*   summary: [Canvas Feedback](http://catseye.tc/installation/Canvas%20Feedback) will blow your mind, or at least ruin your eyes.
*   date: Tue, 27 Jan 2015 11:28:29 GMT

Whether you get out the joss sticks and put Ravi Shankar on the stereo
is up to you.  But either way, you should check out 
[Canvas Feedback](http://catseye.tc/installation/Canvas%20Feedback).

It all started while discussing the 1970's-era Doctor Who title sequence
and the video art of [Nam June Paik](http://catseye.tc/node/Nam%20June%20Paik).  The digital era has made many
of those analogue techniques less accessible — so, even if we can't bring
them back, why not see what it's like if we try to adapt them for the
modern world of web browsers and graphics cards?

### This Maze is Never-Ending.  Plus two gewgaws

*   summary: This [maze](http://catseye.tc/installation/The%20Never-Ending%20Maze) is never-ending. Plus two [gew](http://catseye.tc/installation/Eine%20kleine%20Glitchfraktal)-[gaws](http://catseye.tc/installation/Uncle%20Ankur).
*   date: Tue, 20 Jan 2015 14:21:14 GMT

A text adventure — yes, I could never quite get the hang of calling
it "interactive fiction" — a text adventure game that I wrote in [Inform](http://catseye.tc/node/Inform)
about fifteen years ago, is now [installed online](http://catseye.tc/installation/The%20Never-Ending%20Maze)
as a [Java applet](http://catseye.tc/node/Java%20applet) thanks to [Zplet](http://catseye.tc/node/Zplet).

If you like this, you might also like [Cheshire Text](http://catseye.tc/installation/Cheshire%20Text).

If you hate this, you might instead like two new gewgaws that have also
been put online: [Eine kleine Glitchfraktal](http://catseye.tc/installation/Eine%20kleine%20Glitchfraktal) and
[Uncle Ankur](http://catseye.tc/installation/Uncle%20Ankur).  Neither one involves any text whatsoever
(well, just a little on the control panels, maybe.)

### Version 0.2 of The Platform - now with Torrent

*   summary: Version 0.2 of [The Platform](https://github.com/catseye/The-Platform) — now with [torrent](https://raw.githubusercontent.com/catseye/The-Platform/master/torrent/The-Cats-Eye-Technologies-Platform-0.2.torrent)!
*   date: Fri, 16 Jan 2015 20:52:27 GMT

Version 0.2 of [The Cat's Eye Technologies Platform](http://catseye.tc/node/The%20Cat%27s%20Eye%20Technologies%20Platform) has been released.
It's based on NetBSD 6.1.5 instead of 6.1.4, and has other minor version
bumps like that in it.  But the major thing now is that, if you don't
want to go through the hassle of *building* it, you can *download* a
pre-built image of it via this torrent right here:

*   [The-Cats-Eye-Technologies-Platform-0.2.torrent](https://raw.githubusercontent.com/catseye/The-Platform/master/torrent/The-Cats-Eye-Technologies-Platform-0.2.torrent)

For more information on The Platform, please refer to
[its repository on Github](https://github.com/catseye/The-Platform)
and/or the [announcement of the release of version 0.1](http://catseye.tc/node/Introducing%20The%20Cat%27s%20Eye%20Technologies%20Platform).

### The Aftermath of NaNoGenMo 2014

*   summary: The Aftermath of [NaNoGenMo 2014](http://catseye.tc/node/NaNoGenMo%202014).
*   date: Thu, 18 Dec 2014 20:58:20 GMT

So [NaNoGenMo](http://catseye.tc/node/NaNoGenMo%202013) survived into a [second year](http://catseye.tc/node/NaNoGenMo%202014).

It probably would have made more sense to mention it at the beginning
of November, rather than two-thirds through December, but — well —
it's all very exciting when its time of year comes around you see,
and I get distracted.  Last year, I didn't bother to say anything about
it even _after_ it was over.  So this is, at least, an improvement over that.

In 2014, Cat's Eye Technologies (or rather, Chris Pressey sponsored by
the auspices of Cat's Eye Technologies — or something) staffed the
[NaNoGenLab](https://github.com/catseye/NaNoGenLab/tree/nanogenmo-2014-end),
running one experiment in the generation, transformation, and general
mutilation of text, per day, for the month of November.  (So that was a
goal of: 30 experiments.  But we actually ended up with 32, somehow.)

Out of this chaos, we generated some novels too, which you can read
in the [Text](http://catseye.tc/node/Text)s section.

And I regret with alarm to note that, right in the middle of November, there was
an unfortunate...
[aesthetic incident](https://github.com/dariusk/NaNoGenMo-2014/issues/10#issuecomment-63069185)...
which resulted in... _measures_ being taken, you see...
resulting in the creation of
[this monstrosity](https://github.com/cpressey/NaOpGenMo/).  Listen
at your own risk.
   
Oh!  And, um, I dusted off some [gewgaws](http://catseye.tc/node/Gewgaw) that were just languishing
in the lab, and put them on the site.  They are, in no particular order,
[The Judgment of Paris](http://catseye.tc/installation/The%20Judgment%20of%20Paris),
[Woman on Film](http://catseye.tc/installation/Woman%20on%20Film),
[Radialjective](http://catseye.tc/installation/Radialjective), and
[Circus Xamulus](http://catseye.tc/installation/Circus%20Xamulus).

And also [Cheshire Text](http://catseye.tc/installation/Cheshire%20Text), which is not a gewgaw but a text, but which
was not done for NaNoGenMo, because it's not a novel.  And a
[Text Uniquifier](http://catseye.tc/installation/Text%20Uniquifier), which isn't a novel _or_ a text but
which _was_ done for NaNoGenMo because it's a generator, or at least a
filter, which I've classified, provisionally, as a gewgaw.  Clear as mud, eh?

### Introducing The Cat's Eye Technologies Platform

*   summary: The première of [The Cat's Eye Technologies Platform](https://github.com/catseye/The-Platform).
*   date: Sat, 04 Oct 2014 18:49:59 GMT

We are happy to announce the first release of
[The Cat's Eye Technologies Platform](http://catseye.tc/node/The%20Cat%27s%20Eye%20Technologies%20Platform),
version 0.1.  It is a "distro" (if I may use that "word") of
[NetBSD 6.1.4](http://www.netbsd.org/releases/formal-6/NetBSD-6.1.4.html),
containing almost all of Cat's Eye Technologies' software distributions and
the infrastructure needed to build and run them.

Each of the software distributions is tagged at a particular version
(The Platform v0.1 can be thought of as a "versionset") at which they
build and run on NetBSD, and if they have automated tests, the relevant
ones pass.

There is no binary distribution yet, so if you want a copy of
The Platform, you'll have to build it yourself (instructions for doing
so are included.)  However, we hope to distribute a binary image once we
sort out how best to host large files.

It is, in a sense, an exercise in "software canning" to diminish bitrot.
As long as you have an i386 emulator (such as [QEMU](http://catseye.tc/node/QEMU)) which can boot
into NetBSD, you will be able to use these software distributions, without
having to worry about conflicts due to upgrades and suchlike.

And as an exercise, it was somewhat illuminating; almost all of our
projects, excluding what's hosted [online](http://catseye.tc/node/Online%20Installation), can
be run on a rather modest environment of open-source infrastructure:
NetBSD (which already contains Lua and `gcc`), GNU Make, cPython, Perl,
Erlang/OTP (stripped down), Hugs98, Chicken Scheme, yasm, and Ophis.

### BefOS version 0.10 released and installed online

*   summary: [BefOS](http://catseye.tc/node/BefOS) version 0.10 released and [installed online](http://catseye.tc/installation/BefOS).
*   date: Mon, 22 Sep 2014 17:19:58 GMT

Look!  Up on [this web page!](http://catseye.tc/installation/BefOS)  Is it [Befunge](http://catseye.tc/node/Befunge-93)?
Is it an [operating system](http://catseye.tc/node/operating%20system)?  No... no, it's just a disk sector editor
with some unusual features, really.

Er... in case you were wondering... yes, this *is* the time of the
year (September) when I usually do something to celebrate the anniversary
of [Befunge-93](http://catseye.tc/node/Befunge-93).  It's 21 years old now, so if it were a person, it
could drink legally in the United States, and, basically, it would be
tried as an adult in pretty much any court in the world.

BefOS is a bit younger (but it would still be old enough to, what,
drive?), but, in answer to your unspoken question, no, updating BefOS was
not what I was planning to do for Befunge-93's birthday.  It's only
tangentially related.

In fact, I've been working on cleaning up the Befunge-93 (and [Maentwrog](http://catseye.tc/node/Maentwrog)
and [RUBE](http://catseye.tc/node/RUBE) reference distributions — making their implementations
compile cleanly on multiple platforms ([Linux](http://catseye.tc/node/Linux), [NetBSD](http://catseye.tc/node/NetBSD), [FreeDOS](http://catseye.tc/node/FreeDOS),
and [AmigaDOS 1.3](http://catseye.tc/node/AmigaDOS%201.3).)

But that's all not quite done yet; hopefully the Befunge-93 distribution
will have a few more surprises in it before the end of the year.

But before you bemoan the barbarity of Befunge's birthday bash being a
bit belated, ... well, nothing really, I just wanted to get some
alliteration out of my system there.  Have fun with [BefOS](http://catseye.tc/installation/BefOS).

### Yolk, a Meta-circularly-defined Programming Language

*   summary: Release of the meta-circularly-defined language [Yolk](http://catseye.tc/node/Yolk).
*   date: Sun, 24 Aug 2014 14:10:52 GMT

And it came to pass that my mind turned once again to the question
of whether there are any universal computational classes smaller
than the class of recursively enumerable functions.

And lo, did I try to write a self-interpreter that was obviously
not Turing-complete; and lo, did I fail.  Pretty sure I failed, yeah.

But the result, behold!  It was less than half the size of [Pixley](http://catseye.tc/node/Pixley)'s
meta-circular interpreter.  So did I keep it, and did I christen it
[Yolk](http://catseye.tc/node/Yolk), and verily did I wax philosophical in its README about `cons`
and stuff.

### Release of toolshelf version 0.1-2014.0823

*   summary: Release of [toolshelf](http://catseye.tc/node/toolshelf) version 0.1-2014.0823.
*   date: Sat, 23 Aug 2014 07:49:41 GMT

Oh man, so many things updated recently, but this news feed is so
not one of them.  OK, where to begin.  OK...

[Cat's Eye Technologies](http://catseye.tc/node/Cat%27s%20Eye%20Technologies) really isn't in the business of making
tools.  (Implementations of programming languages excepted —
they're incidental, they're in service of the languages themselves.)

But we've implemented so many programming languages that, without
some kind of tooling, the situation would become unwieldy.  So, for
example, we designed [Falderal](http://catseye.tc/node/Falderal) and build [py-falderal](http://catseye.tc/node/py-falderal) so that
all these programming languages could have their example programs
presented nicely and tested in an automated way.

But there have been other, more fundamental problems to solve.  How
do you get all of these implementations onto a machine in the first
place, for instance?  If the distribution is self-contained, that's
not a huge problem — download it and maybe build it and run it.  But
if it's not self-contained, if it has dependencies (and ultimately they
all do, because each implementation is written *in* something,) then it
becomes a package management problem.

And I detest package managers.  I don't like their fragile package
databases that get corrupted if you look at them wrong.  I don't
like their tendency to shotgun files all over my filesystem; nor do I
like having faith that, if asked to remove the package, they will find
them all and delete them.  I don't like that they require root
priviledges (*root priviledges!*) to install anything.  And I don't
like that they're almost never portable; there's one for every operating
system and one for every programming language and never mind the fact
that every modern operating system hosts more than one programming language.

So we wrote our own and called it [toolshelf](http://catseye.tc/node/toolshelf).  **toolshelf is
a package installer which neither uses packages, nor installs anything.**
(Why yes, I am feeling a little farklempt, but that's neither here nor
there.)  It doesn't maintain a package database, it keeps all its files
in one place (which you can just blow away if you don't want it anymore),
it doesn't need root priviledges, and it is quite portable (in theory,
anyway.)

It simply downloads (or clones) what you ask it to, makes its best guess
at how to build it, and if that succeeds, makes its best guess at which
files are executables and libraries that you care about, and puts those
files on the appropriate search paths.  Voilà!  Sorted.

Ah, I know what you're thinking.  You're thinking, that's insane.
That's not a real package manager.  That's going to fail in *so* many cases.

All true.  And all irrelevant.  In fact, it works in a surprising number
of cases.  It's actually really good for random little projects you find
on Github and elsewhere.  (It's not like they're ever going to show up
in a "real" package manager.  And when you get bored with them, you just
blow away the clone directory.)  And really, the other option is installing
from source — and you can just think of toolshelf as an assistant that makes
installing from source a lot less painful.
    
More to the point, it works really well with our projects.  It is the
recommended way to start using software from Cat's Eye Technologies.  Just
[install toolshelf](https://github.com/catseye/toolshelf/#quick-start)
and then

    toolshelf dock @@catseye

and watch it download, build, and install everything.

Even though it was originally only intended for random little projects, I
now regularly dock things like [QEMU](http://catseye.tc/node/QEMU), Chicken Scheme, and Django with it.
I recently set up two Linux environments for my own use; on each of them,
I installed only maybe a dozen packages from `apt`, and I haven't used
`pip` at all.  Most of what I've needed, I've brought in with toolshelf.

Of course, there are still some rough edges — and the way it works, there
will always *be* rough edges — but there is a lot of potential too.

So, [check it out](http://catseye.tc/node/toolshelf)!

### Music, Pictures, Texts, and Wunnel

*   summary: [Music](http://catseye.tc/node/Online_Installation#music_exhibit), [Pictures](http://catseye.tc/node/Online_Installation#pictures_exhibit), [Texts](http://catseye.tc/node/Online_Installation#texts_exhibit), and [Wunnel](http://catseye.tc/installation/Wunnel).
*   date: Mon, 26 May 2014 15:37:50 GMT

The [Online Gallery](http://catseye.tc/node/Online%20Installation) has had an overhaul since
the last time I announced anything regarding it.  It's got tabs with
proper anchors and stuff now.

In an attempt to prove that I am a polymath (which is a Greek word which means
"bad at everything",) music I've written and pictures I've made
and texts I've (meta-)written are available under the tabs there now.

But its main purpose is still for interactive HTML5-y stuff, especially
esolangs, and lo, there is
[an HTML5 implementation of Wunnel](http://catseye.tc/installation/Wunnel) there now too.

And with this implementation of Wunnel, [yoob.js](http://catseye.tc/node/yoob.js) has reached another
release point, version 0.6.  But, of course, it is still basically in the
work-in-progress stage, with things changing all over.

### Github as a computer dating service (!)

*   summary: [Github as a computer dating service](https://github.com/cpressey/Operation-Match-Github) (not that I can in good conscience recommend that.)
*   date: Tue, 25 Mar 2014 08:18:34 GMT

As a little hack on the weekend, I started playing with the Github API,
after using it for more serious purposes in [toolshelf](http://catseye.tc/node/toolshelf).  The result was

[Operation Match, Github edition](https://github.com/cpressey/Operation-Match-Github)

which turns Github into a computer dating service.  Well, not really,
and I really *can't* recommend using Github for romance...

...but the script *does* try to find Github users who have tastes that
are similar to those to a given user, based on the starred repositories
they have in common.  And while it's very crude metric,
I did end up finding a few users with it whose interests seem broadly
similar to my own, who I have since started following.

(And I suppose that it's a coincidence that
just as I was about to write this announcement, 
the BBC ran [this article](http://www.bbc.co.uk/news/business-26613909)?)

### De-pict-sly: Pixley and Etcha in HTML5

*   summary: [Pixley](http://catseye.tc/installation/Pixley) and [Etcha](http://catseye.tc/installation/Etcha) are now online.
*   date: Sat, 11 Jan 2014 14:44:17 GMT

We present, just below, the [Pixley](http://catseye.tc/node/Pixley) reference interpreter (that is,
the one that's written meta-circularly in Pixley itself)
depicted as a set of nested, coloured rectangles.  Looks a bit like
an [integrated circuit](http://zeptobars.ru/en/read/how-to-open-microchip-asic-what-inside),
perhaps, except without the wires.  I'll leave it to you to decide if this
is unsurprising or not.  You can see this and more in [Pixley](http://catseye.tc/installation/Pixley).

![Pixley Interpreter as nested rectangles](http://catseye.tc/images/generated/Pixley.png)

But that's not all!  We also present what happens when you run
that one [Etcha](http://catseye.tc/node/Etcha) example program over and over again.  Looks a bit like
a pattern produced by [Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant),
and perhaps that is no surprise at all.  You can try this, and any other
Etcha program you care to concoct, yourself in [Etcha](http://catseye.tc/installation/Etcha).

![An Etcha program state after many repetitions](http://catseye.tc/images/generated/Etcha.png)

### Release of yoob.js version 0.5

*   summary: [yoob.js](http://catseye.tc/node/yoob.js) 0.5 has been released.
*   date: Wed, 08 Jan 2014 19:19:33 GMT

[yoob.js](http://catseye.tc/node/yoob.js) has been mentioned in several announcements, but this is the
first announcement concerning it specifically.  It started out as a
project to replace [yoob](http://catseye.tc/node/yoob), running esolangs in [HTML5](http://catseye.tc/node/HTML5) instead of a
[Java](http://catseye.tc/node/Java) applet, but as of this release — version 0.5 — it has grown some
generally-useful features for making animated and interactive things in
HTML5, especially on the `<canvas>` element.

All that notwithstanding, this is a fairly minor announcement for a
fairly minor release.  The major version number is still at zero, and
there will likely be a few backwards-incompatible changes in the next
version.  But 0.5 has enough reasonably useful junk in it that it's a
comfortable snapshot of things at this stage.

### Shelta v1.2 online in FreeDOS in v86

*   summary: [Shelta](http://catseye.tc/node/Shelta) 1.2 released — and bootstrappable [online](http://catseye.tc/installation/Shelta)!
*   date: Thu, 12 Dec 2013 18:19:08 GMT

Version 1.2 of the [Shelta](http://catseye.tc/node/Shelta) distribution has been released.  This
is a very minor update, with the only change to the language being
essentially inconsequential: Shelta source files now must end with
[everybody's favourite character](http://prog21.dadgum.com/76.html),
the vertical tab, instead of a null byte.

This was to work around what seems to be a subtle bug in [FreeDOS](http://catseye.tc/node/FreeDOS).
And that, in turn, was to get Shelta running under FreeDOS inside the
[HTML5](http://catseye.tc/node/HTML5)-based [IBM PC compatible](http://catseye.tc/node/IBM%20PC%20compatible) emulator, [v86](http://catseye.tc/node/v86).  You can
read all the gory details [here](https://github.com/catseye/Shelta/blob/master/doc/fdos2013.txt).

Anyway, this all brings us to the good news, which is: you can now
play with Shelta — including bootstrapping it —
[online, right here](http://catseye.tc/installation/Shelta)!

### Presenting Amiga Gondola

*   summary: [Amiga Gondola](http://catseye.tc/node/Amiga%20Gondola) sets up a development environment for AmigaDOS 1.3 in E-UAE.
*   date: Tue, 12 Nov 2013 15:58:08 GMT

This year — about two months ago, to be more exact — marked
the 20th anniversary of [Befunge-93](http://catseye.tc/node/Befunge-93).  How to commemorate
this historic occasion?  

Well, one way would be to design its twenty-year successor,
"Befunge-113".  But that's just _typical_, y'know?  Besides,
I doubt there's much left to be done with Befunge besides
suck all the fun out of it by defining it more formally.
At any rate, I don't think any Befunge-113 I could come up
with at the moment would make very many people happy, so:
proposal declined.

A better idea: make it easier to re-create the development
environment in which Befunge-93 was originally developed.
Namely, [AmigaDOS 1.3](http://catseye.tc/node/AmigaDOS%201.3) on an [Amiga 500](http://catseye.tc/node/Amiga%20500).

So, that's what we did, and the result is [Amiga Gondola](http://catseye.tc/node/Amiga%20Gondola),
a set of shell scripts which, given an [E-UAE](http://catseye.tc/node/E-UAE) emulator,
images of the Workbench and Extras disks, and access to
Aminet, put together an environment which, while not being
a totally authentic copy of the environment I was using
twenty years ago, is a perfectly cromulent development
environment for AmigaDOS 1.3.

More information about Amiga Gondola and some nice screenshots
can be found in its
[README](https://github.com/catseye/Amiga-Gondola/blob/master/README.markdown).

### Release of Falderal version 0.9 "Navy Pier"

*   summary: [Falderal](http://catseye.tc/node/Falderal) version 0.9 "Navy Pier" has been released.
*   date: Tue, 29 Oct 2013 20:22:36 GMT

Well, that was quick — well, we were on a roll (whoa, déjà vu.)
[Falderal](http://catseye.tc/node/Falderal) 0.9 introduces one major new feature —
the ability to supply input to a test.  Typically, the test body
would be considered the program (in some language) being tested,
and the input would be sent to the standard input of the language
interpreter (or whatever) to ensure that that program reacts the
way you expect it to, given that input.

There are also a number of cleanups and minor improvements in
`py-falderal`, including warning you if there are no tests to
be run, or if it has run the same tests multiple times.  It will
also produce partial test results if you break it with `^C` in
the middle of a long test run.

### Release of Falderal version 0.8 "Ukrainian Village"

*   summary: [Falderal](http://catseye.tc/node/Falderal) version 0.8 "Ukrainian Village" has been released.
*   date: Sat, 26 Oct 2013 18:45:30 GMT

A "new" version of [Falderal](http://catseye.tc/node/Falderal), version 0.8 "Ukrainian Village", has
been released.

I say "new" because, well, it's basically the same as it's been for the
last year, when the `Test.Falderal` implementation of Falderal in
[Haskell](http://catseye.tc/node/Haskell) was replaced by the `py-falderal` implementation in
[Python](http://catseye.tc/node/Python), which was christened the new reference implementation.

This switcheroo happened right after the last distribution of Falderal
in which `Test.Falderal` was the reference implementation,
version 0.7 "Odgen Avenue", was released.  Unfortunately, I see by
my records that I never announced that in this news feed, so, this
may be news to you.  Yes, it's written in Python now.  And much like
version 0.7 was a release of Falderal to get it out of the way so I
could start working on a brand new code base (in Python), version 0.8
is a release to get this relatively-stable Python version out of the way
so I can start making larger, long-overdue improvements to it.

The Falderal Literate Test Format has not changed much between 0.7
and 0.8.  The main change is now that blocks *must* be indented by
four spaces.  It is generally assumed that Falderal test files will be
embedded in Markdown and have file extensions like `.markdown`
that let software (e.g. Github and Bitbucket) know how to pretty-format
them.

In related news, recent improvements to [toolshelf](http://catseye.tc/node/toolshelf) allow it to
run any tests defined in a source tree, and to operate on all source
trees owned by a given user on a given host.  The end result being
that we can now say `toolshelf test bitbucket.org/catseye/all` and
have it test *all* of Cat's Eye Technologies' active distributions.
And the even better news is that, out of approximately 112 distributions,
22 have tests (mostly done with Falderal), and all 22 of those currently
pass on both Ubuntu and Windows (under Cygwin).

### New implementations of Xoomonk and Pixley

*   summary: Xoomonk 1.0 and Pixley 2.0-2013.1024 have been released, each with new implementations.
*   date: Thu, 24 Oct 2013 19:42:47 GMT

[Xoomonk](http://catseye.tc/node/Xoomonk) 1.0 was recently released.  For this release, a Xoomonk
interpreter was implemented in [Python](http://catseye.tc/node/Python), using the [Falderal](http://catseye.tc/node/Falderal) tests
written for the *test-driven language design* approach used in Xoomonk
0.1's documentation.  I've used test-driven language design successfully
in other projects ([Castile](http://catseye.tc/node/Castile), [Robin](http://catseye.tc/node/Robin)) since Xoomonk was released, but
it was the first project in which I proposed the concept, so it's nice to
see it finally realized there.

The semantics of Xoomonk 1.0 are slightly simpler than those set out for
Xoomonk 0.1 — specifically, a variable is considered unsaturated in a block
if it is *never* assigned a value in that block (and not just if it is
used in the block before it is assigned a value.)  The syntax for built-ins
also changed slightly.  But these are not major changes, and the same
original mouthfeel of malingering updateable stores is still there (and
implemented!)

[Pixley](http://catseye.tc/node/Pixley) 2.0-2013.1024 has also been released.  There are no changes to
the language in this release, but two new implementations, [mignon](http://catseye.tc/node/mignon),
in [ANSI C](http://catseye.tc/node/ANSI%20C), and [haney](http://catseye.tc/node/haney), in [Haskell](http://catseye.tc/node/Haskell), have been added to the
reference distribution.  They both implement Pixley well enough to serve
as the bottom of a tower of Pixley interpreters.  Many of the supporting
materials (scripts, tests) have also been cleaned up. 

### I got two new gewgaws and an esolang... online

*   summary: I got two new [gew](http://catseye.tc/installation/Chzrxl)[gaw](http://catseye.tc/installation/Multicolouralism)s and an [esolang](http://catseye.tc/installation/ZOWIE)... online.
*   date: Sun, 13 Oct 2013 02:27:17 GMT

Two new HTML5 gewgaws in the [Gallery](http://catseye.tc/node/Online%20Installation):
[Chzrxl](http://catseye.tc/installation/Chzrxl) and [Multicolouralism](http://catseye.tc/installation/Multicolouralism).

Also, the public-domain gewgaws are now kept in
[a repository on Github](https://github.com/catseye/HTML5-Gewgaws)
with
[a mirror on Bitbucket](https://bitbucket.org/catseye/html5-gewgaws).

Also, the esolang [ZOWIE](http://catseye.tc/installation/ZOWIE) is now runnable online.
Unlike previous online esolang implementations, this one didn't involve
re-implementing ZOWIE in [Javascript](http://catseye.tc/node/Javascript).  Instead, the ZOWIE reference
interpreter, written in [Python](http://catseye.tc/node/Python), is running under [Skulpt](http://catseye.tc/node/Skulpt) on that
web page.  Only a few modifications were necessary, and it's only a
little pokey.

Oh, also!  The [Programming Language](http://catseye.tc/node/Programming%20Language) index has been redone to be a
bit more like the [Project Matrix](http://catseye.tc/node/Project%20Matrix).  It's a bit daunting, and awkward
still, but probably better than how it was organized previously.

### catseye.tc hosted on new servers

*   summary: [catseye.tc](http://catseye.tc/node/catseye.tc) is now hosted on new web servers.
*   date: Tue, 08 Oct 2013 21:09:16 GMT

"Here's a nickel, kid.  Get a real web hosting service."

So I did.

You should see few if any changes.  The ones you might see are:

*   `www.catseye.tc` is no longer an alias for `catseye.tc`, although
    I'll probably set up a redirect in the near future, maybe, if I
    get around to it.
*   Getting documentation (of esolangs, etc.) onto `catseye.tc` has
    always been a bit of a pain, and that fact hasn't changed, so only
    links to documentation on Github are given here for now.
*   On the plus side, URLs for Chrysoberyl nodes now look much nicer;
    you can use underscores instead of spaces, kind of like what
    Mediawiki does.  The old URLs will still work too, though.
*   The new servers are in Europe.  That may affect your latency.

Everything else should be pretty much as it was.  If you see anything
really broken, feel free to let me know.

### Some HTML5 gewgaws for y'all

*   summary: Several new [HTML5](http://catseye.tc/node/HTML5) gewgaws are now online in the [Gallery](http://catseye.tc/node/Online%20Installation).
*   date: Sun, 04 Aug 2013 03:00:00 GMT

In [a previous article](http://catseye.tc/node/Programming%20Languages%20as%20an%20Artistic%20Medium),
I mentioned that I consider, not just
[programming languages](http://catseye.tc/node/Programming%20Language), but also [HTML5](http://catseye.tc/node/HTML5),
an artistic medium.

If short, fluffy, entertaining pieces of music are called
[bagatelles](http://en.wikipedia.org/wiki/Bagatelle_%28music%29),
then I propose that short fluffy works in the medium of HTML5 be
called [gewgaws](http://www.thefreedictionary.com/gewgaw).  Or at
least, that's what I call them.
        
And so, here are a few HTML5 gewgaws for your (possible) entertainment.
Located in the Digital Art Exhibit of our
[Gallery](http://catseye.tc/node/Online%20Installation).  In fact there are six new ones in
total.  And when I say HTML5, I mainly mean the `<canvas>` stuff, of
course.

They're not esolangs, but if you like esolangs, or if you liked
[Cyclobots](http://catseye.tc/node/Cyclobots), you might like some of the more mathematically-oriented
ones.

### I'd been meaning to re-implement this for ages

*   summary: Our 1994 automaton [Cyclobots](http://catseye.tc/node/Cyclobots) is now [live in-browser](http://catseye.tc/installation/Cyclobots) in the [Gallery](http://catseye.tc/node/Online%20Installation).
*   date: Fri, 12 Apr 2013 09:26:41 GMT

Turn back the clock.  It's 1994.  NAFTA.  OJ Simpson.  Rwanda.
And [SMETANA](http://catseye.tc/node/SMETANA), implemented for the first time in [Visual Basic](http://catseye.tc/node/Visual%20Basic).

And, unseen by all but maybe three or four people, [Cyclobots](http://catseye.tc/node/Cyclobots).

Also implemented in Visual Basic.  Described as an "interactive
desktop toy".  Fun to watch.  Languished in obscurity because I
had other interests at the time.

Then, the Visual Basic programs were forgotten, and eventually [lost](http://catseye.tc/node/lost).
When Java came on the scene, I had meant to re-implement it as an applet.
But man, that must have been one *low* priority TODO item, because I
never got around to it.

[Until now](http://catseye.tc/installation/Cyclobots).

'Course, it's not a Java applet now, it's [Javascript](http://catseye.tc/node/Javascript) on an [HTML5](http://catseye.tc/node/HTML5)
canvas, so make sure you're using one of those awesome new
cutting-edge browsers, i.e., you've updated your Interwebs Explorer
recently.

If you enjoyed watching what happens when you click "Revolution!" —
and I mean *really* enjoyed it — feel free to show your appreciation
by tossing a quarter into
[this here empty guitar case](https://www.gittip.com/catseye/).

### An Online Parade of Cellular Automata

*   summary: Our five [ALPACA](http://catseye.tc/node/ALPACA) creations are now online in the [Gallery](http://catseye.tc/node/Online%20Installation).
*   date: Sat, 06 Apr 2013 12:08:26 GMT

It's about time!  You can now play with Cat's Eye Technologies'
cellular automata in your web browser on the following pages:
[REDGREEN](http://catseye.tc/installation/REDGREEN), [Circute](http://catseye.tc/installation/Circute), [Braktif](http://catseye.tc/installation/Braktif),
[Jaccia](http://catseye.tc/installation/Jaccia), and [Jacciata](http://catseye.tc/installation/Jacciata).

I've wanted to be able to generate some kind of usable-in-a-web-browser
code from [ALPACA](http://catseye.tc/node/ALPACA) descriptions for a good long while.  At one point
I even considered hacking [alpaca.pl](http://catseye.tc/node/alpaca.pl) to generate [yoob](http://catseye.tc/node/yoob) classes
to do it.  Well, the ALPACA language got a long-deserved update, and
[Perl](http://catseye.tc/node/Perl) gave way to [Python](http://catseye.tc/node/Python) for the new compiler; and yoob in
[Java](http://catseye.tc/node/Java) has given way to [yoob.js](http://catseye.tc/node/yoob.js) in [Javascript](http://catseye.tc/node/Javascript).

(In fact, there's nothing much HTML5-specific about these Javascript
implementations, except for a slider control for adjusting the animation
speed, which is kind of crude and subject to change anyway.)

The few improvements to yoob.js that were spurred on by this effort to
get these CA's online have also resulted in improvements to the
online installations of [Gemooy](http://catseye.tc/installation/Gemooy) and
[noit o' mnain worb](http://catseye.tc/installation/noit%20o%27%20mnain%20worb).

### noit o' mnain worb implemented in HTML5

*   summary: [noit o' mnain worb](http://catseye.tc/node/noit%20o%27%20mnain%20worb) has been implemented in [HTML5](http://catseye.tc/installation/noit%20o%27%20mnain%20worb).
*   date: Sat, 30 Mar 2013 18:34:22 GMT

The implementation of various things in HTML5 continues.  This
time it's [noit o' mnain worb](http://catseye.tc/node/noit%20o%27%20mnain%20worb), which you can play with
[here](http://catseye.tc/installation/noit%20o%27%20mnain%20worb).  With pretty graphics,
for some value of pretty.

Seeing as worb has already been implemented in [yoob](http://catseye.tc/node/yoob), why
do this?  It's not like I can say it's "now playable online", because
it already was.  (Or if not "playable", then... "play withable"...
or whatever.)

Well, the security track record for Java applets has been
rather awful lately.  Certainly, applets aren't going away, but they're
quickly falling out of fashion.  Updating your browser may,
reasonably, disable Java.  We may one day, not far off, see the JVM
stop being shipped with browsers, and available only as an add-on.

And that all means I have to tell you to install and/or enable Java in
your browser, which defeats the idea of reducing the install burden for
esolangs, which was one of the original goals of yoob.

The newer [yoob.js](http://catseye.tc/node/yoob.js) framework, which uses [HTML5](http://catseye.tc/node/HTML5) instead of Java,
is still pretty messy and ad-hoc, and lacks
a few things that would be nice to have, like adjustable animation
speed.  But the more things, like this, that get implemented in it, the
more it will mature.

### Super Wumpus Land now playable online

*   summary: [Super Wumpus Land](http://catseye.tc/node/Super%20Wumpus%20Land) is now [playable online](http://catseye.tc/installation/Super%20Wumpus%20Land).
*   date: Sun, 24 Mar 2013 12:28:33 GMT

[Super Wumpus Land](http://catseye.tc/node/Super%20Wumpus%20Land), our silly "extended dance mix" version of
[Hunt the Wumpus](http://catseye.tc/node/Hunt%20the%20Wumpus), has been converted to [Javascript](http://catseye.tc/node/Javascript), and is now
playable online here: [Super Wumpus Land](http://catseye.tc/installation/Super%20Wumpus%20Land).

This new implementation uses modules from [yoob.js](http://catseye.tc/node/yoob.js) to simulate
a text-based terminal on an [HTML5](http://catseye.tc/node/HTML5) `<canvas>` element.

### Oops, I just turned Chrysoberyl into a blogging platform

*   summary: Oops, I just turned [Chrysoberyl](http://catseye.tc/node/Chrysoberyl) into a blogging platform.
*   date: Wed, 20 Mar 2013 14:59:21 GMT

I'm not much of a blogger.  I've considered starting a blog a few times,
but the thing is, most blogs are either about trends or opinions
(or both, combined: _reactions_), and I don't follow trends, and when I
have opinions, they're about specific *things*.  (Which is why the old
[catseye.tc](http://catseye.tc/node/catseye.tc) had an "About" section, and why [Chrysoberyl](http://catseye.tc/node/Chrysoberyl) lets
commentary be attached to particular nodes.)  And those opinions, like
the things themselves, are relatively "evergreen" -- they're not news,
there's no need to go announcing them.  I also like to be able to
edit/tweak/update an opinion incrementally after writing it, which also
fits poorly with the blog model.  [EDIT: see what I mean?]

At the same time, I do generate news, if not trends, and these
announcements that I've implemented such-and-such or updated
such-and-such *are* news articles, even if they're short ones.

And sometimes I have something to say that's not focussed on a single
topic, and it fits best as a stand-alone article, such as 
[my retrospective on esolang design](http://catseye.tc/node/Retrospective%3A%20Chris%20Pressey%20on%20Language%20Design).

Therefore, I merged the concepts of "News Item" and "Article" into
just [Article](http://catseye.tc/node/Article) in Chrysoberyl, and all articles get included in
the Atom feed, whether they're explicitly "news" or not.  The result
is that Chrysoberyl is, among all the other words that already don't
describe it, now a blogging platform.

That's not to say you'll be seeing a lot of blog posts in the news feed.
Even this article, which I consciously tried to write like a blog post,
is still really mostly an announcement.

But you might see some.  You totally might.  Yeah, you're totally going
to hear every little nitpick I have about why the latest version of
Gadget X (resp. Language X) sucks and why GadgetCorp (resp. the Language
X community) is going totally off-course as a company (resp. open-source
project).  Because that's so totally the kind of thing I give a crap
about.

### ALPACA turns 1.0

*   date: Fri, 15 Mar 2013 18:00:00 GMT

We have finally released version 1.0 of [ALPACA](http://catseye.tc/node/ALPACA),
A Language for the Pithy Articulation of Cellular Automata.

The specification has been rewritten (although _written_ would be
more accurate) from scratch, and adds some new features to the language,
such as being able to include an initial configuration in an ALPACA
description, and handling neighbourhoods other than the Moore
neighbourhood.

The reference implementation has also been rewritten from scratch,
in [Python](http://catseye.tc/node/Python) this time.  It can both interpret an ALPACA description,
and compile it to [Javascript](http://catseye.tc/node/Javascript).  We plan to use the latter functionality
to showcase some cellular automata on the website, which incidentally is
looking a little less dire these days.

The version bump also cures two unpleasantnesses which are pet peeves
of mine: ALPACA is no longer hanging out at version 0 (which sets it
apart from, say, `node.js`), and the meaningless version numbers like
0.94 are now history.  (It's not like it was the ninety-fourth iteration
of anything.)

### First language release of 2013: Exanoke

*   date: Sat, 05 Jan 2013 11:18:23 GMT

We have released [Exanoke](http://catseye.tc/node/Exanoke), a pure functional
language which is syntactically restricted to expressing the primitive
recursive functions.

If this doesn't sound like a stellar achievement, it's probably because
it's not one.  But, I was previously aware of only how an imperative
language could be restricted to primitive recursion (i.e. have only `for`
loops) and previously did some work on analyzing functions in a
pure functional language to determine if they are primitive recursive
or not; in a way, Exanoke combines both of those ideas.

### Chrysoberyl is now in BETA

*   date: Fri, 04 Jan 2013 14:17:00 GMT

Happy 2013!  [Chrysoberyl](http://catseye.tc/node/Chrysoberyl) is now in beta, whatever
that means in this day and age where it's not considered absurd for
web services to be in perpetual beta.

Well, concretely, what it means is we've replaced the older parts of
`[catseye.tc](http://catseye.tc/node/catseye.tc)` entirely with Chrysoberyl entries, with a lot of web
redirects so all those links out in the wild still work.

What it doesn't mean is that Chrysoberyl is finished in any sense.
Its content will of course continue to evolve, and it will likely be a
while before we are entirely happy with its structure and styling (so
expect these to change in the near future.)

### Language, Language, Implementation, Bug fix, Bug fix

*   date: Mon, 17 Sep 2012 22:13:56 GMT

So yeah, let's catch up with all the exciting, exciting
*non*-Chrysoberyl-related developments we've seen here in the past few days!

First, please welcome our latest newcomer to the menagerie,
[Jolverine](http://catseye.tc/node/Jolverine).  I haven't been able to write a loop in it yet, but
<a class="external" href="http://esolangs.org/wiki/Talk:Jolverine">Ørjan
is figuring that part out</a>.

Second, I remembered why I designed [Etcha](http://catseye.tc/node/Etcha) — it was part of a
larger, stranger, maze-based automaton called [Zame](http://catseye.tc/node/Zame).  Which is now
described on the esowiki.

Third, I finally got around to implementing [Thue](http://catseye.tc/node/Thue).  In [Ruby](http://catseye.tc/node/Ruby).
I've been maintaining a distribution of it for so long without contributing
to it, I felt it was overdue.  And now there is a new release of the
Thue distribution.

Fourth, Keymaker reported a bug with in [smith.pl](http://catseye.tc/node/smith.pl) — and while fixing
it, I found another fixed that one too, and there has been another release
of the [SMITH](http://catseye.tc/node/SMITH) distribution.

Lastly, while implementing a truth-machine in [Ypsilax](http://catseye.tc/node/Ypsilax) I found a bug
in [ypsilax.pl](http://catseye.tc/node/ypsilax.pl) too (turns out, in [Perl](http://catseye.tc/node/Perl), the *string* `'0'` is false-y.
It's things like that why I don't code in Perl much anymore.)  So there's
a new release of the [Ypsilax](http://catseye.tc/node/Ypsilax) distribution too.

### Dungeons of Ekileugor: 3,221 bytes of roguelike

*   date: Sun, 16 Sep 2012 05:04:44 GMT

Have you ever wondered how much roguelike can
be crammed into the 3583 bytes available to BASIC on an unexpanded
[Commodore VIC-20](http://catseye.tc/node/Commodore%20VIC-20)?  Well wonder no more, for [Dungeons of Ekileugor](http://catseye.tc/node/Dungeons%20of%20Ekileugor)
is such a cramming.  Random dungeon level generation with
fairly reasonable layout of rooms and tunnels, monsters, combat with
hit points and experience points, queued messages, treasure, chests,
traps, potions — it's quite a respectable set of "dungeon furniture"
considering the platform, we think.  Fire up your emulator (or, bless
you, a real VIC-20) and try it out!

### Chrysoberyl is now in ALPHA

*   news-link: http://catseye.tc/node/Chrysoberyl.html
*   date: Sun, 16 Sep 2012 01:44:35 GMT

Remember "The Great DVCS Exodus"
(May 20, 2012)?  (Well, if you don't, scroll down.)
I am happy to say that it is, for all intents and purposes,
complete: essentially all of our stuff is now in repositories on
<a class="external" href="https://bitbucket.org/catseye">Bitbucket</a>
and
<a class="external" href="https://github.com/catseye">GitHub</a>.

And remember how I said that the role of catseye.tc might
change in light of this, but that I wasn't sure how?  Well, here's
the deal.  We have put together a database of sorts of all the
things Cat's Eye Technologies has produced, and many of the
things directly related to the things Cat's Eye Technologies has
produced, and how they all relate, called _Chrysoberyl_.

I like to think of it as a sort of cross between a wiki and a semantic web
and _The Devil's Dictionary_.
It teases apart the relationships between programming languages
(and other intangibles), implementations (things you can
run), and distributions (things you can download), and casts it all in
a bunch of YAML files with embedded Markdown.
From these, a set of HTML5 pages can be generated, and lo and behold,
[these are now on the site](http://catseye.tc/node/Chrysoberyl).

They are, however, still in a very early stage of development.  Expect
the styling to change, the content to change, the structure to change,
links to break, and the usual sort of thing.

This has a few implications for the rest of the site.  The Gallery Space will
stay more-or-less as it is for a while, but the Projects Space
and the "About" documents will eventually go away, and will redirect into
Chrysoberyl instead.  In the meantime, they will likely *not* be
updated to reflect the latest developments.  Look at Chrysoberyl, or our repositories
on Bitbucket and Github, instead, if you want to follow those.

And, more importantly for you (if you are reading this from our RSS feed)
is that our RSS feed *will no longer be updated*.  This will probably
be the last item in it, except for an "Are you still reading this?" item when we've switched
entirely over to Chrysoberyl.  Instead, you will want to subscribe to
<a href="http://catseye.tc/feeds/atom_15_news.xml">our new Atom feed for
news, generated from Chrysoberyl</a>.

### Cfluviurrh: an Esolang with Feeling (Literally)

*   news-link: http://catseye.tc/projects/cfluviurrh/
*   date: Sun, 26 Aug 2012 17:43:52 GMT

We have released a new programming language.
It's called Cfluviurrh.  It was designed for writing programs that
can *feel*.  That is, defines a mechanism by which
a program can be instructed to experience particular emotions.
You might, thus, on first blush, consider Cfluviurrh to be
unimplementable, as modern-day computers are not capable of
experiencing emotions (you guess.)  However, this is demonstrably
untrue, and the Cfluviurrh reference interpreter demonstrates it.

### The NEW Befunge-93 Reference Distribution

*   news-link: http://catseye.tc/projects/befunge-93/
*   date: Sat, 25 Aug 2012 17:58:39 GMT

Since `bef`
is the reference implementation of Befunge-93, or at least I've
been calling it that, and since we've decided more or less
that packaging all reference materials for a language into a
"reference distribution" is the way to go, the bef and befunge93
distributions have been merged into a single, NEW distribution
called "befunge-93".  Also included are a couple of new example
programs, a Makefile, and a small feature fix to the debugger.  Enjoy!

### One More Language: Hello, Velo

*   news-link: http://catseye.tc/projects/velo/
*   date: Sat, 14 Jul 2012 20:58:15 GMT

And when we do get rid of a language, we like
to introduce another language to keep our numbers up.  Enter
Velo, a vaguely Ruby-inspired scripting language which unifies
strings with code blocks, and scripts with object classes.
It's by no means final or complete, but enough of it is there that
it feels like it's been "invented", so here it is — expect it to
change in minor (but backwards-incompatible) ways in the
future, though.

### One Less Language: Farewell 2iota

*   news-link: http://catseye.tc/projects/beta-juliet/
*   date: Sat, 14 Jul 2012 18:36:52 GMT

It's not often we get rid of a language here at
Cat's Eye Technologies, but it happens occasionally.  In fact,
it happened today.  I decided, some time back, that the languages
beta-Juliet and 2iota were simply too similar to be distinct
languages; and so, 2iota was absorbed into β-Juliet version 2.0
(which we can spell with the Greek letter now that everybody's
got their Unicode boots on, right?)  The semantics of the language
have also been clarified somewhat (although the reference
interpreter still needs to catch up to them in some small ways.)

### yucca: Static Analysis for BASIC

*   news-link: http://catseye.tc/projects/yucca/
*   date: Mon, 11 Jun 2012 04:13:52 GMT

We have officially released version 1.0 of
`yucca`, a static analyzer for 8-bit
BASIC programs.  `yucca` can find those
places in your program where you jump to a line number that
doesn't exist, and a modest assortment of other things.  It
graciously ignores statements that it doesn't know anything
about, allowing it to be dialect-agnostic.  It has been used
on our BASIC offerings (all two of them) and did, indeed, find
[a useless jump in Apple Befunge](https://github.com/catseye/Apple-Befunge/commit/ba4319011ccbac2041f0a6a9ec5cadae91483906).

### Bubble Escape now open-source

*   news-link: http://catseye.tc/projects/bubble-escape/
*   date: Sun, 03 Jun 2012 16:46:56 GMT

A new revision of the Bubble Escape distribution has been
released.  It contains all three versions of Bubble Escape: the 2009
Mini Game Competition winner (2K), an 8K cartridge image based on that
source, and the original version, written in BASIC, from the 80's.  What's
more, the source code for all versions is now included, and placed under
a BSD license.

### The Great DVCS Exodus

*   news-link: https://github.com/catseye/
*   date: Sun, 20 May 2012 21:41:02 GMT

Did you know that the catseye.tc website is statically
generated with a set of XSLT templates?  Well, it's true.
This has certain advantages — like, when was the last time you
saw broken XHTML on one of the project pages?  But it has
disadvantages, too.  Namely, it's becoming a pain to update.

Meanwhile, we've been putting more and more of our
projects under distributed version control.  We tend to use
[Mercurial](http://mercurial.selenic.com/) but
[hg-git](http://mercurial.selenic.com/wiki/HgGit)
provides a fairly seamless bridge to [git](http://git-scm.com/)
repositories, too.  And then there's these sites that host such repositories
for you, [Bitbucket](https://bitbucket.org/)
and [Github](https://github.com/) (among others).

So, we've been neglecting catseye.tc a bit lately, and have been
putting our projects onto Bitbucket
and GitHub, and making updates to them there.  There are certain advantages
to doing so.  For example, if you find a bug in one of our implementations,
you can fork that project, fix the bug, and even if Chris doesn't respond to your
pull request for three or four years, at least your fork will be out there and
available to anyone
else who might be interested.  On top of that, the source browsers on both
of these sites are better than anything we have the time to invest in putting on
this site.  (Besides, if we go the way of \_why, chances are some of
our projects will end up there anyway, so why not give them a head start?)

But no, this does not mean the end of catseye.tc.  I mean, we have
to keep it, or all our Java package hierarchies will be busted, right?  And I think
people are peeved enough over all the old links that are still around that lead
to all the old domain names Cat's Eye Technologies has used in the past — no
sense putting another one on that heap, if we can help it.  But the role of
catseye.tc might change somewhat.  I don't know yet.  We'll see.

Anyway, the point is: keep watching this space, but if you want
breaking updates on what kind of crazy crap we're working on
*this minute*, check out
[Cat's Eye Technologies on Bitbucket](https://bitbucket.org/catseye)
and/or
[Cat's Eye Technologies on Github](https://github.com/catseye).

### Some Facts Regarding Apple Befunge v1.1

*   news-link: http://catseye.tc/projects/apple-befunge/
*   date: Mon, 20 Feb 2012 17:44:01 GMT

Pixley and Falderal.  Falderal and Pixley.
I know, I know, it's all you've been hearing about for the past
three months, you poor thing.  But now, O eso-pilgrim, well
may you frolic and jubilate!  I bring news of something closer to
the weird.  After more than a decade, some well-deserved
updates have been made to Apple Befunge, that ol' "retrolanguage"
for the Apple ][+, and it has been placed in the public domain.

### I got Pixley power!

*   news-link: http://catseye.tc/projects/pixley/
*   date: Mon, 20 Feb 2012 01:12:15 GMT

Pixley version 2.0 revision 2012.0219 has been released.
There are no changes to the language, but there are a few significant
improvements to the supporting tools and tests, and a few to the
implementation, and a bevy of minor dialects of Pixley have been defined
for purposes of Scheme-ly tar-pit research.  Oh, and it's been officially
placed under a BSD-style license now.  Enjoy...

### Release of Falderal version 0.6 "Streeterville"

*   news-link: http://catseye.tc/projects/falderal/
*   date: Mon, 02 Jan 2012 14:45:16 GMT

The new year sees another release of
Falderal, our framework for writing literate test suites for
languages.  This version supports variable expansion in
functionality specifiers and the ability to add and remove
functionality specifiers on the command line.  It also fixes
several bugs and shortcomings in the previous version.
And, if you browse around the site a bit, you'll see
we've started using it to format our projects' Falderal,
Markdown, and Literate Haskell documents to XHTML.

### Release of Falderal version 0.5 "The Loop"

*   news-link: http://catseye.tc/projects/falderal/
*   date: Wed, 14 Dec 2011 14:40:19 GMT

Falderal, our format for unit-testing little
languages, has seen release of version 0.5 "The Loop".
As you can see, we have adopted a naming convention for
release milestones — they're named after Chicagoland
neigbourhoods, suburbs, landmarks, and institutions.
This version was named after The Loop in recognition of its
ability to shuttle test results between `falderal`
and the various results generators implemented in different languages
(Haskell, Bourne shell scripts) and to report on all the failures in
a consistent way.

### Release of Pixley version 2.0

*   news-link: http://catseye.tc/projects/pixley/
*   date: Fri, 09 Dec 2011 17:18:14 GMT

Pixley version 2.0 has been released.  It
removes `cadr` and `null?`
from the language.  Partly because of this, the reference interpreter is
now somewhat simpler: 124 lines of Pixley, with 407 instances of 53
unique symbols in 672 cons cells.  The distribution now also includes
driver shell scripts, Falderal tests, and a P-Normalizer, probably the
first non-trivial Pixley program to be written outside the Pixley interpreter
itself.

### Madison, a Term-Rewriting Proof-Checker

*   news-link: http://catseye.tc/projects/madison/
*   date: Fri, 02 Dec 2011 20:26:43 GMT

One thing I've wanted to do for a long while is
design a language in which one can state proofs of the properties
of programs in that language.  Not a full-blown theorem prover, just
a proof checker, where you have to supply the proof, and the
system tells you if it holds or doesn't hold.  And not an immensely
powerful proof-checker either, just powerful enough to state some
simple proofs which hold over an infinite universe of values.

Well, after much thought and sketching, I have come up with
a term-rewriting-based proof-checking language called Madison.  It
supports both direct proof and proof by structural induction, and I
have used it to write a proof that the reflection of the reflection
of any binary tree is the same as the original tree.  It's not much,
but I'm quite pleased with it.

### Q: Are We Not Men?  A: We Are Flobnar!

*   news-link: http://catseye.tc/projects/flobnar/
*   date: Fri, 28 Oct 2011 14:34:04 GMT

One day in September of 2011 — though I'm not
sure precisely which one — marked Befunge-93's 18th birthday.
That means that Befunge is now old enough to drink in its native
land of Canada.  To celebrate this, I thought I'd get Befunge-93 drunk
to see what would happen.

What happened was Flobnar, an esolang which is in many respects a
functional dual of Befunge-93; most of the symbols have analogous
meanings, but execution proceeds in a much more dataflow-like fashion.

### Release of Falderal version 0.4

*   news-link: http://catseye.tc/projects/falderal/
*   date: Mon, 10 Oct 2011 20:47:03 GMT

Well, that was quick — well,
we were on a roll.  Falderal 0.4 introduces several
desirable features.
`Test.Falderal` is a Cabal package now, making
installation easier, and this Cabal package installs
a tool (unflinchingly called `falderal`)
which drives the formatting and testing processes.
Tests are now targetted at abstractions called
_functionalities_, and
functionalities are allowed to be implemented in different ways,
including as shell commands, supporting the testing of multiple
implementations of a function in multiple, essentially arbitrary
implementation languages.  This all brings Falderal closer to
its goal of being a testing framework for programming languages.

### Release of Falderal version 0.3

*   news-link: http://catseye.tc/projects/falderal/
*   date: Fri, 07 Oct 2011 18:30:56 GMT

Remember that major change in
how Falderal works that we talked about when
Falderal 0.2 was released?  Well, it's here, in
Falderal 0.3.  Basically, two things happened.
One, Falderal is a file format now, and
`Test.Falderal`
is the reference implementation,
in Haskell, for tools which claim to understand the
format.  Two, `Test.Falderal`
is now able to format Falderal files into other formats.
In fact, running tests is accomplished by formatting
the Falderal file into Haskell code, and running that.

### OMG WTF FBBI 1.0 SIAS EVVK!

*   news-link: http://catseye.tc/projects/fbbi
*   date: Mon, 03 Oct 2011 20:46:30 GMT

After years and years of apathy, we have
fixed a number of bugs in the Flaming Bovine Befunge-98 Interpreter
(FBBI), raising its quality level from "profound embarrassment" all the
way to "marginal non-fail".  Mainly we did this by randomly applying
those patches that have been floating around, for which we owe much
gratitude, but there was also a crippling memory-management bug that
we found in the stack routines that highly deserved
being killed, so, we sure did that thing too.

To celebrate — and to assuage our acquired annoyance at
version numbers which look like decimal numbers that are supposed
to indicate "close to release" — we have released version 1.0 of FBBI.

Note well that our general apathy towards Funge-98
has not abated in kind.

### yoob 0.3 in the Gallery of Interactive Esolangs

*   news-link: http://catseye.tc/gallery/esolangs/
*   date: Wed, 21 Sep 2011 18:46:23 GMT

yoob 0.3 has been released, and it has moved out
of Cat's Eye Technologies' lab and has become an official part of our
website.  It is now the main exhibit in the new Gallery of
Interactive Esolangs.  And, since we have three galleries now, we have
developed this section of the website into something more real: our
[Gallery Space](http://catseye.tc/gallery/).
This is where we will be exhibiting interactive works, and works
not produced by Cat's Eye Technologies but which we find interesting
nonetheless.

### Have you seen LoUIE lately?

*   news-link: http://catseye.tc/cpressey/louie.html
*   date: Sat, 17 Sep 2011 21:24:45 GMT

Have you seen LoUIE (our List of Unfinished
Interesting Esolangs) lately? Because if you haven't, there's likely
some designs there you haven't seen, because I just now added
three (and in the past, haven't always announced it when I've
added new entries.)  There are twelve in total now, so if you're
looking for an idea to build on, why not give it a look-see?

### Researchers Discover the Civilization Advance "Language: Xoomonk"

*   news-link: http://catseye.tc/projects/xoomonk/
*   date: Sun, 07 Aug 2011 23:56:59 GMT

Xoomonk is a programming language in which
_malingering updatable stores_
are first-class objects.  Malingering updatable stores unify several language
constructs, including procedure activations, named parameters, and object-like
data structures.  While the language is not yet implemented or even
entirely finalized, it is pretty much complete, so is being released as
version 0.1.

### PL-{GOTO}.NET: Eat it Before it Eats You

*   news-link: http://catseye.tc/projects/pl-goto.net/
*   date: Fri, 05 Aug 2011 02:53:30 GMT

You've always wanted an compiler
for the example primitive recursive language PL-{GOTO}
from Brainerd and Landweber's _Theory of Computation_,
haven't you?  And you have a need for it to generate MSIL which
can be fed into `ilasm`to produce a .NET
executable, don't you?  And you wouldn't be satisfied unless it were
implemented in Haskell, with a true-to-form grammar parsed with a
Parsec combinator parser, would you?

...

Why aren't you answering me???

### Bubble Escape 2K Now Playable Online

*   news-link: http://catseye.tc/gallery/c64/bubble-escape-2k/
*   date: Sat, 16 Jul 2011 05:34:50 GMT

As subject.  We've wanted to do this for a
while, but last time an attempt was made,
[JaC64](http://jac64.sourceforge.net/)
was not quite up to the task.  So we
[forked it on Bitbucket](https://bitbucket.org/catseye/jac64/)
and for the past few weeks we've been busy fixing bugs in it.
It's still not perfect, but it's playable on several
platforms including Windows (Firefox and IE)
and Ubuntu 11 (Firefox).  So try it!  Enjoy!

### Release of Falderal version 0.2

*   news-link: http://catseye.tc/projects/falderal/
*   date: Mon, 27 Jun 2011 18:40:47 GMT

Mainly to get a few minor niceties
and bugfixes out of the way before we start on
major changes to how Falderal works, Falderal 0.2
has been released.  The planned major changes are
probably more interesting than the niceties: I hope
to make Falderal into something that can test more
than just Haskell functions.  Of course, it will still
be written in Haskell.

### First public release of yoob source code

*   news-link: http://catseye.tc/projects/yoob/
*   date: Fri, 24 Jun 2011 04:27:27 GMT

yoob has pulled itself out of its
"technology preview" stage, and is officially released
as open-source software.  More specifically, its source
code is in the public domain and its development is
hosted on a
[public repository](https://bitbucket.org/catseye/yoob)
on Bitbucket.  Even though the source code is
embarrasingly bad, I decided not to care.  If you decide
to care, you are quite free to hack it into better shape --
there are more than a dozen open issues in its
[issue tracker](https://bitbucket.org/catseye/yoob/issues).

### Corona: Realm of Magic: Dug out of the Attic

*   news-link: http://catseye.tc/projects/corona-realm-of-magic/
*   date: Fri, 24 Jun 2011 00:17:55 GMT

Something else I dug out of the attic.  This was
an elaborate roguelike I wrote (but never finished) in Perl,
circa 2000. Still runs on a modern Perl (v5.10.1), but doesn't
play too nicely with my modern terminal emulator. No further
development is planned — it is retained here for historical
interest only.  It's actually been on the site for a while, but
due to some technical problems, was not announced until now.

### Apple Befunge: Dug out of the Attic

*   news-link: http://catseye.tc/projects/apple-befunge/
*   date: Tue, 07 Jun 2011 19:47:35 GMT

Hey, look what I dug out of the attic.  I don't even
remember what emulator the disk image was built for.  Oh well.

### Pail is an acceptable Bizaaro[sic]-Pixley

*   news-link: http://catseye.tc/projects/pail/
*   date: Fri, 27 May 2011 14:33:34 GMT

If you've been following our news,
you've noticed that twenty-eleven's been kind of a
light year for new languages here at Cat's Eye Technologies.
It's been mostly updates, with the only original design
being Wunnel.  Well, that pattern's been broke!
We have another new language.  It started its life
under the name Bizaaro[sic]-[Pixley](http://catseye.tc/node/Pixley),
but it's called Pail now (for PAIr Language).

### Falderal: Literate Testing for Haskell Functions

*   news-link: http://catseye.tc/projects/falderal/
*   date: Tue, 17 May 2011 23:43:10 GMT

We here at Cat's Eye Technologies
have decided to stop building new ad-hoc test suite
machinery for every new esolang we implement in
Haskell.  Instead, we have put together a package
that can be used and reused for this purpose, and
we have (for reasons obscure even to us) called it
Falderal.  It doesn't do a lot yet (it's only version 0.1...), but it has promise.
We're already using it in [Quylthulg](http://catseye.tc/node/Quylthulg).
To encourage contributions, its development is hosted on a
[public repository on Bitbucket](https://bitbucket.org/catseye/falderal).
Watch for its use in future projects!

### Pluggin' some (specification) leaks in Eightebed

*   news-link: http://catseye.tc/projects/eightebed/
*   date: Tue, 10 May 2011 18:59:22 GMT

Eightebed version 1.1.  Has a nice ring to
it, doesn't it?  Kind of mellow, with hints of
strawberry and creosote on the back of the tongue.
And that ring is even nicer when you
realize that this update fixes the definition of the language to
make it fulfill its original purpose.  The concept of
the _safe area_ has been limited
to statements in a block before the first `free`
statement, thus preventing the creation of aliased
dangling references.  Thanks to Gregor Richards for
pointing out this hole.  Also included: a handful of bug
and documentation of fixes that you don't care about.

### Oozlybub and Murphy and Progress!

*   news-link: http://catseye.tc/projects/oozlybub-and-murphy/
*   date: Wed, 27 Apr 2011 19:37:55 GMT

Version 1.1 of the Oozlybub and Murphy
programming language has been released.  This update
tries to clarify some of the errors in the specification while
also slathering some extra goo onto it like a wimpmode.
Enjoy, then enjoy again, then PLEASE DO KEEP ENJOYING
UNTIL YOUR EYES BURN WITH DEEP DEEP CORROSION.

### More blowing off of dust: Maentwrog

*   news-link: http://catseye.tc/projects/maentw/
*   date: Tue, 26 Apr 2011 18:00:57 GMT

Marinus has been so kind to write
documentation and example programs for the
ancient and venerable Maentwrog language that
I decided I ought to update the distribution to
include them — along with a small fix that allows the
source to be build with modern C compilers like
gcc and pcc.

### yoob Grows Support for 3 More Esolangs

*   news-link: http://catseye.tc/lab/yoob/applet.html
*   date: Wed, 30 Mar 2011 23:37:49 GMT

The yoob framework for esolang
implementations has seen many minor improvements,
and has had three more esolangs implemented for it.
Two of these, Befunge-93 and brainfuck, are languages
that no mega-eso-interpreter should be without; the
third is Ypsilax, which was implemented in a relatively
efficient manner (far more so than the existing implementation)
to vet yoob's pattern-matching support.

None of these esolang implementations is
particularly refined; each has some shortcomings w.r.t.
the framework, and probably some bugs too.  I expect
they'll ripen with age.  Enjoy...

### Blowing the Dust off bef

*   news-link: http://catseye.tc/projects/bef/
*   date: Sat, 19 Mar 2011 05:49:00 GMT

The Befunge-93 reference interpreter,
after a long period of inactivity, has been updated to
version 2.22.  This fixes three bugs, shortcomings,
features, call them what you will: EOF characters are
no longer written into the playfield when loading an
otherwise blank source file (thanks to whoever sent
me that patch six-odd years ago, and sorry that I have
no recollection who you are); long source file lines
are truncated instead of wrapping around to the next
playfield line (this lets bef load mycology.b98 correctly);
and the # instruction now behaves consistently when
combined with wrapping (i.e. when it occurs at the
very edge of the playfield.)  All this and some minor
aesthetic improvements to the interpreter, too!

### Technology preview: yoob

*   news-link: http://catseye.tc/lab/yoob/applet.html
*   date: Tue, 15 Mar 2011 17:48:27 GMT

Cat's Eye Technologies has embarked
on an ambitious project: build a framework which both
reduces the effort to implement esolangs, and makes
those implementations easily accessible to, and usable
by, anyone with a modern web browser — even
non-programmers.

The project is called yoob.  Even though it
is still in an early stage of development, already
more than ten esolangs have been implemented in it.
And you can certainly expect more in the future.
Enjoy...

### We Three Things of Disorient Are

*   news-link: http://catseye.tc/cpressey/lingography.html#Gemooy
*   date: Tue, 04 Jan 2011 14:23:23 GMT

Alright, so it's a little late, I admit, but
puns of that quality take time!  We present three
remotely fungeoid little esolangs
that, in fact, *were* designed before Christmas:
[Gemooy](http://catseye.tc/node/Gemooy), [Nhohnhehr](http://catseye.tc/node/Nhohnhehr), and [Kelxquoia](http://catseye.tc/node/Kelxquoia).
They're not in our project space yet, but they are on the
esolang wiki, and one of them (Nhohnhehr) has an
implementation already, thanks to Marinus.

So, take a gander at 'em, and you'll be saying,
"Hey Chris, where'd you get your programming language
designer's license?  A cereal box?"

Actually, that'd be a pretty cool breakfast cereal,
to have a prize like that...

### Refurbishment of Thue Implementations

*   news-link: http://catseye.tc/projects/thue/
*   date: Sat, 18 Dec 2010 21:33:39 GMT

We've released a couple of bugfixes
and some general modernization to the implementations
of the Thue language included in our Thue distribution.
Thanks to Nathan Thern for the bug report that spurred
on this effort!

### Fresh, Bold Stupid: Oozlybub and Murphy

*   news-link: http://catseye.tc/projects/oozlybub-and-murphy/
*   date: Wed, 01 Dec 2010 04:02:32 GMT

Cat's Eye Technologies has
developed a new programming language. The name of this
language is Oozlybub and Murphy. Despite appearances,
this name refers to a single language. The majority of the
language is named Oozlybub. The fact that the language
is not entirely named Oozlybub is named Murphy. Deal with it.

### Pixley Version One Point One

*   news-link: http://catseye.tc/projects/pixley/
*   date: Fri, 05 Nov 2010 21:11:25 GMT

An update to the Pixley programming
language has been made, version 1.1, which fixes a problem
where the reference implementation (and thus, for better or
worse, the language definition) was not preserving
the disjointedness of types.  A lot of goodies have also been
added to the distribution, including a more complete test
suite, a REPL, a statistics generator, and an implementation
in Mini-Scheme.

### A Programming Language called Eightebed

*   news-link: http://catseye.tc/projects/eightebed/
*   date: Wed, 01 Sep 2010 22:56:25 GMT

I could have just explained to Gregor
why he was mistaken, but _noooo_,
I had to go and design an entire _language_
to make my point.  And I had to go and name it
"Eightebed", too!

### Whothm, a Language for Infinite Drawings

*   news-link: http://catseye.tc/projects/whothm/
*   date: Tue, 29 Jun 2010 22:44:31 GMT

We present Whothm, a simple language for
describing infinite two-colour bitmaps.  You can try it out
in your web browser with JWhothm, an implementation of
Whothm in a Java applet.

### Burro Climbs to 2.0

*   news-link: http://catseye.tc/projects/burro/
*   date: Mon, 07 Jun 2010 19:13:58 GMT

A major overhaul was done to the Burro language,
resulting in version 2.0.  Whatever Burro 1.0 might have achieved,
it _wasn't_ its primary goal.  As Alex Smith was
kind enough to point out, the set of Burro 1.0 programs don't
actually form a group.

Burro 2.0 fixes the design of the language to avoid the
problem.  It is defined as an executable semantics written in
Literate Haskell/Markdown which includes both a proof that Burro
2.0 programs form a group, and a demonstration of how one can
map a Turing machine to a Burro program.

### A video game: Bubble Escape 2K

*   news-link: http://catseye.tc/projects/bescape2k/
*   date: Wed, 12 May 2010 03:03:58 GMT

Wow!  A tiny C64 video game from the deep past!
Actually, this was released almost a year ago, when it
was submitted to the Mini Game Competition 2009,
where it won first prize in its class.  I decided to host it
here given the undecided nature of the future of the
minigamecomp.org.uk site.

We humbly think you should get out your Commodore 64 emulator and play it!

### Gallery of Esteemed Programming Languages

*   news-link: http://catseye.tc/gallery/languages/
*   date: Fri, 30 Apr 2010 20:13:55 GMT

At Cat's Eye Technologies, we have long
beheld a few programming languages as exceptionally worth
persual and appreciation, despite the fact that they have no
implementations, are not under active development, and were
not designed by Chris Pressey (or at least, you can't prove it.)
We have, until recently, hosted these in our projects space.
However, because of the criteria listed in the first sentence,
we decided that these aren't really "projects" in any good sense,
and we resolved to establish a distinguished display case for
these beauties on this website.

And here it is – the Gallery of Esteemed Programming Languages.

The past few days have also seen a flurry of extremely
minor updates to many of our projects, mostly to fix small
conformancy issues, such as making the documentation validate
as XHTML 1.0 Strict.

### Another blast from the past: RUBE

*   news-link: http://catseye.tc/projects/rube/
*   date: Thu, 04 Feb 2010 16:26:47 GMT

In a move likely to set a dangerous
precedent for retrotechnology maintenance,
Cat's Eye Technologies today released a
new version of the RUBE programming language,
the first such update in over twelve years.
"Actually 1.3 is exactly the same language as 1.02,
but I couldn't stand that meaningless zero anymore,"
Chris Pressey, a spokesman for the company, stated
at a fictional news conference.  "At least I finally got around
to getting the implementation to compile under something
besides Borland C++."

None of Mr. Pressey's livestock were available
for comment.

### ZOWIE: Memory-Mapped Structured Flow Control

*   news-link: http://catseye.tc/projects/zowie/
*   date: Tue, 29 Dec 2009 21:14:00 GMT

Cat's Eye Technologies' last language of the aughts,
ZOWIE, goes to press.  ZOWIE is a machine-like language, somewhat
echoing SMITH in syntax, where flow control is both structured (as in
structured programming) and memory-mapped (as in you write to memory
to indicate the start, and the end, of each loop.)

Also, I can now say I've worked on a language project for every
letter of the Roman alphabet.  I'm so happy.

### Release of Etcha, a Turtle-Based Language

*   news-link: http://catseye.tc/projects/etcha/
*   date: Sun, 04 Oct 2009 17:57:05 GMT

We present the esolang Etcha, a four-instruction BitChanger
descendant with a two-dimensional storage model based on turtle graphics.  Unlike the
turtle in LOGO however, the turtle in Etcha is an integral part of the
computation, playing a role similar to the tape head of a Turing machine.

### Dieter: Type Qualifiers meet Modules

*   news-link: http://catseye.tc/projects/dieter/
*   date: Sun, 04 Oct 2009 01:00:31 GMT

After a long long time incubating, the Dieter
programming language is released.  Dieter (that's Dieter as in the
German masculine given name Dieter, not dieter as in "one who diets")
conflates _type qualifiers_ with _modules_.
The article describes how the interaction between these two features
produces something that resembles object-oriented programming.

### The Pixley Programming Language Arrives

*   news-link: http://catseye.tc/projects/pixley/
*   date: Sat, 02 May 2009 03:23:46 GMT

We present Pixley, a strict subset of
R5RS Scheme.  Pixley supports four
datatypes (boolean, cons cell, function, and symbol) and
a dozen built-in symbols.  The Pixley reference interpreter
is highly meta-circular, being written in 140 lines of Pixley
(or, if you prefer, 140 lines of Scheme.)

Pixley is also (depending on how you count them)
my 50th programming language (that I'll admit to!)  This puts
me squarely in the ballpark of [Wouter](http://strlen.com/proglang/)
and [Aaron](http://esoteric.voxelperfect.net/wiki/User:Zzo38),
and suggests that I plan to be *personally* responsible for a significant
fraction of
[the next 700 programming languages](http://ttic.uchicago.edu/~blume/classes/aut2008/proglang/papers/Landin-next-700.pdf).

### Scientific Proof that Cellular Automata are Intelligent!

*   news-link: http://catseye.tc/projects/jaccia/
*   date: Sun, 12 Apr 2009 01:23:46 GMT

Did you know that
[slime molds are intelligent because they can solve mazes](http://web.archive.org/web/20020220163303/http://www.riken.go.jp/lab-www/frontier-div/NEWSLETTER/feb2001/ameboid_e.htm)?
Well it's true, because a scientist said it!
And now, since Cat's Eye Technologies has designed a pair of cellular automata (called Jaccia and Jacciata) that can solve mazes,
we know that cellular automata are intelligent too!  Three cheers for science!

### The Unlikely Programming Language Unveiled

*   news-link: http://catseye.tc/projects/unlikely/
*   date: Sun, 15 Mar 2009 21:20:50 GMT

So we have our first new programming language
of the year (or the overwhelming majority of it, anyway.)  It's called
Unlikely and it conflates objects with continuations, exposes its
program structures as classes with commensurate inheritance
relationships, and to top it all off, makes dependency injection
*mandatory*.  Overall a pretty painful experience, we think.

### Shelta Revisited

*   news-link: http://catseye.tc/projects/shelta/
*   date: Sun, 08 Mar 2009 19:00:30 GMT

Almost a decade after it was first published,
the assembly-language version of the Shelta compiler has been
translated to NASM.  In the process it was improved so that
it is *both* smaller than 512 bytes in size
*and* able to participate in the bootstrap
process.  Check it out (if you like that sort of thing.)

### A List of Unfinished Interesting Esolangs (LoUIE)

*   news-link: http://catseye.tc/cpressey/louie.html
*   date: Wed, 13 Jan 2009 04:06:22 GMT

Wouldn't it be great if I had enough time to
pursue every interesting idea for every yet-another-esolang I had?  Well,
that's simply not possible.  They have leaked out into LoUIE, a
List of Unfinished Interesting Esolangs, so that other esolang
designers may possibly some day take up the torch.  (And,
considering their recidivist tendencies, probably commit arson
with it.  Just you watch.)

### Nine Projects Moved to Archive

*   news-link: http://catseye.tc/archive/
*   date: Sun, 11 Jan 2009 23:06:29 GMT

We've moved nine of our less exciting projects to
an archive area of the website, where they can bit-rot in peace.
Their distfiles are still available for download, but their project pages
will not be maintained.  A good number of these are forks and ports of
open-source projects started by others (ErlGTK, ErlGuten, libvesa.)

### Let's Have a Warm Hand for Quylthulg

*   news-link: http://catseye.tc/projects/quylthulg/
*   date: Sun, 07 Dec 2008 02:32:51 GMT

Let's have a warm hand for Quylthulg,
the latest atrocity to escape from Cat's Eye Technologies'
labs.  Quylthulg is a programming language with but a single
control-flow construct: `foreach`.  In fact, it
does also have a `goto`, but that can only appear
inside data structures.

### Publishing of the "Kitsilano" Oscillator Circuit

*   news-link: http://catseye.tc/projects/kitsilano/
*   date: Sat, 06 Sep 2008 06:58:13 GMT

After a summer hiatus, production
resumes at Cat's Eye Technologies with the publishing of
the schematic of and story behind
'Kitsilano', an electronic oscillator circuit based on a pair
of NPN transistors and a single capacitor.

### Release of the Context Rewriting Language Treacle

*   news-link: http://catseye.tc/projects/treacle/
*   date: Sat, 12 Apr 2008 23:24:55 GMT

The Treacle programming language, successor
to Arboretuum, has been released.  It is based on context
rewriting, which generalizes forest-rewriting; names and variables
are separate, and patterns may contain holes inside which
subpatterns may match at any depth.

### Wee Present: The PETulant Cursor

*   news-link: http://catseye.tc/projects/petulant/
*   date: Wed, 02 Apr 2008 07:59:59 GMT

Just in time for April Fools,
Cat's Eye Technologies presents _The PETulant Cursor_,
a tiny (just 44 bytes!) "display hack" for the Commodore 64.
What's it do?  Run it and see!

### Arboretuum Forest-Rewriting Language Released

*   news-link: http://catseye.tc/projects/arboretuum/
*   date: Wed, 05 Mar 2008 06:46:13 GMT

The Arboretuum programming language has
been released.  It is based on forest-rewriting, which, as
the name suggests, is an extension of tree-rewriting in
which multiple trees are rewritten simultaneously.

### Website Updated to Use XHTML 1.0

*   news-link: http://catseye.tc/about/website.html
*   date: Fri, 01 Feb 2008 03:26:31 GMT

We have updated our webpages to conform to
the W3C Recommendation XHTML 1.0.  (This does not, however,
apply to HTML documentation in projects.)  The CSS has also
been cleaned up significantly, and the site generally looks
better in Internet Explorer.

### Release of the Larabee Programming Language

*   news-link: http://catseye.tc/projects/larabee/
*   date: Fri, 11 Jan 2008 03:20:00 GMT

The Larabee programming language has been released.
Larabee borrows the notion of branch prediction from computer
architecture, and abuses it to create a state of total despair.
Also great fun at parties.

### Release of the Mascarpone Programming Language

*   news-link: http://catseye.tc/projects/mascarpone/
*   date: Sun, 09 Dec 2007 02:01:55 GMT

The Mascarpone programming language has been released.
Mascarpone is a rationalization and further exploration of some of the
ideas behind Emmental.  Mascarpone is a self-modifying language, defined by
a meta-circular interpreter, in which interpreters are also first-class values.

### Ypsilax Updated to Use Console::Virtual

*   news-link: http://catseye.tc/projects/ypsilax/
*   date: Sun, 02 Dec 2007 17:40:07 GMT

Following the improvements made to the
implementation of [noit o' mnain worb](http://catseye.tc/node/noit%20o%27%20mnain%20worb),
our Ypsilax implementation also uses [Console::Virtual](http://catseye.tc/node/Console%3A%3AVirtual) and
optional sub-second delays to provide a nice screen-oriented
animation of Ypsilax' two-dimensional, non-deterministic,
reflective grid rewriting, taking the burden of visualization
off the user.

### RSS Feed Now Available for Cat's Eye Technologies

*   news-link: http://catseye.tc/news.xml
*   date: Sat, 01 Dec 2007 23:09:50 GMT

News on the latest developments at Cat's Eye Technologies
is now available as an RSS feed.  The [news page](/news.html)
is still available, but it is now automatically generated from the RSS feed by
an XSLT stylesheet.

This may seem like a bit of a dodgy move, for a
company with as staunch an attitude of post-modernist rectitude
as Cat's Eye Technologies
to go adopting technologies that are clearly of Pakled origin.

However, there are several good reasons.  Firstly, XSLT, being
a Turing-complete macro-expansion language with all the readability
of Scheme, is practically an honourary esolang.  Secondly, RSS is
specified about as rigorously and consistently as most esolangs as well.
And thirdly — although I dispute that this is a particularly important
reason — somebody might actually find it useful.

### Release of the Iphigeneia Programming Language

*   news-link: http://catseye.tc/projects/iphi/
*   date: Sat, 25 Nov 2007 12:00:00 GMT

The Iphigeneia programming language is released.  Iphigeneia is a toy
programming language which contains features from both
imperative programming and functional programming.  It was originally
intended as a testbed for algorithms that convert programs between the
two forms, but it has strayed slightly from that goal.

### Console::Virtual Revived, HUNTER and worb Benefit

*   news-link: http://catseye.tc/projects/cons_virt/
*   date: Sat, 23 Nov 2007 12:00:00 GMT

Noticing that the Perl 5 implementation of [HUNTER](http://catseye.tc/node/HUNTER)
required a module that was never restored to the website after the last crash,
I dug it out of cold storage and refurbished it a bit, resulting in
[Console::Virtual](http://catseye.tc/node/Console%3A%3AVirtual).

In the process I tidied up the HUNTER project quite a bit, including supporting a
real delay, measured in milliseconds, between animation frames.  (This requires the
Time::HiRes module, but it still works without it; you just can't get
sub-second resolution in that case.)

And, in the process of doing that, I noticed the implementation of
[noit o' mnain worb](http://catseye.tc/node/noit%20o%27%20mnain%20worb) could use many of the same improvements.
So now it, too, uses Console::Virtual
instead of requiring an ANSI-compatible terminal, and supports an adjustable delay
between frames.

Concurrent with this project interdependency, I've made a quick stab at listing
the requirements for each project in the little "info box" on its project page.
This is pretty crude right now, but it's hopefully a step in the right direction.

### Release of the Didigm Reflective Cellular Automaton

*   news-link: http://catseye.tc/projects/didigm/
*   date: Sat, 17 Nov 2007 12:00:00 GMT

Release of initial specification of the Didigm
reflective ceullar automaton.

Also some random hacking on libvesa.

### Release of the Emmental Programing Language

*   news-link: http://catseye.tc/projects/emmental/
*   date: Sat, 11 Nov 2007 12:00:00 GMT

The Emmental programming language has been
released.  Emmental is a self-modifying programming language; it is defined in
terms of a meta-circular interpreter, and this meta-circular interpreter provides
operations that modify its behaviour.  In fact, Emmental requires that this
mechanism of meta-circular self-modification in order for it to achieve
Turing-completeness.

### Release of You are Reading the Name of this Esolang

*   news-link: http://catseye.tc/projects/urreading/
*   date: Sat, 05 Nov 2007 12:00:00 GMT

The programming language You are Reading the Name of this Esolang
was released.  It's an exploration in the design space of programming languages
with undecidable elements.  Specifically, the problem of whether or not a given string
of symbols is a well-formed You are Reading the Name of this Esolang program is undecidable.

### Release of the Cabra Programming Language

*   news-link: http://catseye.tc/projects/cabra/
*   date: Sat, 01 Nov 2007 12:00:00 GMT

The Cabra programming language,
successor of sorts to [Burro](http://catseye.tc/node/Burro), has been released.
Cabra programs form, not a group, but a dioid — an idempotent semiring — 
under the operations of sequential and parallel composition.

### Release of the Burro Programming Language

*   news-link: http://catseye.tc/projects/burro/
*   date: Sat, 26 Oct 2007 12:00:00 GMT

The Burro programming language, after two years
(on and off) of design work, has finally been released.  Burro is a Brainfuck-like language
whose programs form an algebraical group under the operation of concatenation (roughly
speaking — see the docs for the complete picture.)

### (Re-)Unearthing of the Maentwrog Programming Language

*   news-link: http://catseye.tc/projects/maentw/
*   date: Sat, 30 Sep 2007 12:00:00 GMT

The Maentwrong language, predecessor of
[Befunge-93](http://catseye.tc/node/Befunge-93), and thought by me to be lost forever (again), was found (again)
on a long-forgotten backup disc.  It has been brought forth into the light
of the projects directory (again) for whatever it's worth.

### catseye.mine.nu No Longer in Service

*   news-link: http://catseye.tc/
*   date: Sat, 28 Aug 2007 12:00:00 GMT

The catseye.mine.nu server is no longer in service
This has two consequences:  The old http://catseye.mine.nu:8080/
URL prefix for this site will no longer redirect here to catseye.tc,
and the Subversion repositories served by catseye.mine.nu
will no longer be publicly available.

The catseye.webhop.net redirect will continue to work, and the
tarball releases of projects will still be available from catseye.tc.

Whether the catseye.mine.nu server will ever go up again or not depends
on too many factors for me to be able to say at this time.  I definately want to
keep providing publicly available source code repositories of the projects, but due
to circumstances it will have to be a low priority goal over the next few months.

### Updates to SMITH and REDGREEN

*   news-link: http://catseye.tc/projects/smith/
*   date: Sat, 22 Jul 2007 12:00:00 GMT

The SMITH language has been updated in
a tiny but significant way: overwriting instructions with other instructions
is now defined.  The reference implementation now implements this sanely as
well.  Thanks to Nathan Thern for pointing this out (and for submitting a
SMITH version of "99 Bottles of Beer"!)

Some bugs in [REDGREEN](http://catseye.tc/node/REDGREEN) have been fixed
as well: the documentation claims that Wires and Sparks behave per the
WireWorld automaton, and that Zappy and BigZappy set things on fire.  The
ALPACA implementation of REDGREEN now properly implements these rules.
Thanks to Stewart Gordon for pointing these bugs out.

Also, I dug up [noise](http://catseye.tc/node/noise) and put
it in the projects.  I swear there was a manual page for it too, but I can't find it.

### Release of the Hev Programming Language

*   news-link: http://catseye.tc/projects/hev/
*   date: Sat, 17 Jun 2007 12:00:00 GMT

The Hev programming language has been released.
Hev allows programming in infix notation, but at the same time,
never needs parentheses and never forces you to memorize precedence tables!
Truly, a major breakthrough.

### Release of the Xigxag automaton

*   news-link: http://catseye.tc/projects/xigxag/
*   date: Sat, 02 Jun 2007 12:00:00 GMT

Xigxag, a simple automaton with exponential growth almost
everywhere, has been released.

### Zzrk Released, and More

*   news-link: http://catseye.tc/projects/zzrk/
*   date: Sat, 15 May 2007 12:00:00 GMT

Most significantly, a project has been added for
Zzrk, a text adventure
game written in a meta-language intended for building compilers (Zz).

I also brought [GraNoLa/M](http://catseye.tc/node/GraNoLa/M) and [SP\ASM](http://catseye.tc/node/SP_ASM)
out of those dusty ol' boxes in the attic and added them to the line-up.

[REDGREEN](http://catseye.tc/node/REDGREEN), [Braktif](http://catseye.tc/node/Braktif), and [Circute](http://catseye.tc/node/Circute)
have also been split off from the main [ALPACA](http://catseye.tc/node/ALPACA)
distribution, and live in projects of their own.

I also polished the site design a wee bit.


