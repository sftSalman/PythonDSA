arr = [1, 4, 20, 3, 10, 5]
sum =6

def findSum(arr,sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                return arr[i],arr[j]
    return None


result = findSum(arr, sum)
if result:
    print("Pair found:", result)
else:
    print("No pair found with the given sum.")