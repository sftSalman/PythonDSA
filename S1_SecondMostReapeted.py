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
