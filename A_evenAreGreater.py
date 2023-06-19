arr = [1, 2, 2, 1]
even = []
odd = []

def even_odd(arr):
    for index, num in enumerate(arr):
        if index % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    #Implement a sorting algorithm (e.g., Bubble Sort) for even and odd lists
    for i in range(len(even)):
        for j in range(0, len(even) - i - 1):
            if even[j] > even[j + 1]:
                even[j], even[j + 1] = even[j + 1], even[j]

    for i in range(len(odd)):
        for j in range(0, len(odd) - i - 1):
            if odd[j] > odd[j + 1]:
                odd[j], odd[j + 1] = odd[j + 1], odd[j]

    return even + odd

result = even_odd(arr)
print(*result)