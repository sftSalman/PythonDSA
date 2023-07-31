

def countDistinct(s):
    char_count = {}
    count = 0
    for char in s:
        if char not in char_count:
            char_count[char] = 1
            count += 1

    return count

str_example = 'salman'
print(countDistinct(str_example))  # Output: 5 (distinct characters: 's', 'a', 'l', 'm', 'n')
