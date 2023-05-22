arr = [10, 4, 3, 50, 23, 90]


def largest_three(arr):
    first = second = third = -99999999999999
    for i in range(len(arr)):
        if arr[i]>first:
            third = second
            second = first
            first = arr[i]
        elif arr[i]>second & arr[i] != first:
            third = second
            second = arr[i]


        elif arr[i] > third & arr[i] != second:
            third = arr[i]


    print(first, second, third)




largest_three(arr)