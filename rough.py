arr = [1, 1, 1, 2, 2, 3, 4, 4]
new_arr = []

def distc(arr):
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            new_arr.append(arr[i])

distc(arr)
print(new_arr)

# Call distc function again with the new_arr

