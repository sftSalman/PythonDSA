arr = [1, 2, 3, 4, 5, 6, 7]
d = 2


def rotate(arr, d) :
    n = len ( arr )
    rotated_arr = []

    # Append elements from index d onwards
    for i in range ( d, n ) :
        rotated_arr.append ( arr[i] )

    # Append elements from index 0 to d-1
    for i in range ( d ) :
        rotated_arr.append ( arr[i] )

    return rotated_arr


result = rotate ( arr, d )
print ( result )
