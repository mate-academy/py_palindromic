"""
docstring
"""

import palindromic


def test_empty():
    """

    :return:
    """
    assert palindromic.get_longest_palindrome("") == ""


def test_one_char():
    """

    :return:
    """
    assert palindromic.get_longest_palindrome("A") == "A"


def test_one_char_in_str():
    """

    :return:
    """
    assert palindromic.get_longest_palindrome("ABCDEF") == "A"


def test_whole_string():
    """

    :return:
    """
    assert palindromic.get_longest_palindrome("ABBA") == "ABBA"


def test_banana():
    """

    :return:
    """
    assert palindromic.get_longest_palindrome("BANANA") == "ANANA"


def test_reversed():
    assert palindromic.get_longest_palindrome("ABCDEBCA") == "A"
