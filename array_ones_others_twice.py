arr = [2, 3, 5, 4, 5, 3, 4]
one = []

def find_ones(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == arr[i-1]:
            count = count + 1
        else:
            return arr[i]




print(find_ones(arr))

