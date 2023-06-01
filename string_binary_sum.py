def binary_sum(strings):
    decimal_sum = sum(int(string, 2) for string in strings)
    binary_sum = bin(decimal_sum)[2:]
    return binary_sum

# Example usage
binary_strings = ['110', '101', '111']
result = binary_sum(binary_strings)
print(result)  # Output: 10010
