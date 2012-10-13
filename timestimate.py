# coding=utf-8
import re


def gettime(ln):
    '''(str) -> number

    Return time in hours for string ln

    >>> * Агенда и вопросы к Синельникову, 30
    0.5
    >>> - Агенда и вопросы для переговоров в среду, 20
    0.3333(3)
    >>> * Хуячим горячую и ВИП-страницу, 4
    4
    >>> - перенести домен Галкиной
    0
    >>> - Товеровский, 1:30
    1.5
    >>> * Дочитать Business Model Generation, 1,3
    1,3
    >>> - купить билеты, 115Ж, 28 сен 10:03–00:17. 115И 30 сен 22:15–10:37, 1.4
    1.4

    '''

    r = re.compile(".*")  # ^[*-].*D+.*$
    m = r.match(ln)
    return m


f = open('done.txt', 'r')

'''
for line in f:
    print line
f.close()
'''

str1 = "- Агенда и вопросы для переговоров в среду, 20"
print gettime(str1)
