""""Palindromic search module"""


def get_longest_palindrome(text: str) -> str:
    """"Palindromic search function"""
    size = len(text)
    result = ""
    max_size = size
    howtry = 1
    breaker = False
    for index in range(size):
        if index == size or breaker:
            break
        for howtry_index in range(howtry):
            temp = text[howtry_index:max_size+howtry_index]
            if temp == temp[::-1]:
                result = temp
                breaker = True
                break
        howtry += 1
        max_size -= 1
    return result
