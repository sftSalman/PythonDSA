
str= "GeeksforGeeks is a computer science portal"
def findSubstring(str, given):
    if given in str:
        return True

print(findSubstring(str,'is'))