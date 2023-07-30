str1 = "2a-b-(3c-d)"
str2 = "2a-b-(3c-d)"


def chckString(st1):
    new = ''
    for ch in st1:
        if not ch.isdigit():
            new = new + ch

    return new

def isSame(str1,str2):
    first = chckString(str1)
    second = chckString(str2)

    if first == second:
        return print("They are indentical")
    else:
        return print("They are not identical")

isSame(str1,str2)


