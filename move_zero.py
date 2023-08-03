arr = [1,23,57,0,4,0,2,4,5,0]

def moveZero(arr):
    zero = []
    others=[]
    for i in range(len(arr)):
        if arr[i]==0:
            zero.append(arr[i])
        else:
            others.append(arr[i])



    return others + zero


print(moveZero(arr))
