"""This module contains function
get_longest_palindrome(s)
"""

def get_longest_palindrome(string: str) -> str:
    """Returns a substring of a given string
    which is a palindrome"""
    length_s = len(string)

    if length_s < 2:
        return string
    longest_pal = ''
    for s_pal in range(0, length_s - 1):
        for e_pal in range(s_pal + 1, length_s):
            substr = string[s_pal:e_pal + 1]
            if substr == substr[::-1] and len(substr) > len(longest_pal):
                longest_pal = substr

    return longest_pal if longest_pal else string[0]
