#!/bin/sh -x

ARTICLES=../Chrysoberyl/article

REFDEXES=games-refdex.json,retrocomputing-refdex.json,misc-refdex.json

feedmark --input-refdexes=$REFDEXES --output-refdex \
                          "article/Distribution Organization.md" \
                          "article/Electronics Projects.md" \
                          "article/Games.md" \
                          "article/List of Unfinished Interesting Esolangs.md" \
                          "article/Musical Compositions.md" \
                          "article/Pictures.md" \
                          "article/Retrocomputing.md" \
                 >refdex.json

## non-lists
feedmark --input-refdex=refdex.json --input-refdex-filename-prefix="../" \
         "article/Distribution Organization.md" \
         "article/Retrocomputing.md" \
         --rewrite-markdown || exit 1

exit 0

## lists
feedmark --input-refdex=refdex.json \
         --check-against-schema="schema/Electronics Project.md" \
         "article/Electronics Projects.md" \
         --rewrite-markdown || exit 1

feedmark --input-refdex=refdex.json \
         --check-against-schema="schema/Game.md" \
         "article/Games.md" \
         --rewrite-markdown || exit 1
