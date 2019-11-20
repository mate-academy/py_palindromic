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
    if strng == '':
        return ''
    if is_palindrom(strng):
        return strng
    lngth = len(strng)
    for i in range(0, lngth - 1):
        for j in range(lngth, i+1, -1):
            if is_palindrom(strng[i:j]):
                return strng[i:j]
    return strng[0]
