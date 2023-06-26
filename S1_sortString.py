str = "cdaefz"

def sortString(str):
    char_list = list(str)  # Convert the string to a list of characters

    for i in range(len(char_list) - 1):
        for j in range(len(char_list) - 1 - i):
            if char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]

    sorted_str = "".join(char_list)  # Join the sorted characters back into a string
    return sorted_str

print(sortString(str))
