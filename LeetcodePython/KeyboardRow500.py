# Given a List of words, return the words that can be typed using letters of alphabet
#  on only one row's of American keyboard


def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """

    rows = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 'a': 2, 's': 2, 'd': 2,
            'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
    res = []

    for el in words:
        val = rows[el[0].lower()]
        ensum = sum(rows[ch.lower()] for ch in el)
        if ensum == val * len(el):
            res.append(el)

    return res


