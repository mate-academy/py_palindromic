'''
Vodule
'''


def is_palindrom(strng: str) -> bool:
    '''

    :param strng:
    :return:
    '''
    return strng == strng[::-1]


def get_longest_palindrome(strng: str) -> str:
    '''

    :param s:
    :return:
    '''
    lngth = len(strng)
    for i in range(lngth - 1):
        if is_palindrom(strng[i:]):
            return strng[i:]
    for i in range(lngth, 0, -1):
        if is_palindrom(strng[:i]):
            return strng[:i]
    return ''
