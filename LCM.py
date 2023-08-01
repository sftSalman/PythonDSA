def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_array_elements(arr):
    if len(arr) == 0:
        raise ValueError("Array is empty, cannot find LCM.")

    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])

    return result

# Example usage:
arr = [3, 6, 12, 18]
result = lcm_of_array_elements(arr)
print("LCM of the array elements:", result)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_array_elements(arr):
    if len(arr) == 0:
        raise ValueError("Array is empty, cannot find GCD.")

    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])

    return result

# Example usage:
arr = [24, 36, 48]
result = gcd_of_array_elements(arr)
print("GCD of the array elements:", result)
