arr = [1,7,2,4,2,7,0,8,2,9,4]
def bblsort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j] ,arr[j+1]= arr[j+1],arr[j]



bblsort(arr)
print(arr)