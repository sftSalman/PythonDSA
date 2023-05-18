arr = [1, 2, 4, 5, 6]

def missing(arr):
    arr_sum = 0
    n = len(arr) + 1
    total = (n * (n + 1)) // 2

    for num in arr:
        arr_sum += num

    return total - arr_sum

print(missing(arr))
