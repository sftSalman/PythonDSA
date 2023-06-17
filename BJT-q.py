def consonant(instr):
    vowels_and_digits = ['a', 'e', 'i', 'o', 'u', '0', '1', '2', '3', '4', '5', '6', '7','8','9']
    new = instr
    for alphabet in vowels_and_digits:
        new = new.replace(alphabet, '')
    return new

instr = '1A2BcDnajMkW'
result = consonant(instr)
print(result)
