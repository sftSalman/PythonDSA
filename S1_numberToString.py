n = 1024

def numberToString(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if n < 10:
        return ones[n]
    elif n < 20:
        return teens[n - 10]
    elif n < 100:
        ten_digit = n // 10
        one_digit = n % 10
        return tens[ten_digit] + ' ' + ones[one_digit] if one_digit != 0 else tens[ten_digit]
    elif n<1000:
        hundrad_digit = n//100
        remainder = n%100
        if remainder == 0:
            return ones[hundrad_digit] + ' '+ 'hundrad'
        else:return ones[hundrad_digit] + " "+ 'hundrad' + ' '+ numberToString((remainder))

    elif n< 10000:
        thousand_digit = n//1000
        remainder = n% 1000

        if remainder == 0:
            return  ones[thousand_digit]+"  "+'thousand'
        else: return ones[thousand_digit]+"  "+'thousand' + numberToString(remainder)

print(numberToString(9220))
