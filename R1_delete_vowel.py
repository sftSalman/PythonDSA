st   = 'salman'
def delete_vowel(sti):
    if len(sti)==0:
        return sti
    else:return delete_vowel(sti[1:])
