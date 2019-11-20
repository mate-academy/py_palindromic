"""
docstring
"""


def reversed_palindrome(string):
    """

    :param string:
    :return:
    """
    return string[::-1]


def get_longest_palindrome(string):
    """

    :param string:
    :return:
    """
    if len(string) <= 1:
        return string
    longest_palindrome = ''
    for start_palindrome in range(0, len(string) - 1):
        for end_palindrome in range(start_palindrome + 1, len(string)):
            palindrome = string[start_palindrome: end_palindrome + 1]
            if palindrome == reversed_palindrome(palindrome) \
                    and len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
    if longest_palindrome:
        return longest_palindrome
    else:
        return string[0]
