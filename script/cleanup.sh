#!/bin/sh -x

ARTICLES="
    article/Distribution?Organization.md
    article/Electronics?Projects.md
    article/Games.md
    article/List?of?Unfinished?Interesting?Esolangs.md
    article/Musical?Compositions.md
    article/Pictures.md
    article/Movies.md
    article/Retrocomputing.md
    article/Texts.md
    article/Tools.md
    article/Platforms.md
    article/Formats.md
    article/Archived.md
    article/Languages.md
    article/Language?Implementations.md
    article/Automata.md
    article/Gewgaws.md
    article/Events.md
    article/General?Information.md
    article/Project?Dependencies.md
"

### rebuild refdexes

feedmark --output-refdex $ARTICLES >article-refdex.json || exit 1
REFDEXES=misc-refdex/games-refdex.json,misc-refdex/texts-refdex.json,misc-refdex/retrocomputing-refdex.json,misc-refdex/languages-refdex.json,misc-refdex/misc-refdex.json
feedmark --input-refdexes=$REFDEXES $ARTICLES --output-refdex >refdex.json || exit 1

### rewrite documents with new refdexes

PYTHONPATH=../Feedmark/src python ./script/cleanup.py || exit 1
