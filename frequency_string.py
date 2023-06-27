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

st = 'aabccccdd'
print(len(st))

def freq(st):
    result = ''
    count = 1
    for i in range(len(st)-1):
        print('loop:',i)
        if st[i] == st[i+1]:
            count += 1
        else:

            print('result is : ',result)
            print('count is ',str(count))
            result += st[i] + str(count)
            print('result after add ',result)

            count = 1
    print('do nothing, end of loop')
    print('result', result)
    print("count",str(count))
    print(st[-1])
    result += st[-1] + str(count)
    print('final result',result)# Add the last character and its count
    return result

print(freq(st))