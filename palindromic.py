def get_longest_palindrome(phrase: str) -> str:
    result = []
    if phrase:
        for index, value in enumerate(phrase):
            for j in range(0, index + 1):
                sub_phrase = phrase[j:index + 1]
                if sub_phrase == sub_phrase[::-1]:
                    result.append(sub_phrase)
        return max(result, key=len)
    else:
        return ''
