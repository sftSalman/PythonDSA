arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]

def evenAreGreater(arr):
    even = []
    odd = []
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd


print(evenAreGreater(arr))