str = 'salman'

def reverseStr(str):
    n = len(str)
    str1 = ''
    idx = n - 1
    for i in str:
        str1 = str1 + str[idx]
        idx = idx - 1
    return str1  # Return the reversed string

reversed_str = reverseStr(str)
print(reversed_str)  # Print the reversed string

# Alternatively, you can directly print the reversed string without storing it in a separate variable
print(reverseStr(str))  # Print the reversed string
