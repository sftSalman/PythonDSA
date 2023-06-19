def remove_chars(string):
    vowels_and_digits = ['a', 'e', 'i', 'o', 'u', '0', '1', '2', '3', '4', '5', '6', '7']

    if len(string) == 0:
        return string

    if string[0] in vowels_and_digits:
        return remove_chars(string[1:])
    else:
        return string[0] + remove_chars(string[1:])


instr = '1A2BcDnajMkW'
result = remove_chars(instr)
print(result)
