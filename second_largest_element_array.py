
arr = [1,2,3,4,55,333]

def second_arr(arr):
    first = second = -99999999999
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second & arr[i] != first:
            second = arr[i]

    return second


print(second_arr(arr))