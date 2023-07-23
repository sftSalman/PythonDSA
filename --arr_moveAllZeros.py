# arr = [1, 2, 0, 4, 3, 0, 5, 0]
#
# def moveZeros(arr):
#     none_zero = []
#     zero = []
#     count = 0
#
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             zero.append(arr[i])
#         if arr[i] !=0:
#             none_zero.append(arr[i])
#
#     return none_zero + zero
#
#
# print(moveZeros(arr))


arr = [1, 2, 0, 4, 3, 0, 5, 0]

# def moveZeros(arr):
#     count = 0
#     n = len(arr)
#
#     for i in range(n):
#         if arr[i]!=0:
#             arr[count] = arr[i]
#             count = count + 1
#     return arr
#
#
#     # while count <n :
#     #     arr[count]=0
#     #     count += 1
#
#     return arr
#
#
#
# print(moveZeros(arr))

def push_zeros_to_end(arr):
    n = len(arr)
    count_zeros = 0

    # Traverse the array and move all non-zero elements to the front
    for i in range(n):
        if arr[i] != 0:
            arr[count_zeros], arr[i] = arr[i], arr[count_zeros]
            count_zeros += 1

    # Fill the remaining elements with zeroes
    while count_zeros < n:
        arr[count_zeros] = 0
        count_zeros += 1

    return arr

# Example usage:
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
result = push_zeros_to_end(arr)
print(result)
