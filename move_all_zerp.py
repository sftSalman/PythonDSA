arr = [1, 2, 0, 4, 3, 0, 5, 0]

def move_zero(arr):
    zero_count = arr.count(0)  # Count the number of zeros in the list
    arr = [num for num in arr if num != 0]  # Create a new list without zeros
    arr.extend([0] * zero_count)  # Append the required number of zeros at the end
    return arr

print(move_zero(arr))
