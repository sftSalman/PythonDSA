def stringRemove(s) :
    new_string = ''
    prev_char_is_space = False

    for ch in s :
        if ch.isalnum () or ch.isspace () :
            if not (prev_char_is_space and ch.isspace ()) :
                new_string += ch

            prev_char_is_space = ch.isspace ()

    return new_string.strip ()


str_example = 'Trim       white       spaces.'
print ( stringRemove ( str_example ) )
