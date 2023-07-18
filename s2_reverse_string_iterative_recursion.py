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
        return rev(st[1:]) + st[0]

# Example usage
st = "Hello, World!"
print(rev(st))
