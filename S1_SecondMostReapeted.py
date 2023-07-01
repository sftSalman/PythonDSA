def find_second_most_repeated_word(sequence):
    word_count = {}

    # Count the frequency of each word
    for word in sequence:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_repeated = None
    second_most_repeated = None

    # Find the most and second most repeated words
    for word, count in word_count.items():
        if most_repeated is None or count > word_count[most_repeated]:
            second_most_repeated = most_repeated
            most_repeated = word
        elif second_most_repeated is None or count > word_count[second_most_repeated]:
            second_most_repeated = word

    return second_most_repeated


sequence = ["apple", "banana", "apple", "cherry"]
second_most_repeated = find_second_most_repeated_word(sequence)
print(second_most_repeated)


# Initialize an empty dictionary called word_count.
# Iterate through the sequence ["apple", "banana", "apple", "cherry", "banana", "banana"].
# For the first word "apple":
# Since "apple" is not in word_count, add it as a key with a count of 1.
# For the second word "banana":
# Since "banana" is not in word_count, add it as a key with a count of 1.
# For the third word "apple":
# Since "apple" is already in word_count, increment its count by 1.
# For the fourth word "cherry":
# Since "cherry" is not in word_count, add it as a key with a count of 1.
# For the fifth word "banana":
# Since "banana" is already in word_count, increment its count by 1.
# For the sixth word "banana":
# Since "banana" is already in word_count, increment its count by 1.
# word_count dictionary now contains the word counts: {'apple': 2, 'banana': 3, 'cherry': 1}.
# Initialize variables most_repeated and second_most_repeated as None.
# Iterate through the items of word_count dictionary.
# For the first item ('apple', 2):
# Since most_repeated is None, update most_repeated to 'apple'.
# For the second item ('banana', 3):
# Since most_repeated is not None, compare the count (3) with the count of most_repeated (2).
# Since 3 > 2, update second_most_repeated to 'apple' and most_repeated to 'banana'.
# For the third item ('cherry', 1):
# Since most_repeated is not None, compare the count (1) with the count of most_repeated (3).
# Since 1 < 3, second_most_repeated remains 'apple'.
# second_most_repeated variable now holds 'apple', which is the second most repeated word.
# Print the value of second_most_repeated.
# Output: 'apple'
# The output indicates that 'apple' is the second most repeated word in the given sequence ["apple", "banana", "apple", "cherry", "banana", "banana"].
#
# Please note that if there is a tie for the second most repeated word (multiple words with the same frequency), this implementation will return the first encountered word with that frequency.