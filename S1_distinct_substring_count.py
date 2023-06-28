def printAllSubstrings(s, n) :
    # Fix start index in outer loop.
    # Reveal new character in inner loop till end of string.
    # Print till-now-formed string.
    substring = [""]
    for i in range ( n ) :
        temp = ""
        for j in range ( i, n ) :
            # print('temp:',temp)
            # print('s[j]',s[j])
            temp += s[j]
            substring.append(temp)
            # print('after ',temp)
    return len(substring)


# Driver program to test above function

s = "gfg"
print(printAllSubstrings ( s, len ( s ) ))