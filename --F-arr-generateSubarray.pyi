def genSubarray(arr):
    for i in range(len(arr)):
        for j in range (len(arr)-i-1):
            return i ,j


print(genSubarray([1,2,3,4]))
