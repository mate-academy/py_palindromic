"""docstring?"""


def get_longest_palindrome(string: str) -> str:
    """Find longest palindrome"""
    reversed_string = string[::-1]
    # its already palindrome
    if reversed_string == string:
        return string

    for index in range(len(string)):
        if string[index:] in reversed_string:
            return string[index:]
        # if there is no substring palindrome longer than 1 char
        if len(string[index:]) == 2:
            return string[0]

    return ""
