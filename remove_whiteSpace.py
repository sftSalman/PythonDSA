def remove_extra_whitespace(input_string):
    # Initialize an empty list to store the cleaned words
    words = []

    # Split the input string by whitespace
    splitted_words = input_string.split()

    # Append non-empty words to the 'words' list
    for word in splitted_words:
        if word:
            words.append(word)

    # Join the words with a single space to form the cleaned string
    cleaned_string = " ".join(words)

    return cleaned_string

# Test the function
input_string = "    Hello     there!      "
result = remove_extra_whitespace(input_string)
print("String with extra whitespace removed:", result)
