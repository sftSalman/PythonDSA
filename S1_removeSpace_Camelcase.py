def convert_to_camel_case(sentence) :
    # Split the sentence into individual words
    words = sentence.split ()

    # Convert the first word to lowercase
    first_word = words[0].lower ()

    # Capitalize the first letter of each remaining word
    capitalized_words = []
    for i in range ( 1, len ( words ) ) :
        word = words[i]
        capitalized_word = word.capitalize ()
        capitalized_words.append ( capitalized_word )

    # Join the lowercase first word with the capitalized remaining words
    camel_case = first_word + ''.join ( capitalized_words )

    return camel_case


print(convert_to_camel_case('Hello, how are you?'))