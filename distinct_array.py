arr = [1,1,1,2,2,3,4,4]
new_arr = []

def distc(arr):
    for i in range(len(arr)) :
        for j in range (0,len(arr)-i-1):
            if arr[j] == arr[j+i]:
                arr.remove(arr[j])


distc(arr)
print(arr)


distc(arr)