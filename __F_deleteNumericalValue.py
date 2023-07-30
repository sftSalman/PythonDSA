def delNumeric(s):
    new_str = ''

    for ch in s:
        if not ch.isdigit():
            new_str += ch

    return new_str

def check_expressions_similarity(expr1, expr2):
    modified_expr1 = delNumeric(expr1)
    modified_expr2 = delNumeric(expr2)

    if modified_expr1 == modified_expr2:
        return "Two expressions are identical"
    else:
        return "Two expressions are different"

# Example usage:
input1 = "5a-b-c+6d"
input2 = "5a-b-c+6d"
print("Input1:", input1, "&", input2)
print("Output1:", check_expressions_similarity(input1, input2))

input3 = "2a-b-(3c-d)"
input4 = "5a-b-c-6d"
print("Input2:", input3, "&", input4)
print("Output2:", check_expressions_similarity(input3, input4))
