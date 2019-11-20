"""docstring"""

def get_longest_palindrome(string: str) -> str:
    """Find longest palindrome"""
    reversed_string = string[::-1]
    # its already palindrome
    if reversed_string == string:
        return string

    # save all substring palindromes in list
    palindromes = []
    largest = 0
    for i in range(len(string)):
        for j in range(len(string) + 1):
            if string[j:(j+i)] == string[j:(j+i)][::-1]:
                palindromes.append(string[j:(j+i)])
                # find largest in list
                if len(string[j:(j+i)]) > largest:
                    largest = len(string[j:(j+i)])
                    index_of_largest = palindromes.index(string[j:(j+i)])

    return palindromes[index_of_largest]
