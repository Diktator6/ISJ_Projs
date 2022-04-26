#!/usr/bin/env python3

from itertools import permutations

def all_permutations_substrings(a_str):
    """Generates all permutations of all substrings of the input string
    """

    return set(
        ''.join(item)
        for item in permutations(a_str, len(a_str)))


def uniq_srt(it):
    """Returns the input sequence unified and sorted (according to the values)

    uniq_srt([3, 3, 5, 3, 4, 2, 4])
    [2, 3, 4, 5]

     uniq_srt('abrakadabra')
    ['a', 'b', 'd', 'k', 'r']

    """

    return sorted({item for item in it})

def uniq_orig_order(it):
    """Returns the input sequence, items ordered by the order of their
       first appearance

     uniq_orig_order([3, 3, 5, 3, 4, 2, 4])
    [3, 5, 4, 2]

     uniq_orig_order('abrakadabra')
    ['a', 'b', 'r', 'k', 'd']

    """

    list_it = list(it)
    list_re = []
    while list_it:
        x = list_it.pop()
        if x not in list_it:
            list_re.insert(0, x)

    return list_re                                       # your solution

print(uniq_orig_order([3, 3, 5, 3, 4, 2, 4]))
