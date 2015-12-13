Idemscriptent Given Names
=========================
Are you a Romanian-Hungarian that is expecting a baby with a Polish-Ukrainian? Are you living in Sweden, but consider moving to Germany or France? Have you been traumatised by having your name misspelled while moving from one country to another? If the answer to some of these questions is _yes_, then this script might be for you.

This script find all the given names that are spelled identically in a configurable number of languages. For example, if your name is _Cristian_ expect your name to be misspelled to _Christian_ while living in France or German, _Krystian_ while living in Poland and _Kristian_ while living in Sweden. On the other hand, if your name was _Ahmed_, it would be spelled correctly in numerous countries whose official language uses the Latin script.

Current Implementation
======================
The script `find-idemscriptent-given-names.py` works as follows. It reads the top 100 list of baby names for French, German, Polish, Romanian and Swedish. Diacritic marks are stripped, e.g., _Léo_ become _Leo_. Finally, the names that are present in the top 100 list of at least 3 languages are displayed, sorted by the number of lists they are present in.

To customise the result to your own needs, remove or add files or the form `names-m-LANG.txt` and `names-f-LANG.txt`, where LANG is the [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code of a language.

Example Output
==============

Female Baby Names
-----------------
    Emma      : de fr pl ro sv
    Sara      : de fr pl ro sv
    Victoria  : de fr pl ro sv
    Anna      : de fr pl sv
    Emilia    : de pl ro sv
    Julia     : de fr pl sv
    Laura     : de fr pl ro
    Maria     : de pl ro sv
    Olivia    : fr pl ro sv
    Sofia     : de fr ro sv
    Clara     : de fr ro
    Elina     : de ro sv
    Eva       : de fr ro
    Hanna     : de pl sv
    Klara     : de pl sv
    Lena      : de fr pl
    Lisa      : de fr sv
    Luna      : de fr sv
    Maja      : de pl sv
    Marta     : de pl ro
    Melissa   : de fr sv
    Milena    : de pl ro
    Nina      : de fr pl

Male Baby Names
---------------
    Gabriel   : de fr pl ro sv
    Adam      : fr pl ro sv
    Adrian    : de pl ro sv
    Daniel    : de pl ro sv
    David     : de fr ro sv
    Simon     : de fr ro sv
    Alex      : fr pl sv
    Alexander : de pl sv
    Artur     : de pl ro
    Benjamin  : de fr sv
    Emil      : de pl sv
    Felix     : de ro sv
    Filip     : pl ro sv
    Florian   : de fr ro
    Hugo      : fr ro sv
    Jonathan  : de fr sv
    Julian    : de pl sv
    Leo       : de fr sv
    Leon      : de pl sv
    Lucas     : de fr sv
    Matteo    : de fr sv
    Noah      : de fr sv
    Paul      : de fr ro
    Samuel    : de fr sv
    Sebastian : de pl sv
    Theo      : de fr sv
    Valentin  : de fr ro
    Vincent   : de fr sv

Weirdly, both _Clara_ and _Klara_ seem popular in 3 of the selected languages.

Feedback
========
Feedback on how to improve selection of baby names is highly appreciated. Please create an issue or a pull request. Thanks!
