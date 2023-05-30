arr = [4,6,3,7]


def tri(arr):
    c=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i]+arr[j]>arr[k] and arr[j]+arr[k]>arr[i] and arr[i]+arr[k]>arr[j]:
                    c += 1
    return c



tri(arr)
print(tri(arr))