arr = [1, 2, 2, 1]
even = []
odd = []

def even_odd(arr):
    for index, num in enumerate(arr):
        if index % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return (even + odd)

print(even_odd(arr))
