s = "abbb"
print(s[::-1])

def pallindrom(str):
    # just reverse the sring

    rs = s[::-1]

    if s == rs :
        return True
    else :
        return False


print(pallindrom(s))