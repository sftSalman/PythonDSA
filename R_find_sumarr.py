
ar = [1,2,3,4,5,5,6]
print(ar[1:])
sum = 0
def r(ar):
    if len(ar)==0:f
        return 0
    else:
        return ar[0] + r(ar[1:])


print(r(ar))