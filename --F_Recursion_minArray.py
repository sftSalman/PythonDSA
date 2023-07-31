def recMin(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return min(arr[0], recMin(arr[1:]))

arr = [1, 4, 3, -5, -4, 8, 6]
print(recMin(arr))  # Output: -5
