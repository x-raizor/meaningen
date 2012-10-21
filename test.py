
def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that appear at least
    once in s2.  The characters in the result will appear in the same order as
    they appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a'
    >>> common_chars('abb', 'ab')
    'abb'
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''

    res = ''

    for ch in s1:
        if ch in s2:
            res = res + ch

    print res
    return res

common_chars('abc', 'ad')
common_chars('a', 'a')
common_chars('abb', 'ab')
common_chars('abracadabra', 'ra')