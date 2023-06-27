def remove_char_recursive(s, ch):
    if ch not in s:
        print('not found')
        return s

    index = s.index(ch)
    print(index)
    print(s[:index])
    print(s[index +1 :])
    print(s[:index] + s[index+1:])
    return remove_char_recursive(s[:index] + s[index+1:], ch)

s = "geeksforgeeks"
e = 's'

n = remove_char_recursive(s, e)
print(n)
