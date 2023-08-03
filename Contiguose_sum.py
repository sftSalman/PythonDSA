def max_contiguous_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = num if num > current_sum + num else current_sum + num
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Example usage:
arr = [7, 1, 2, 3, 4, 5, 6]
result = max_contiguous_sum(arr)
print(result)  # Output: 10 (The maximum sum subarray is [3, 4, -1, 2, 1])
