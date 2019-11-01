Formats
=======

These are file formats that Cat's Eye Technologies has defined, and
implemented processing tools for.  "File formats" are generally simpler
than [languages](Languages.md).

### Falderal

*   subtitle: **Literate Testing for Languages**
*   inception-date: 2011
*   reference distribution: [Falderal distribution](https://catseye.tc/distribution/Falderal_distribution)

Falderal is a file format for literate test suites.  It is particularly
suited for documenting programming languages (or other specifications of
ways to transform text) and testing their implementation(s) in a
language-agnostic fashion.  The dumbed-down sound-bite version:
"doctests for DSLs".  It can be embedded in both Markdown and Literate
Haskell.

#### Reference Implementation: py-falderal

*   license: BSD license
*   host-language: [Python][]

#### Implementation: Test.Falderal

*   license: BSD license
*   host-language: [Haskell][]

### Feedmark

*   inception-date: 2017
*   reference distribution: [Feedmark distribution](https://catseye.tc/distribution/Feedmark_distribution)

Feedmark is a file format for embedding curational information in Markdown.

#### Reference Implementation: feedmark (Python)

*   license: MIT license
*   host-language: [Python][]

Links
-----

*   [The myth of RSS compatibility](https://web.archive.org/web/20081103204806/http://diveintomark.org/archives/2004/02/04/incompatible-rss)
*   [The S stands for Simple](http://harmful.cat-v.org/software/xml/soap/simple)

[Python]: ../article/Project%20Dependencies.md#python
[Haskell]: ../article/Project%20Dependencies.md#haskell

