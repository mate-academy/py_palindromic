"""This module contains function
get_longest_palindrome(s)
"""

def get_longest_palindrome(string: str) -> str:
    """Returns a substring of a given string
    which is a palindrome"""
    length_s = len(string)

    if length_s < 2:
        return string

    s_last = 1
    while s_last < length_s:
        for start in range(s_last):
            end = length_s - s_last + start
            substr = string[start:end + 1]
            if substr == substr[::-1]:
                return substr
        s_last += 1

    return string[0]
