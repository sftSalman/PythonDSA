# String in which a character to be searched.
str = "GeeksforGeeks is a computer science portal"

# Returns index of first occurrence of character.
firstIndex = str.find('s')
print("First occurrence of char 's' is found at:", firstIndex)

# Returns index of last occurrence specified character.
lastIndex = str.rfind('s')
print("Last occurrence of char 's' is found at:", lastIndex)

# Index of the first occurrence of specified char after the specified index if found.
first_in = str.find('s', 10)
print("First occurrence of char 's' after index 10:", first_in)

last_in = str.rfind('s', 20)
print("Last occurrence of char 's' after index 20 is:", last_in)

# gives Unicode code point value of character at location 20
char_at = ord(str[20])
print("Character at location 20:", char_at)

# Note: If we uncomment it will throw IndexError
# char_at = str[50]
