ar = [1,4,2,4,5]
def sortArr(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr


print(sortArr(ar))