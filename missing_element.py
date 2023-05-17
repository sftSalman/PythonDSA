def findMissing(arr, N):
    # create a list of zeroes
    temp = [0] * (N + 1)

    for i in range(0, N):
        temp[arr[i] - 1] = 1

    for i in range(0, N + 1):
        if (temp[i] == 0):
            ans = i + 1

    print(ans)
findMissing([1,2,4,6,3,7,8],len([1,2,4,6,3,7,8]))