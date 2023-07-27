def calculate_arithmetic_series_sum(a, r, n, P):
    total_sum = 0

    for i in range(n + 1):
        term = a + i * r
        total_sum += term ** P

    return total_sum

# Input from the user
a = int(input("Enter the first term (a): "))
r = int(input("Enter the common difference (r): "))
n = int(input("Enter the number of terms (n): "))
P = int(input("Enter the power/exponent (P): "))

# Calculate and print the result
result = calculate_arithmetic_series_sum(a, r, n, P)
print("The sum of the arithmetic series is:", result)
