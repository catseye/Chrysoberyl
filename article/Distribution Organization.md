Distribution Organization
=========================

How Cat's Eye Technologies' software distributions are organized.

### Release Engineering

Historically, Cat's Eye Technologies has usually identified each release
of a software distribution with only a release number. The release number is
really just the date that the software was released, formatted as
`YYYY.MMDD`. Each of `Y`, `M`, and `D` is a single digit, so that it
sorts nicely, even in a purely lexicographical sort order. In
retrospect, `YYYY.MM.DD` might have been a more structurally consistent
choice, but it's not as nicely symmetrical.

Using only the release date to identify releases mostly suffices for
distributions like ours, which rarely have any maintenance needs warranting
branches and such. But most of our distributions do contain implementations of
[programming languages][],
and these languages may or may not change
between releases. For example, if we're just fixing bugs in a feature of
the implementation, or clarifying the documentation or whatever, that's
not a change to the language. But if all we use to identify it is a
release number, you can't tell if it's a change to the language or not.

In addition, some of our distributions used a different convention, usually
two numbers `A.B` which resembled a fraction in decimal notation: often
`B` would be two digits (like 94) which did not count the number of
minor releases since the last major release cycle, but rather tried to
measure "how close" it was to the *next* major release cycle. Version
numbers like this were sometimes also followed by an (essentially
meaningless) letter.

Realizing what a mess this is, we have strived to revise our release
identification system, as well as to make it more consistent.

With few exceptions, every distribution now carries both a version and a
revision. The version consists of a major version number and a minor
version number, in the format `A.B`, where `A` and `B` are both
non-negative integers. The revision is the same as the old release
number, that is, it is the date in `YYYY.MMDD` format. The version and
revision are separated by hyphens, so a new-style "distfile" name
typically looks like `foo-1.3-2009.0116.zip` (although we are by and
large still providing only the legacy distfiles for download).

The rules for when these numbers change are as follows:

-   If a new release of a distribution supports the same interface
    (syntax and semantics, API, protocol, or what have you) as the
    previous release of that distribution, then the version
    will be the same as the old distribution, but the revision will be
    different.
-   If a new release of a distribution is more-or-less backwards-compatible
    with the previous release, then the major version will be the same,
    but the minor version and revision will be different.
-   If a new release of a distribution is distinctly *not*
    backwards-compatible with the previous release, then the major
    version will be different, the minor version is typically reset to
    zero, and the revision will of course be the date of the release.

### Filesystem Organization

This is a rough guide to how [Cat's Eye Technologies][]' distributions
are laid out.  It is prescriptive,
specifying how distributions should be laid out, but it is informed by
the general pattern we're trying to find in our distributions.  This
guide is currently a work in progress and should not be considered
complete yet.

Certain files in a distribution's root directory have standard meanings:
    
-   `README.markdown` (preferred) or `README` or `README.txt`
    
    A short text (or preferably Markdown) document summarizing what the
    distribution is a distribution of, what sorts of files it contains,
    where to get the latest version of the distribution, and what other
    tools might be needed to use (run or build) the files found in it.
    
    READMEs for [esolangs][] may describe the entire language.
    I'm not sure if this is a good practice or not.
    It started because Bitbucket would only HTMLify
    a Markdown file in its source viewer if it was the README, but now
    it will do that for every Markdown file, so there is less reason to
    put the whole language description here.  Still, for some esolangs,
    this style seems to fit.  (The only problem is that there isn't
    usually a good place to give the other info, like how to build and
    run the included implementations.)
    
-   `LICENSE` or `UNLICENSE`
    
    A short text document explaining what license or licenses the
    content of the distribution is available under.  The filename
    `UNLICENSE` is used instead if (and only if) the entire contents of
    the distribution are in the public domain.

-   `make.sh` or `Makefile`
    
    A Bourne shell script which builds executables and related things
    from the sources included in the distribution.  This may also be
    a `Makefile`, but `Makefile`s are usually put in the `src`
    directory.  `make.sh` may just `cd` to that directory and run `make`.

-   `clean.sh`
    
    A Bourne shell script to clean up after building, in lieu of a
    `make clean` command.

-   `test.sh`
    
    A Bourne shell script which runs tests for the distribution.  The
    tests can test anything they like, but should produce output which
    conforms to Portent format, which we haven't exactly defined yet, so
    don't worry about it.  For now, an exit code of 0 means pass,
    anything else means failure.

Certain files in the root distribution directory have standard meanings as
well:

-   `bin`
    
    Where executables shoud be kept.  Distributions should generally not
    contain native executables; the main exception to this rule is native
    executables for "legacy platforms" such as [MS-DOS][] and
    [Commodore 64][] computers.
    
    Native executables may be written into the `bin` directory when they
    are built from other files in the distribution by e.g. `make.sh`.
    
    Distributions may contain non-native binary files intended to be
    executed, i.e. virtual machine code, and these will reside in `bin`.
    Java `.class` files are contained, under `bin`, in a directory tree
    matching the package names.
    
    Distributions may contain executable scripts.  However, executable
    scripts which contain significant amounts of source code (i.e. ones
    that are not just little drivers or wrappers) should go in `script`
    rather than `bin`.  They may in some cases be copied into `bin` upon
    build.
    
    Names of files in `bin` should not have extensions unless convention
    demands it.  (That is, `tool` rather than `tool.py`, but `tool.com`
    is OK.)
    
-   `demo`
    
    A directory of examples of how the contents of the distribution might
    be used.  Somewhat interchangeable with `eg`, except that `eg` is
    primarily for example programs for a programming language
    (or configuration files, etc.) while `demo` contains demonstrations
    of how the tools (etc.) in the distribution might be used.
    
-   `dialect`
    
    For distributions of programming (and other) languages, this is
    where related languages (usually too minor in variation to warrant
    their own distributions) are defined and implemented.
    
-   `disk`
    
    Where disk images should be kept.

-   `doc`
    
    Where documentation should be kept.  Exceptions include
    `README.markdown` and `LICENSE`, which should be in the root
    directory.
    
    Images may be included in `doc` if they are part of the
    documentation (for example, diagrams) but if they are just
    screenshots, they should probably be elsewhere.

-   `ebin`
    
    Distributions should not ship with pre-compile Erlang `.beam` files,
    but when they are built from the sources, they will go here.  Erlang
    `.app` files may be contained here as well, but these are generally
    not all that useful, and mostly for decoration.
    
-   `eg`
    
    Where examples should be kept, particularly example programs
    in distributions which contain implementations of programming
    languages.  Somewhat interchangeable with `demo`, except that `demo`
    is primarily for demonstrations of how the tools (etc.) in the
    distribution might be used, while `eg` contains examples programs
    for a programming language (or configuration files, etc.)
    
-   `impl`
    
    For distributions containing more than one implementation, this is
    where source code for the non-reference implementations should be
    kept.  (The reference implementation's source should be in `src`.)
    
-   `priv`
    
    Where data files for Erlang applications are kept.
    
-   `script`
    
    Where executable scripts which have significant amount of code in
    them should be kept.  (But if the script gets really large, it should
    probably be broken up into a driver script in `bin` which imports
    source modules from `src`.)
    
-   `src`
    
    Where source code is kept.  For distributions containing more than
    one implementation, this is where the reference implementation is
    kept; other implementations should probably be in `impl` instead.

[programming languages]: https://catseye.tc/article/Languages.md
[esolangs]: ../article/General%20Information.md#esolang
[Cat's Eye Technologies]: ../article/General%20Information.md#cats-eye-technologies
[MS-DOS]: ../article/Project%20Dependencies.md#ms-dos
[Commodore 64]: ../article/Project%20Dependencies.md#commodore-64

