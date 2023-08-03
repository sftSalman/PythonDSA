arr = [16, 17, 4, 3, 5, 2]

def leaderOfArray(arr):
    n = len(arr)
    leader = []
    for i in range(n):
        is_leader = True
        for j in range(i+1, n):
            if arr[i] <= arr[j]:
                is_leader = False
                break
        if is_leader==True:
            leader.append(arr[i])
    return leader

print(leaderOfArray(arr))
