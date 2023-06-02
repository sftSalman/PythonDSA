st = 'aabccccddddddd'

def freq(st):
    result = ''
    count = 1
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            count += 1
        else:
            result += st[i] + str(count)
            count = 1
    result += st[-1] + str(count)  # Add the last character and its count
    return result

print(freq(st))
