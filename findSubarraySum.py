def find_subarray_with_given_sum(arr, target_sum):
    n = len(arr)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target_sum:
                return arr[i:j+ 1]
            elif current_sum > target_sum:
                break

    return None  # If no subarray is found with the given sum

# Example usage:
arr = [1, 4, 20, 3, 10, 5]
sum_to_find = 33
result = find_subarray_with_given_sum(arr, sum_to_find)
print(result)  # Output: [20, 3, 10
