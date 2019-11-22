"""
Find palindrome in string
"""

def get_longest_palindrome(strg: str) -> str:
    """ func find palindrome  """
    if not strg or len(strg) == 1:
        return strg

    for i in range(len(strg)-1):
        for y in range(len(strg)-1, i, -1):
            if strg[i:y+1] == strg[i:y+1][::-1]:
                return strg[i:y+1]

    return strg[0]
