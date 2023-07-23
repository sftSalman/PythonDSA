
arr = [1,2,4,3,5,6,7,8,4,6,20]
# Searching in the array
def search(arr,n):
    if n in arr:
        return True
    else: return False

print(search(arr,5))
print(search(arr,100))

#  reversing an array

def reverse(arr):
    return arr[::-1]

print(reverse(arr))


arr.append(5)
print(arr)
arr.remove(20)
print(arr)


def sortARR(arr):

    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr


print(sortARR(arr))

