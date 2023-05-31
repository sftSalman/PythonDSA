def printLeaders(arr, size):
    for i in range(0, size):
        j = i + 1
        while j < size:
            if arr[i] <= arr[j]:
                break
            j += 1
        if j == size:  # If loop completed all iterations
            print(arr[i])

# Driver code
arr = [16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))
