"""
module docstring
"""
import itertools


def get_longest_palindrome(strng: str) -> str:
    """
    Find the longest substring which is palindrome for a given string.
    :param strng: str
    :return: str
    """
    max_pol_strng = ''
    max_pol_strng_len = 0

    for start, stop in itertools.combinations(range(len(strng) + 1), 2):
        sub_strng = strng[start:stop]
        if (len(sub_strng) > max_pol_strng_len) and (sub_strng == sub_strng[::-1]):
            max_pol_strng, max_pol_strng_len = sub_strng, len(sub_strng)

    return max_pol_strng
