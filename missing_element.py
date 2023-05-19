arr = [6,1,2,8,3,4,7,10,5]

def missing(arr):
    arr_sum = 0
    n = len(arr) + 1
    total = (n * (n + 1)) // 2

    for num in arr:
        arr_sum += num

    return total - arr_sum

print(missing(arr))
