def printDistinct(s):
    distinct_chars = []

    for char in s:
        if char not in distinct_chars:
            distinct_chars.append(char)

    return distinct_chars

str_example = [1,2,3,4,5,6,6,3,5,3,2]
print(printDistinct(str_example))  # Output: ['s', 'a', 'l', 'm', 'n'] (distinct characters)
