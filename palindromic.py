"""Find the longest palindrome"""


def get_longest_palindrome(string: str) -> str:
    """Find the longest palindrome"""
    if not string:
        return ''
    largest = string[0]
    for i in range(len(string)):
        for j in range(0, i):
            sub = string[j:i+1]
            if sub == sub[::-1]:
                largest = max(largest, sub, key=len)
    return largest
