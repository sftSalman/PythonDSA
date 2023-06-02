s = 'geeksforgeeks'
ch = 'e'
n=s.replace(ch,'')
print(n)


def remove_char_list_comprehension(string, char):
    return "".join([c for c in string if c != char])