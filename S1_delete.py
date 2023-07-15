st = 'salman'

def delete_vowel(st):
    new = st
    vow =['a','e','i','o','u']
    for ch in vow:
        new = new.replace(ch,'')

    return new

print(delete_vowel(st))