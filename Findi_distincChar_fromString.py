str = 'Easyone'

def find_distinct(arr):
    duplicate = []
    count = 0

    for ch in str:
        if ch.upper() not in duplicate:
            duplicate.append(ch)
            count += 1
    return duplicate,count

print(find_distinct(str))
