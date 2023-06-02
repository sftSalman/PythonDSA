st = 'salman'
print(st) # ['a', 'a', 'l', 'm', 'n', 's']
print(sorted(st))
def sortString(str) :
    str = ''.join(sorted(str))
    return (str)


sortString(st)
print(sortString(st))