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
    for j in range(1, lngth // 2):
        if is_palindrom(strng[j:-j]):
            return strng[j:-j]
        if is_palindrom(strng[j:]):
            return strng[j:]
        if is_palindrom(strng[:j]):
            return strng[:j]
    return strng[0]
