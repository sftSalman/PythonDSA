inp = "A1B2C3DEFGH"


def strprocess(input_str1):
    vowels = 'AEIOUaeioui'
    new = ''

    for ch in input_str1:
        if ch.lower() not in vowels and not ch.isdigit():
            new += "*" +ch.upper()

    return new


print(strprocess(inp))
