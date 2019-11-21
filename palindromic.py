"""Find the longest palindrome"""


def get_longest_palindrome(string: str) -> str:
    """Find the longest palindrome"""
    longest = ''
    reversed_string = string[::-1]
    for index, _value in enumerate(string, start=1):
        if string[:index] == string[:index][::-1] and index > len(longest):
            longest = string[:index]
    for index, _value in enumerate(reversed_string, start=1):
        if reversed_string[:index] == reversed_string[:index][::-1] and index > len(longest):
            longest = reversed_string[:index]
    return longest
