def recStringProcess(s) :
    vowels = 'AEIOUaeiou'
    if len ( s ) == 0 :
        return ""

    if s[0].isdigit () or s[0] in vowels :
        return recStringProcess ( s[1 :] )
    else :
        return '*'+s[0].upper() + recStringProcess ( s[1 :] )


str_input = 'A1b2C3DEFGH'
print ( recStringProcess ( str_input ) )  # Output: "BCDFGH"
