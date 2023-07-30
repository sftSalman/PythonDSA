def modify_string(input_string) :
    # Step 1: Replace "RL" with an empty string.
    input_string = input_string.replace ( 'RL', '' )

    # Step 2: Replace consecutive "L" with a single "L" and consecutive "R" with a single "R".
    modified_string = ''
    prev_char = ''

    for char in input_string :
        if char == prev_char :
            continue
        else :
            modified_string += char
            prev_char = char

    # Step 3: Remove first "L" and last "R" characters if they exist.
    if modified_string.startswith ( 'L' ) :
        modified_string = modified_string[1 :]
    if modified_string.endswith ( 'R' ) :
        modified_string = modified_string[:-1]

    return modified_string


def is_palindrome(string) :
    return string == string[: :-1]


# Example usage:
inputs = [
    "543L24R6",
    "34L5R43",
    "L33433R",
    "LL33433RRR",
    "RL36LR73",
]

for i, input_str in enumerate ( inputs, start = 1 ) :
    modified_str = modify_string ( input_str )
    is_palindrome_flag = is_palindrome ( modified_str )

    print ( f"Input{i}: {input_str}" )
    print ( f"Modified: {modified_str}" )

    if is_palindrome_flag :
        print ( f"{modified_str} is palindrome" )
    else :
        print ( f"{modified_str} is not palindrome" )

    print ()
