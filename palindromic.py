"""
module docstring
"""


def get_longest_palindrome(strng: str) -> str:
    """
    Find the longest substring which is palindrome for a given string.
    :param strng: str
    :return: str
    """
    if len(strng) <= 1:
        return strng
    max_pol_strng = ""
    for i in range(len(strng)):
        for j in range(i + len(max_pol_strng), len(strng)):
            if strng[i:j + 1] == strng[i:j + 1][::-1]:
                if len(strng[i:j + 1]) > len(max_pol_strng):
                    max_pol_strng = strng[i:j + 1]
    return max_pol_strng
