# st = 'abc'
# print(st[:])
# def rev(st):
#     return st[::-1]
#
# print(rev(st))
# # recursion

def rev(st):
    if len(st) <= 1:
        return st
    else:
        return  rev(st[1:]) +st[0]
#
# "d" + rev("lroW" + " " + "," + "o" + "l" + "l" + "e" + "H")
# "dl" + rev("roW" + " " + "," + "o" + "l" + "l" + "e" + "H")
# "dlr" + rev("oW" + " " + "," + "o" + "l" + "l" + "e" + "H")
# "dlro" + rev("W" + " " + "," + "o" + "l" + "l" + "e" + "H")
# "dlroW" + rev(" " + "," + "o" + "l" + "l" + "e" + "H")
# "dlroW " + rev("," + "o" + "l" + "l" + "e" + "H")
# "dlroW ," + rev("o" + "l" + "l" + "e" + "H")
# "dlroW ,o" + rev("l" + "l" + "e" + "H")
# "dlroW ,ol" + rev("l" + "e" + "H")
# "dlroW ,oll" + rev("e" + "H")
# "dlroW ,olle" + rev("H")
# "dlroW ,olleH"


# Example usage
st = "Hello, World!"
print(rev(st))
