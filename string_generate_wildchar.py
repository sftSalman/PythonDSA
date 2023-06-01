st = '1??0?101'
print(st)

def wildchar(st):
    for i in range(len(st)):
        if st[i] == '?':
            st = st[:i] + '0' + st[i+1:]

    return st

st = wildchar(st)
print(st)
