"""
docstring
"""


def get_longest_palindrome(string: str) -> str:
    """

    :param string:
    :return:
    """
    if reverse(string) == string:
        return string


def reverse(string):
    """

    :param string:
    :return:
    """
    return string[::-1]

