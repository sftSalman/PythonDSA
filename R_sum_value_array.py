arr = [2,3,4,5,6,7]

# using for recursion


def findsum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0]+findsum(arr[1:])


print(findsum(arr))

