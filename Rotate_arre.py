def rotate(arr, d):
    n = len(arr)
    #d = d % n
    print(d)# To handle cases where d is greater than the length of the array

    # Rotate the array in-place using slicing
    arr[:] = arr[d:] + arr[:d]
    return arr


arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]
d = 9
print(rotate(arr, d))
