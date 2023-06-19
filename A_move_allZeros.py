arr = [1, 2, 0, 4, 3, 0, 5, 0]

def moveZeros(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        if arr[i]!=0:
            arr[count] = arr[i]
            count = count + 1


    while count <n :
        arr[count]=0
        count += 1

    return arr



print(moveZeros(arr))

