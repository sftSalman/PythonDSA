input2 = 'A1B2C3DEAAFEEE5959959GH'
vowel = 'AEIOUaeiou'
new = ''
for ch in input2:
    if not ch.isdigit() and ch not in vowel:
        new += "*" + ch


print(new)
