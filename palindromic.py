"""module docstring"""

def find_palindrome_substr(some_string, left, right, max_string):
    """function docstring"""
    while left >= 0 and right < len(some_string):
        if some_string[left] != some_string[right]:
            break
        pal = some_string[left:right + 1]
        if len(pal) > len(max_string):
            max_string = pal
        left -= 1  # expand to left
        right += 1  # expand to right
    return max_string

def get_longest_palindrome(some_string):
    """function docstring"""
    max_string = ""
    if len(some_string) != 0:
        for seq in range(len(some_string)):
            max_string = find_palindrome_substr(some_string, seq, seq + 1, max_string)
            max_string1 = find_palindrome_substr(some_string, seq - 1, seq + 1, max_string)
            if max_string < max_string1:
                max_string = max_string1

        if max_string == "":
            max_string += some_string[0]

    return max_string
