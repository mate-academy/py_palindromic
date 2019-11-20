""""Palindromic search module"""


def get_longest_palindrome(text: str) -> str:
    """"Palindromic search function"""
    size = len(text)
    result = ""
    for index in range(size):
        for second_index in range(index+1, size+1):
            temp = text[index:second_index]
            if temp == temp[::-1]:
                if len(temp) > len(result):
                    result = temp
    return result
