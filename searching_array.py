ar = [10, 4, 3, 50, 23, 90]

def check(arr):
    max = []
    first=second=third=float('-inf')
    for i in arr:
        if i > first:
            third=second
            second=first
            first= i
        elif i >second:
            third=second
            second=i
        elif i>third:
            third = i
    return first,second,third




result = check(ar)
print(result)



