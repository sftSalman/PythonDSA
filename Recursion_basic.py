
#https://www.youtube.com/watch?v=IJDJ0kBx2LM&ab_channel=freeCodeCamp.org

def findLenght(st):
    count = 0
    for i in st:
        count = count + 1
    return count

print(findLenght('salman'))

def recur_lenght(st,idx=0):
