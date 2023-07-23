
arr = [1,2,44,2,4,4,10]

def largestThree(arr):
    first,second,third = -9999999999999999,-999999999,-9999999999
    for i in range(len(arr)):
        if arr[i]>first:
            second = third
            third = first
            first = arr[i]
        elif arr[i]>second and arr[i] != first:
            third = second
            second = arr[i]
        elif arr[i] > third and arr[i] != second:
            third = arr[i]

    return first,second,third


print(largestThree(arr))



