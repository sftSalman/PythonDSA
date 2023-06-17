def find_minimum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return min(arr[0], find_minimum(arr[1:]))

arr = [1, 4, 3, -5, -4, 8, 6]
min_element = find_minimum(arr)
print(min_element)
