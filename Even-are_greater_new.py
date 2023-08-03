arr = [1, 23, 57, 0, 4, 0, 2, 4, 5, 0]


def moveZero(arr) :
    even = []
    others = []
    for i in range ( len ( arr ) ) :
        if arr[i]%2 == 0 :
            even.append ( arr[i] )
        else :
            others.append ( arr[i] )

    return even + others


print ( moveZero ( arr ) )
