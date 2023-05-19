def find_first_repeating(arr):
    indices = {}
    min_index = len(arr) +1
# 4 , 5
    for i in range(len(arr)):
        if arr[i] in indices:
            min_index = min(min_index, indices[arr[i]])
        else:
            indices[arr[i]] = i

    if min_index > len(arr):
        return -1
    else:
        return arr[min_index]

arr1 = [10, 5, 3, 4, 3, 5, 6]
print(find_first_repeating(arr1))  # Output: 5

arr2 = [6, 10, 5, 4, 9, 120, 4, 6, 10]
print(find_first_repeating(arr2))  # Output: 6

