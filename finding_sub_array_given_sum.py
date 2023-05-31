arr = [1, 4, 20, 3, 10, 5]
sum = 33

def find_sub_sum(arr,sum):
    subarr=[]
    for i in range(len(arr)):
        subarr = arr[i]
        if arr[i] == sum :
            return i
        else:
            for j in range(i+1,len(arr)):
                subarr += arr[j]
                if subarr == sum :
                    return (i,j)



print(find_sub_sum(arr,sum))