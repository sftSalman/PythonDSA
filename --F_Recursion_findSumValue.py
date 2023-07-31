arr = [1, 4, 3, -5, -4, 8, 6]
def findSum(arr):
    if len(arr)<=1:
        return arr[0]
    else:
        return arr[0]+findSum(arr[1:])

print(findSum(arr))