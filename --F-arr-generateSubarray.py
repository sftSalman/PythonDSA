def generate_subarrays(arr):
    subarrays = []
    n = len(arr)

    for start in range(n):
        for end in range(start, n):
            subarray = arr[start:end + 1]
            subarrays.append(subarray)

    return subarrays

arr = [1,2,3]
all_subarrays = generate_subarrays(arr)
print(*all_subarrays)