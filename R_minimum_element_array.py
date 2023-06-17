arr = [1, 4, 3, -5, -4, 8, 6]


def minArr(arr) :
    min_element = float ( 'inf' )  # Initialize min_element with positive infinity

    for element in arr :
        if element < min_element :
            min_element = element

    return min_element


min_element = minArr ( arr )
print ( min_element )
