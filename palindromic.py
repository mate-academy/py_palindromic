"""
Find palindrome in string
"""

def get_longest_palindrome(strg: str) -> str:
    """ func find palindrome  """
    if not strg or len(strg) == 1:
        return strg

    for i in range(len(strg)-1):
        if strg[i:] == strg[i:][::-1]:
            return strg[i:]

    return strg[0]
