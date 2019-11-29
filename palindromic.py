""" get sub palindrome"""


def get_longest_palindrome(word: str) -> str:
    """get long palindrome"""
    count = 0
    if word == "":
        return ""

    longest = word[0]
    sub = [word[i:j] for i in range(len(word)) for j in range(i + 1, len(word) + 1)]
    for i in sub:
        if len(i) > 1 and len(i) > count and check_pl(i):
            count = len(i)
            longest = i
    return longest


def check_pl(wrd):
    """check word"""
    return wrd == wrd[::-1]
