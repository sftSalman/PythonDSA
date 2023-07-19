def deciTobinary(n, r):
    if n == 0:
        return r if r else "0"
    else:
        r = str(n % 2) + r
        return deciTobinary(n // 2, r)

# Example usage
n = 12
binary_representation = deciTobinary(n, '')
print(binary_representation)
