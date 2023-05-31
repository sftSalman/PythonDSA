def printLeaders(arr, size) :
    for i in range ( 0, size ) :
        for j in range ( i + 1, size ) :
            if arr[i] <= arr[j] :
                break
        if j == size :  # If loop didn't break
            print ( arr[i] )


# Driver function
arr = [16, 17, 4, 3, 5, 2]
printLeaders ( arr, len ( arr ) )