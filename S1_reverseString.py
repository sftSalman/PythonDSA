def reverse_string(string):
    if len(string) <= 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


# Example usage
str = 'salman farshi '
print(str[1:])
reversed_str = reverse_string(str)
print(reversed_str)
