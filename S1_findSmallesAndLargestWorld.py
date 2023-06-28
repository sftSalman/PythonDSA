def find_smallest_largest_word(string):
    # Split the string into words
    words = string.split()

    # Initialize variables to store the smallest and largest word
    smallest_word = words[0]
    largest_word = words[0]

    # Iterate through each word in the list
    for word in words:
        # Update the smallest word if the current word is smaller
        if len(word) < len(smallest_word):
            smallest_word = word

        # Update the largest word if the current word is larger
        if len(word) > len(largest_word):
            largest_word = word

    return smallest_word, largest_word

s = "GeeksforGeeks A computer Science portal for Geeks"
print(find_smallest_largest_word(s))