Chrysoberyl
===========

*Chrysoberyl* is an attempt to catalogue, and curate, the things produced
by, and related to, [Cat's Eye Technologies][].

It is something between a wiki and a database and a semantic web and
_The Devil's Dictionary_.

It is supposed to be primarily informative, and only secondarily machine-
processable, and only thirdly structured.  For this purpose, it has
historically been collected in relatively ad-hoc YAML files, but in 2017
it was converted to [Feedmark][] format, which is a subset of Markdown.

These Feedmark articles can be found in [the article directory](article/).

Chrysoberyl contains primarily things produced by Cat's Eye Technologies;
it only contains things not produced by Cat's Eye Technologies when they
directly relate to things that are (e.g. Perl 5.12 might have an entry,
but only as a "Project Dependency", not as a "Programming Language".)

This README used to contain a lot more information, but a lot of it has
gone out of date at this point, but if you're interested, you can look
it up in this repository's history.

The scripts in the `script` directory are used for managing the content
in Chrysoberyl, as well as for release management of the things produced
by Cat's Eye Technologies.  They are written in Python 3, and may have
a few requirements.  You can set up a virtualenv and install them with:

    virtualenv --python=3.5 venv
    source venv/bin/activate
    pip install -r requirements.txt

[Cat's Eye Technologies]: https://catseye.tc/
[Feedmark]: https://catseye.tc/node/Feedmark
