# coding=utf-8
from pymorphy import get_morph

# Return all of combinations for string in file variants.txt

_file = open("variants.txt", 'r')

words = []

for line in _file:
    line = line.rstrip("\n")
    words.append(line)
_file.close()

morph = get_morph("/Users/andrew/Python/meaningen/dict/ru")

for _word in words:

    _copy = words[:]
    _copy.remove(_word)

    for _iword in _copy:
        # для морфологии слова должны быть в юникоде и ЗАГЛАВНЫМИ
        word_form = morph.inflect_ru(unicode(_iword, 'utf-8').upper(), u'рд,ед')
        print  unicode(_word, 'utf-8') + " " + word_form.lower()

modificators = ["анти", "над", "под"]
rod_modificators = ["прошлое", "будущее"]

for _word in words:
    for _modi in rod_modificators:
        word_form = morph.inflect_ru(unicode(_word, 'utf-8').upper(), u'рд,ед')
        print  unicode(_modi, 'utf-8') + " " + word_form.lower()
    for _modi in modificators:
        print  _modi + _word
