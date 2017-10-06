# encoding: UTF-8

mzstorkipiwanbotbotbot: 
  type: Tool
  authors:
  - Chris Pressey
  auspices:
  - Cat's Eye Technologies
  description: |
    An IRC bot with no purpose or plan.
  inception-date: 2010
  development-stage: archival

mzstorkipiwanbotbotbot (Lua):
  type: Implementation
  implementation-of:
  - mzstorkipiwanbotbotbot
  reference: true
  in-distribution: mzstorkipiwanbotbotbot distribution
  license: Public Domain
  host-language: Lua

Rtype:
  type: Implementation
  implementation-of:
  - mzstorkipiwanbotbotbot
  in-distribution: mzstorkipiwanbotbotbot distribution
  license: Public Domain
  host-language: R


Rooibos:
  type: Library
  summary: Simple, single-module parser combinator library
  authors:
  - Chris Pressey
  auspices:
  - Cat's Eye Technologies
  description: |
    Rooibos is a parser combinator library for Python. Modelled somewhat
    after yeanpypa (self-contained, public domain), but compensates for what
    I considered a fatal flaw in yeanpypa (no good way to describe a
    recursive grammar.) Has a fatal flaw of its own (can only parse
    strictly LL(1) grammars — no backtracking is yet possible.) Originally
    used in [[Eightebed]], but provided here for ease of transplanting into
    other projects.
  inception-date: '2011'
  development-stage: archival

rooibos.py:
  type: Implementation
  implementation-of:
  - Rooibos
  reference: true
  in-distributions:
  - Eightebed distribution
  license: Public Domain
  host-language: Python


toolshelf: 
  type: Tool
  summary: A "package manager" that doesn't actually install anything
  authors:
  - Chris Pressey
  auspices:
  - Cat's Eye Technologies
  description: |
    `toolshelf` is a "package manager" which doesn't actually install any files.
    Instead, it stores the source trees of sundry packages in a single directory,
    and manages your search paths to include the relevant subdirectories of
    those trees. The source trees are typically the working directories of
    local git or Mercurial clones, or they can be source distributions from tarballs.
  inception-date: 2012
  development-stage: work in progress

toolshelf.py:
  type: Implementation
  implementation-of:
  - toolshelf
  reference: true
  in-distribution: toolshelf distribution
  license: MIT license
  host-language: Python


TPiS: 
  type: Tool
  subtitle: Total Procedures in Scheme
  summary: Totality-checker for Scheme procedures
  authors:
  - Chris Pressey
  auspices:
  - Cat's Eye Technologies
  description: |
    This is a static analyzer, written in Scheme, which can check if
    given Scheme procedures are total (always terminate, on any input) by
    checking that they are specified primitive-recursively.  What's more, it
    is written almost entirely in a primitive-recursive style, so it can
    check itself!
  inception-date: ca 2006
  development-stage: archival

TPiS (Scheme):
  type: Implementation
  implementation-of:
  - TPiS
  reference: true
  in-distribution: TPiS distribution
  license: BSD license
  host-language: Scheme
