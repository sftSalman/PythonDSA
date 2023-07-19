st = 'aa'
def isPlaindrom(st):
    if len(st)==1:
        return True
    if (st[0]==st[-1]):
        return isPlaindrom(st[1:])
    else:return False


print(isPlaindrom(st))