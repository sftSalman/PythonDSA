arr = [1, 2, 2, 1]
even = []
odd = []

def even_odd(arr):
    for index, num in enumerate(arr):
        if index % 2 == 0:
            even.append(num)
            even.sort()
        else:
            odd.append(num)
            odd.sort()
    return even + odd

result = even_odd(arr)
print(*result)
